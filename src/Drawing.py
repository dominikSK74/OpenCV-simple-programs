import cv2
import numpy as np


capture = cv2.VideoCapture(0) # 0 - numer kamery jak masz wiecej niz jedna to moze byc 1, 2, 3, ... n

while True:
    retur, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    image = cv2.line(frame, (0, 0), (width, height), (255,0,0), 5)
    image = cv2.rectangle(image, (100, 100), (200, 200), (0,255,0), 5)
    image = cv2.circle(image, (300, 300), 60, (0,0,255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'Hello world', (200, height-10), font, 2, (255,255,255), 3, cv2.LINE_AA)
    #                   img     text      position(x,y) center   font  size  color       thickness   line type

    cv2.imshow('frame', image)

    if(cv2.waitKey(1) == ord('q')):
        break

capture.release()
cv2.destroyAllWindows() 