import cv2

# 设置初始窗口大小
cv2.namedWindow("camera", cv2.WINDOW_NORMAL)
#窗口命名为camera，窗口尺寸 800* 600
cv2.resizeWindow("camera", 800, 600)

# 输入视频地址就是读取视频
#video = cv2.VideoCapture('../videos/1.mp4')
# 输入0就是表示读取0号摄像头
video = cv2.VideoCapture(0)

# 判断视频视频是否能够打开
while video.isOpened():
    # 读取每一帧图片，第一个返回值为True或者False，表示是否读取成功，第二个就是读取的图像
    ret, frame = video.read()
    # 读取视频就退出循环
    if not ret:
        break
    # 展示每一帧图片
    cv2.imshow("camera", frame)
    # 等待10毫秒用户输入
    key = cv2.waitKey(10)
    # 输入q就用 break 退出while循环
    if key & 0xFF == ord('q'):
        break

# 释放资源，关闭窗口
video.release()
cv2.destroyAllWindows()