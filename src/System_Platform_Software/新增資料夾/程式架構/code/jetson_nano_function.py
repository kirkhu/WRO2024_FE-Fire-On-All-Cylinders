import cv2
import numpy as np
import serial as AC
import struct


color_ranges = {
    'Orange': ([10, 180, 115], [20, 255, 180], (0, 165, 255)),
    'Blue': ([105, 115, 95], [140, 180, 135], (255, 0, 0))
}
color_ranges_final = {
    'Orange': ([10, 180, 115], [20, 255, 180], (0, 165, 255)),
    'Blue': ([105, 115, 95], [140, 180, 135], (255, 0, 0)),
    'Red': ([0, 175, 80], [10, 235, 170], (0, 0, 255)),
    'Green': ([50, 120, 85], [65, 195, 180], (0, 255, 0)),
    'Pink': ([160, 80, 64], [175, 175, 190], (255, 192, 203))
}

current_last = 0
def process_roi(undistorted_frame, x1, y1, x2, y2, threshold_value=90):
    roi = undistorted_frame[y1:y2, x1:x2]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)

    # 找到所有的轮廓
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 如果有轮廓，找到面积最大的轮廓
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        black_pixels = int(cv2.contourArea(largest_contour))  # 将黑色像素转换为整数
        # 画出最大的轮廓
        cv2.drawContours(binary, [largest_contour], -1, (255, 255, 255), -1)
    else:
        black_pixels = 0

    return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR), black_pixels

