import cv2

src = cv2.imread("Study_Py_OpenCV/src/crow.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#dst2 = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 역상(Reverse Image)은 영상이나 이미지를 반전 된 색상으로 변환하기 위해서 사용합니다.
# 픽셀 단위마다 비트 연산(Bitwise Operation)을 적용하는데, 그중 NOT 연산을 적용합니다.
# NOT 연산은 각 자릿수의 값을 반대로 바꾸는 연산입니다.
# 만약 153의 값을 갖는 픽셀에 NOT 연산을 적용한다면 102의 값으로 변경됩니다.
# 153은 0b10011001의 값을 가지며, 102는 0b01100110의 값을 갖습니다.
# 즉, 10 진수의 픽셀값을 2 진수의 값으로 변경한 다음, 각 자릿수의 값을 반대로 바꾸게 됩니다.
# 1은 0이 되며, 0은 1로 변경됩니다.

src = cv2.imread("Study_Py_OpenCV/src/whitebutterfly.jpg", cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()