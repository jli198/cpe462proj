import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Fig0630(01).tif', cv.IMREAD_UNCHANGED)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

hsv_img = cv.cvtColor(img, cv.COLOR_RGB2HSV)

light_red = (255, 204, 203)
dark_red = (200, 63, 73)

mask = cv.inRange(hsv_img, light_red, dark_red)

result = cv.bitwise_and(img, img, mask=mask)

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.show()