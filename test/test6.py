import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(2)

while True:
    (ret, frame) = cam.read()
    if ret != 0:
        cv2.imshow('webcam', frame)

    key = cv2.waitKey(1) & 0xFF #& 0xFF converts ascii to char
    if key == ord('q'):
        break
