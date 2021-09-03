import cv2
import numpy as np

m = cv2.imread('test1.jpeg')

m = cv2.cvtColor(m, cv2.COLOR_HSV2BGR)

h, w, bpp = np.shape(m)

for i in range(0, h):
	for j in range(0, w):
		m[i][j][1] == 0
		m[i][j][0] == 0

cv2.imshow('matrix', m)
cv2.waitKey()
