import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#1 read image
img = cv.imread("/home/yhp/PycharmProjects/pythonProject/image2/imori.jpg",0)

#2 show image

# cv.imshow("img",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#3 matplotlib

# plt.imshow(img, cmap=plt.cm.gray)

# plt.imshow(img[:, ::-1])
# plt.show()

#4 imwrite save image

# cv.imwrite("gray.jpg",img)



