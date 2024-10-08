# 기하학적 변환(Geometric Transform)이란 이미지를 인위적으로 확대, 축소, 위치 변경, 회전, 왜곡하는 등 이미지의 형태를 변환하는 것을 의미합니다.
# 이미지를 구성하는 픽셀 좌푯값의 위치를 재배치하는 과정으로 볼 수 있습니다.
# 기하학적 변환은 크게 아핀 변환(Affine Transformation)과 원근 변환(Perspective Transformation)이 있다.
# 아핀 변환은 2×3 행렬을 사용하며 행렬 곱셈에 벡터 합을 활용해 표현할 수 있는 변환을 의미합니다.
# 원근 변환은 3×3 행렬을 사용하며, 호모그래피(Homography)로 모델링할 수 있는 변환을 의미합니다.
# Tip : 아핀 변환은 정확하게는 3×3 행렬 형태를 갖습니다. 행렬의 세 번째 행이 [0, 1, 1] 값을 가져 OpenCV에서는 표현하지 않습니다.

import cv2
import numpy as np

src = cv2.imread("Study_Py_OpenCV/src/harvest.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

# 원근 변환(Perspective Transformation)은 네 점을 사용하여 픽셀을 재매핑합니다.
# 그러므로, 매핑에 사용할 변환 전 원본 이미지의 픽셀 좌표(srcPoint)과 변환 후 결과 이미지의 픽셀 좌표(dstPoint)를 선언합니다.
# 변환 전 원본 이미지의 픽셀 좌표가 변환 후 결과 이미지의 픽셀로 매핑되어 이미지가 변형됩니다.
# 예제의 좌표의 순서는 좌상, 우상, 우하, 좌하 순서입니다. numpy.array 형태로 선언하며, 좌표의 순서는 원본 순서와 결과 순서가 동일해야합니다.
# 만약, 순서가 동일하지 않다면 비틀린(twist) 형태로 이미지가 표현될 수 있습니다.
# Tip : 픽셀 좌표 배열은 정밀도(dtype)를 float32 형식으로 선언해야 사용할 수 있습니다.
srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

# 원근 맵 행렬 생성 함수(cv2.GetPerspectiveTransform)로 매핑 좌표에 대한 원근 맵 행렬을 생성할 수 있습니다.
# M = cv2.GetPerspectiveTransform(src, dst)는 변환 전 네 개의 픽셀 좌표(src)과 변환 후 네 개의 픽셀 좌표(dst)을 기반으로 원근 맵 행렬(M)을 생성합니다.
# 만약, 예제와 같은 데이터로 원근 맵 행렬을 생성한다면 다음과 같은 행렬이 생성됩니다.
# [[-2.88000000e+01 -9.60000000e+00  1.05600000e+04]
#  [-4.44089210e-15 -2.15400000e+01  4.30800000e+03]
#  [-1.77809156e-17 -2.00000000e-02  1.00000000e+00]]
matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
# 원근 변환 함수(cv2.warpPerspective)로 원근 맵 행렬에 대한 기하학적 변환을 수행할 수 있습니다.
# dst = cv2.warpPerspective(src, M, dsize, dst, flags, borderMode, borderValue)는 입력 이미지(src)에 원근 맵 행렬(M)을 적용하고, 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)를 반환합니다.
# 이미지를 변형하기 때문에 보간법(flags)과 테두리 외삽법(borderMode), 테두리 색상(borderValue)을 적용할 수 있습니다
dst = cv2.warpPerspective(src, matrix, (width, height))

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()