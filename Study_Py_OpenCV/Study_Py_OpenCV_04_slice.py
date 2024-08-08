import cv2

# 자르기(slice)
src = cv2.imread("Study_Py_OpenCV/src/pawns.jpg", cv2.IMREAD_COLOR)
# OpenCV의 이미지는 numpy 배열 형식과 동일
# src[높이(행), 너비(열)]로 관심 영역 설정
# 리스트나 배열의 특정 영역을 자르는 방식과 동일
# 이미지를 자르거나 복사할 때, dst = src의 형태를 사용할 경우, 얕은 복사(shallow copy)가 되어 원본도 영향을 받음.
# 따라서, *.copy()를 이용해 깊은 복사(deep copy) 진행
dst = src[100:600, 200:700].copy()

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

dst = src.copy()
# 관심영역 설정. tmp공간?
roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()