import numpy as np
import cv2
src = cv2.imread('test1.jpeg')
h, w, bpp = np.shape(src)
(b, g, r) = cv2.split(src)

for i in range(0, h):
	for j in range(0, w):
		src[i][j][0] = 255

cv2.imshow("blue", b)
cv2.imshow("red", r)
cv2.imshow("green", g)
cv2.imshow("color", src)
key = cv2.waitKey()