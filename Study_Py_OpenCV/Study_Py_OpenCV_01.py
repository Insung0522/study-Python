import cv2

#카메라 구동
capture = cv2.VideoCapture(0)
#capture.set(porpid, value)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#cv2.waitKey(지연시간 ms)
#while cv2.waitKey(33) < 0:
while cv2.waitKey(33) != ord('q'):
    #카메라의 상태 및 프레임 받아오기 capture.read()
    #ret은 정상 작동시 Ture 반환. frame에 현재 시점의 프레임 저장
    ret, frame = capture.read()
    #cv2.imshow("윈도우창 제목", 이미지(mat))
    cv2.imshow("VideoFrame", frame)

#카메라 장치에서 받아온 메모리 해제
capture.release()
#모든 윈도우 창 제거 함수
#특정 창만 닫는다면 cv2.destroyWindow(이름)
cv2.destroyAllWindows()