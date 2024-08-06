import cv2

#이미지 출력
image = cv2.imread("Study_Py_OpenCV/lunar.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()

#비디오 출력
capture = cv2.VideoCapture("Study_Py_OpenCV/sample.mp4")
capture.isOpened() # 파일 읽기 성공 여부 확인

while cv2.waitKey(33) < 0:
    # CAP_PROP_POS_FRAMES = 동영상의 현재 프레임 수  //  CAP_PROP_FRAME_COUNT = 동영상의 총 프레임 수
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT): 
        capture.set(cv2.CAP_PROP_FRAMES, 0) # 동영상의 현재 프레임 수 초기화

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.releas()
cv2.destroyAllWindows()