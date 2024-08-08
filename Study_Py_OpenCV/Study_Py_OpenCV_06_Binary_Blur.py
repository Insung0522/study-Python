import cv2

src = cv2.imread("Study_Py_OpenCV/src/geese.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src,  cv2.COLOR_BGR2GRAY)
# retval, dst = cv2.threshold(src, thresh,masxval, type)은 입력 이미지(src)를 
# 입곗값 형식(type)에 따라 임곗값(thresh)과 최댓값(maxval)을 활용하여 설정 임곗값(retval)과 결과 이미지(dst) 반환
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# 입력 이미지는 단일 채널 이미지(그레이스케일)을 입력해 사용합니다.
# 임곗값 형식은 임곗값을 초과한 값은 최댓값으로 변경하고 임곗값 이하의 값은 0으로 바꾸는 등의 연산을 적용합니다
# 설정 임곗값은 일반적으로 임곗값과 동일하지만, 임곗값을 대신 계산해주는 알고리즘인 Otsu나 Triangle를 사용한다면, 해당 알고리즘에서 계산해준 임곗값을 알 수 있습니다.
# 예제에서는 임곗값을 100, 최댓값을 255, 임곗값 형식을 cv2.THRESH_BINARY로 사용하였으므로, 픽셀의 값이 100을 초과하는 경우에는 255의 값으로 변경되며, 100 이하의 값은 0으로 변경됩니다.
# 수식으로 표현한다면 dst = ( src > thresh ) ? maxval : 0 으로 표현할 수 있습니다.
# Tip : 다중 채널 이미지를 입력 이미지로 사용하였을 때, 각 채널마다 이미지를 분리해 이진화 연산을 적용합니다.

cv2.imshow("binary", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 흐림 효과(Blur)는 블러링(Blurring) 또는 스무딩(Smoothing)이라 불리며, 노이즈를 줄이거나 외부 영향을 최소화하는 데 사용됩니다.
# 흐림 효과는 영상이나 이미지를 번지게 하며, 해당 픽셀의 주변 값들과 비교하고 계산해서 픽셀들의 색상을 재조정합니다.
# 단순히 이미지를 흐리게 만드는 것뿐만 아니라 노이즈를 제거해서 연산 시 계산을 빠르고 정확하게 수행하는 데 도움을 줍니다.
# 또한, 이미지의 해상도를 변경하는 경우에도 사용되는데 이미지의 크기를 변경하면 존재하지 않는 데이터를 생성하거나 존재하는 데이터를 줄여야 하므로 샘플링된 이미지를 재구성할 때 사용됩니다.

# 단순 흐림 효과 함수(cv2.blur)로 입력 이미지에 흐림 효과를 적용할 수 있습니다.
# 단순 흐림 효과는 각 픽셀에 대해 커널을 적용해 모든 픽셀의 단순 평균을 구하는 연산입니다.
# dst = cv2.blur(src, ksize, anchor, borderType)는 입력 이미지(src)를 커널 크기(ksize), 고정점(anchor), 테두리 외삽법(borderType)으로 흐림 효과를 적용한 결과 이미지(dst)를 반환합니다.
dst = cv2.blur(src, (9,9), anchor=(-1, -1), borderType = cv2.BORDER_DEFAULT)
# dst2 = cv2.blur(src, (9,9), anchor=(-1, -1), borderType = cv2.BORDER_ISOLATED)

cv2.imshow("blur", dst)
# cv2.imshow("isolated", dst2)
cv2.waitKey()
cv2.destroyAllWindows()