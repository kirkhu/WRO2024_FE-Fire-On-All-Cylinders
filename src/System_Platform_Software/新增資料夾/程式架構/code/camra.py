import cv2
import numpy as np
import glob

# 設置棋盤格的大小 (內角點數量)
checkerboard_size = (8, 5)

# 準備 3D 世界座標系中的點
objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)

# 儲存 3D 和 2D 點的列表
objpoints = []  # 存儲世界座標系中的 3D 點
imgpoints = []  # 存儲影像中的 2D 點

# 使用 GStreamer 管道打開 CSI 鏡頭
cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink", cv2.CAP_GSTREAMER)

# 檢查攝像頭是否打開
if not cap.isOpened():
    print("無法打開攝像頭")
    exit()

image_count = 0  # 記錄拍照的影像數量

while True:
    ret, frame = cap.read()  # 從攝像頭讀取影像
    if not ret:
        print("無法從攝像頭獲取影像")
        break

    # 顯示攝像頭畫面
    cv2.imshow('Press Space to Capture', frame)

    key = cv2.waitKey(1)

    # 按下空白鍵 ('space') 拍照進行校準
    if key & 0xFF == ord(' '):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 將影像轉換為灰階
        
        # 查找棋盤格的內角點
        ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE)

        if ret:
            objpoints.append(objp)  # 儲存世界坐標點
            # 提高角點檢測的精度
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
            imgpoints.append(corners2)  # 儲存影像坐標點
            
            # 繪製角點並顯示
            frame = cv2.drawChessboardCorners(frame, checkerboard_size, corners2, ret)
            print(f"檢測到棋盤格內角點，角點數量: {len(corners2)}")

            # 保存校準影像
            image_path = f'calibration_image_{image_count}.jpg'
            cv2.imwrite(image_path, frame)
            print(f'影像已保存至: {image_path}')
            image_count += 1
        else:
            print("未能檢測到棋盤格內角點，請重試。")

    # 按下 'q' 鍵退出
    if key & 0xFF == ord('q'):
        break

# 完成後關閉攝像頭
cap.release()
cv2.destroyAllWindows()

# 檢查是否有足夠的校準影像
if len(objpoints) > 0 and len(imgpoints) > 0:
    # 使用已檢測到的點進行鏡頭校準
    ret, camera_matrix, distortion_coefficients, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # 打印校準結果
    print(f"相機矩陣:\n{camera_matrix}")
    print(f"畸變係數:\n{distortion_coefficients}")

    # 保存校準數據
    np.savez("calibration_data.npz", camera_matrix=camera_matrix, distortion_coefficients=distortion_coefficients)
    print("校準數據已保存至 'calibration_data.npz'")
else:
    print("未收集到足夠的影像資料進行校準。")
