import cv2
import numpy as np


capture = cv2.VideoCapture(0) # 0 - numer kamery jak masz wiecej niz jedna to moze byc 1, 2, 3, ... n

while True:
    retur, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if(cv2.waitKey(1) == ord('q')):
        break

capture.release()
cv2.destroyAllWindows() 