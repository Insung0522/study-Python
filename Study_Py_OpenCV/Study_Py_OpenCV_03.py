import cv2

# 대칭
src = cv2.imread("Study_Py_OpenCV/src/glass.jpg", cv2.IMREAD_COLOR)
# flipCode < 0 : XY축 대칭
# flipCode = 0 : X축 대칭
# flipCode > 0 : Y축 대칭
dst = cv2.flip(src, 0)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 회전
src = cv2.imread("Study_Py_OpenCV/src/ara.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape # 해당 이미지의 높이, 넓이, 채널 값 지정
# 2X3 회전 행렬 생성 함수. 회전 변환 행렬을 계산
# getRotationMatrix2D(center, angle, scale) center = 중심점, angle = 각도, scale = 비율로 매핑 변환 행렬 생성
# 중심점은 튜플 형태로 기준점 설정
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) 
# warpAffine(원본 이미지, 아핀 맵 행렬, 출력 이미지 크기)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 확대 & 축소
src = cv2.imread("Study_Py_OpenCV/src/fruits.jpg", cv2.IMREAD_COLOR)
height, width, cahnnel = src.shape
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.imshow("dst2",dst)
cv2.waitKey()       
cv2.destroyAllWindows()

# 크기 조절

src = cv2.imread("Study_Py_OpenCV/src/champagne.jpg", cv2.IMREAD_COLOR)
# resize(원본(src), 절대크기(dstSize), 상대크기(fx, fy), 보간법(interpolation))
dst = cv2.resize(src, dsize = (640, 480), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0,0), fx = 0.3, fy = 0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()