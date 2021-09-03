import cv2
src = cv2.imread('test1.jpeg')
#hue 30 to 60
#sat 50 to 255
#val 50 to 255
lr =(30, 50, 50) #lower range
ur = (60, 255, 255) #upper range
hsv= cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
filtered_img = cv2.inRange(hsv,lr,ur)

cv2.imshow('original', src)

fli = cv2.erode(filtered_img, None, iterations = 2)
fli = cv2.dilate(fli, None, iterations = 3)
cv2.imshow('morph', fli)

img_1 = cv2.bitwise_or(src,src, mask = fli)
cv2.imshow('and gate',img_1)
key = cv2.waitKey()
