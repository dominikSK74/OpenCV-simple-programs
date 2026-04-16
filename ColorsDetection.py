import cv2
import numpy as np


capture = cv2.VideoCapture(0) # 0 - numer kamery jak masz wiecej niz jedna to moze byc 1, 2, 3, ... n

while True:
    retur, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if(cv2.waitKey(1) == ord('q')):
        break

capture.release()
cv2.destroyAllWindows() 