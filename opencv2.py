import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#1 make a image empty
img = np.zeros((512, 521, 3), np.uint8)

#2 draw a line
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv.circle(img, (256, 256), 60, (0, 0, 255), -1)

cv.rectangle(img, (100, 100), (400, 400), (0,255,0),5)

cv.putText(img, "hello", (100,150) ,cv.FONT_HERSHEY_COMPLEX,5,(255,255,255),3)
#3 display
plt.imshow(img[:, :, ::-1])
plt.show()

