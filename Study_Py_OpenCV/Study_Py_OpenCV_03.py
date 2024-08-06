import cv2

# 대칭
src = cv2.imread("Study_Py_OpenCV/glass.jpg", cv2.IMREAD_COLOR)
# flipCode < 0 : XY축 대칭
# flipCode = 0 : X축 대칭
# flipCode > 0 : Y축 대칭
dst = cv2.flip(src, 0)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 회전
src = cv2.imread("Study_Py_OpenCV/ara.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape # 해당 이미지의 높이, 넓이, 채널 값 지정
# 2X3 회전 행렬 생성 함수. 회전 변환 행렬을 계산
# getRotationMatrix2D(center, angle, scale) center = 중심점, angle = 각도, scale = 비율로 매핑 변환 행렬 생성
# 중심점은 튜플 형태로 기준점 설정
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) 
print(matrix)
# warpAffine(원본 이미지, 아핀 맵 행렬, 출력 이미지 크기)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()