def detect_color(undistorted_frame):
    hsv_frame = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2HSV)
    color_y_positions = []

    for color, (lower, upper, bgr) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        color_mask = cv2.inRange(hsv_frame, lower, upper)
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 500:  # 过滤小面积的杂讯
                x, y, w, h = cv2.boundingRect(largest_contour)
                center_y = y + h // 2
                cv2.rectangle(undistorted_frame, (x, y), (x + w, y + h), bgr, 2)
                cv2.circle(undistorted_frame, (x + w // 2, center_y), 5, bgr, -1)  # 标记中心点
                color_y_positions.append(center_y)
            else:
                color_y_positions.append(0)  # 如果未找到有效轮廓，返回 0
        else:
            color_y_positions.append(0)  # 如果未找到轮廓，返回 0

    return color_y_positions

def pd_control(target, current, kp, kd):
    global current_last  # 使用全局变量
    error = current - target
    derivative = current - current_last
    control_signal = -(kp * error + kd * derivative)
    current_last =  current  # 在 return 之前更新 current_last
    return control_signal
def draw_multiple_curves(undistorted_frame, start_points, end_points, slope_values, curvature_factors, colors, thickness=2):
    """
    在图像上绘制多个不同起点、终点、斜率和弯曲度的曲线，并返回红色曲线的坐标列表。
    """
    red_curve_points = []  # 用来保存红色曲线的点坐标
    green_curve_points = []  # 用来保存红色曲线的点坐标


    for start_point, end_point, slope, curvature, color in zip(start_points, end_points, slope_values, curvature_factors, colors):
        x1, y1 = start_point
        x2, y2 = end_point

        # 计算中间控制点的位置来控制弯曲程度
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        control_x = mid_x
        control_y = int(mid_y - curvature * slope * (x2 - x1))  # 使用弯曲度和斜率来调整中间控制点

        # 使用贝塞尔曲线绘制
        curve_points = []
        for t in np.linspace(0, 1, 100):
            xt = (1 - t)**2 * x1 + 2 * (1 - t) * t * control_x + t**2 * x2
            yt = (1 - t)**2 * y1 + 2 * (1 - t) * t * control_y + t**2 * y2
            curve_points.append((int(xt), int(yt)))

        # 如果是红色曲线，保存点坐标
        if color == (0, 0, 255):  # 红色曲线
            red_curve_points = curve_points
        if color == (0, 255, 0):  # 红色曲线
            green_curve_points = curve_points

        # 绘制曲线
        for i in range(len(curve_points) - 1):
            cv2.line(undistorted_frame, curve_points[i], curve_points[i + 1], color, thickness)

    return red_curve_points,green_curve_points  # 返回红色曲线的点坐标


def detect_color_final(undistorted_frame, last_red_x_diff, last_green_x_diff, start_points, end_points, slope_values, curvature_factors, colors):
    """检测特定颜色的区域并返回颜色中心点的 Y 坐标，并计算红色曲线点 X 与红中心点 X 的差值，绿色为中心点 X 减函数 X"""
    hsv_frame = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2HSV)
    color_y_positions = [0]*5
    center_x = 0
    center_y = 0
    red_x_diff = 0  # 默认设为 0
    green_x_diff = 0  # 默认设为 0
    

    # 颜色检测
    for color, (lower, upper, bgr) in color_ranges_final.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        color_mask = cv2.inRange(hsv_frame, lower, upper)
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            if color == 'Pink':
                # 对于 Pink，检查所有面积大于 500 的色块
                for contour in contours:
                    if cv2.contourArea(contour) > 1000:
                        x, y, w, h = cv2.boundingRect(contour)
                        center_x = x + w // 2
                        center_y = y + h // 2
                        color_y_positions.append(center_y)

                        # 绘制矩形框和颜色对应的中心点
                        cv2.rectangle(undistorted_frame, (x, y), (x + w, y + h), bgr, 2)
                        cv2.circle(undistorted_frame, (center_x, center_y), 5, bgr, -1)
            else:
                # 对于其他颜色，只找最大轮廓
                largest_contour = max(contours, key=cv2.contourArea)
                if cv2.contourArea(largest_contour) > 500:  # 过滤小面积的噪声
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    center_x = x + w // 2
                    center_y = y + h // 2
                    color_y_positions.append(center_y)

                    # 绘制矩形框和颜色对应的中心点
                    cv2.rectangle(undistorted_frame, (x, y), (x + w, y + h), bgr, 2)
                    cv2.circle(undistorted_frame, (center_x, center_y), 5, bgr, -1)

            # 使用多条不同的曲线和动态起点、终点
            red_curve_points,green_curve_points = draw_multiple_curves(undistorted_frame, start_points, end_points, slope_values, curvature_factors, colors)


            # 检查红色曲线和检测横线交点，并计算红色曲线点和中心点的 X 坐标差值
            if color == 'Red':
                max_curve_y = max([pt[1] for pt in red_curve_points])  # 获取红色曲线的最高点
                if center_y < max_curve_y:
                    for curve_x, curve_y in red_curve_points:
                        if abs(curve_y - center_y) < 2:  # 查找红色曲线和中心点的交点
                            red_x_diff = curve_x - center_x  # 计算红色 X 坐标的差值
                            cv2.circle(undistorted_frame, (curve_x, curve_y), 6, (0, 0, 255), -1)  # 用红色标记交点
                            break
                    else:
                        red_x_diff = last_red_x_diff  # 没有交点，使用上一帧的值
                else:
                    red_x_diff = 0  # 如果中心点高于曲线，设为 0

            # 检查绿色曲线和检测横线交点，并计算绿色中心点 X 减曲线点 X 的差值
            if color == 'Green':
                max_curve_y = max([pt[1] for pt in green_curve_points])  # 获取绿色曲线的最高点
                if center_y < max_curve_y:
                    for curve_x, curve_y in green_curve_points:
                        if abs(curve_y - center_y) < 2:  # 查找绿色曲线和中心点的交点
                            green_x_diff = center_x - curve_x  # 计算绿色 X 坐标的差值
                            cv2.circle(undistorted_frame, (curve_x, curve_y), 6, (0, 255, 0), -1)  # 用绿色标记交点
                            break
                    else:
                        green_x_diff = last_green_x_diff  # 没有交点，使用上一帧的值
                else:
                    green_x_diff = 0  # 如果中心点高于曲线，设为 0
        else:
            color_y_positions.append(0)  # 未找到轮廓，返回 0

    return color_y_positions, red_x_diff, green_x_diff  # 返回颜色中心的 Y 坐标和红绿 X 差值
