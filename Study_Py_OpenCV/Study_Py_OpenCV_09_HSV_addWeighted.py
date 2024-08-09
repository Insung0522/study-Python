# 영상이나 이미지에서 색상을 검출 할 때, 배열 요소의 범위 설정 함수(cv2.inRange)의 영역이 한정되어 색상을 설정하는 부분이 제한되어 있습니다.
# 예를 들어, 빨간색 영역을 검출하려 할 때, 빨간색 영역이 약 0 ~ 5와 약 170 ~ 179으로 범위가 두 가지로 나눠져 있습니다.
# 이 문제를 해결하려면 배열 요소의 범위 설정 함수를 두 개의 범위로 설정하고 검출한 두 요소의 배열을 병합해서 하나의 공간으로 만들어야 합니다.
# 이때 배열 병합 함수를 사용하며, 서로 다른 두 범위의 배열을 병합할 때 사용합니다.
import cv2

src = cv2.imread("Study_Py_OpenCV/src/tomato.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 빨간색 영역은 0 ~ 5, 170 ~ 179의 범위로 두 부분으로 나뉘어 있습니다.
# 이때, 두 부분을 합쳐서 한 번에 출력하기 위해서 사용합니다.
# 배열 요소의 범위 설정 함수(cv2.inRange)를 사용하여 빨간색 영역의 범위를 검출합니다.
# 배열 요소 범위 설정 함수는 다채널 이미지도 한 번에 범위를 설정할 수 있습니다.
# 색상을 분리한 두 배열을 배열 병합 함수(cv2.addWeighted)로 입력된 두 배열의 하나로 병합합니다.
# dst = cv2.addWeighted(src1, alpha, src2, beta, gamma, dtype = None)은 입력 이미지1(src1)에 대한 가중치1(alpha) 곱과 입력 이미지2(src2)에 대한 가중치2(beta) 곱의 합에 추가 합(gamma)을 더해서 계산합니다.
# 정밀도(dtype)은 출력 이미지(dst)의 정밀도를 설정하며, 할당하지 않을 경우, 입력 이미지1과 같은 정밀도로 할당됩니다.
# 두 이미지를 그대로 합칠 예정이므로, 가중치1과 가중치2의 값은 1.0으로 사용하고, 추가 합은 사용하지 않으므로 0.0을 할당합니다.
# 배열 병합 함수는 다음과 같은 수식으로 나타낼 수 있습니다.
# dst = src1 X alpha + src2 X beta + gamma
# Tip : 배열 병합 함수는 알파 블렌딩(alpha blending)을 구현할 수 있어 서로 다른 이미지를 불투명하게 혼합해서 표시할 수 있습니다.
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

red = cv2.bitwise_and(hsv, hsv, mask = added_red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

cv2.imshow("red", red)
cv2.waitKey()
cv2.destroyAllWindows()