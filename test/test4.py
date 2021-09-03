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

cnt = cv2.findContours(fli, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnt[1]
if len(cnts)>0:
    c = max(cnts, key = cv2.contourArea)
    ((x,y), r) = cv2.minEnclosingCircle(c)
    cv2.circle(src, (int(x), int(y)), int(r),(0,0,255), 2)#(coordinates, radius, colour, thickness)

cv2.imshow('detection', src)    
key = cv2.waitKey()
