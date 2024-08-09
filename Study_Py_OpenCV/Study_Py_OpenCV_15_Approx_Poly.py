# 영상이나 이미지의 윤곽점을 압축해 다각형으로 근사하기 위해 사용합니다.
# 영상이나 이미지에서 윤곽선의 근사 다각형을 검출할 수 있습니다.
import cv2

src = cv2.imread("Study_Py_OpenCV/src/phone.png", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

# 반복문을 사용하여 색인값과 하위 윤곽선 정보로 반복합니다.
# 근사치 정확도를 계산하기 위해 윤곽선 전체 길이의 2%로 활용합니다
# 윤곽선의 전체 길이를 계산하기 위해 cv2.arcLength()을 이용해 검출된 윤곽선의 전체 길이를 계산합니다.
# cv2.arcLength(윤곽선, 폐곡선)을 의미합니다.
# 윤곽선은 검출된 윤곽선들이 저장된 Numpy 배열입니다.
# 폐곡선은 검출된 윤곽선이 닫혀있는지, 열려있는지 설정합니다.
# Tip : 폐곡선을 True로 사용할 경우, 윤곽선이 닫혀 최종 길이가 더 길어집니다. (끝점 연결 여부를 의미)
for contour in contours:
    epsilon = cv2.arcLength(contour, True) * 0.02
    # cv2.approxPolyDP()를 활용해 윤곽선들의 윤곽점들로 근사해 근사 다각형으로 반환합니다.
    # cv2.approxPolyDP(윤곽선, 근사치 정확도, 폐곡선)을 의미합니다.
    # 윤곽선은 검출된 윤곽선들이 저장된 Numpy 배열입니다.
    # 근사치 정확도는 입력된 다각형(윤곽선)과 반환될 근사화된 다각형 사이의 최대 편차 간격을 의미합니다.
    # 폐곡선은 검출된 윤곽선이 닫혀있는지, 열려있는지 설정합니다.
    # Tip : 근사치 정확도의 값이 낮을 수록, 근사를 더 적게해 원본 윤곽과 유사해집니다.    
    approx_poly = cv2.approxPolyDP(contour, epsilon, True)

    # 다시 반복문을 통해 근사 다각형을 반복해 근사점을 이미지 위해 표시합니다.
    # 근사 다각형의 정보는 윤곽선의 배열 형태와 동일합니다.
    for approx in approx_poly:
        cv2.circle(src, tuple(approx[0]), 3, (255, 0, 0), -1)

cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 추가 정보
# 다각형 근사는 더글라스-패커(Douglas-Peucker) 알고리즘을 사용합니다.
# 반복과 끝점을 이용해 선분으로 구성된 윤곽선들을 더 적은 수의 윤곽점으로 동일하거나 비슷한 윤곽선으로 데시메이트(decimate)합니다.
# 더글라스-패커 알고리즘은 근사치 정확도(epsilon)의 값으로 기존의 다각형과 윤곽점이 압축된 다각형의 최대 편차를 고려해 다각형을 근사하게 됩니다.
# Tip : 데시메이트란 일정 간격으로 샘플링된 데이터를 기존 간격보다 더 큰 샘플링 간격으로 다시 샘플링하는 것을 의미합니다.