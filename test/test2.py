import cv2
src = cv2.imread('test1.jpeg')

hsv= cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', src)
cv2.imshow('hsv', hsv)
key = cv2.waitKey()
