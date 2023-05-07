import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Fig0631(a).tif', cv.IMREAD_UNCHANGED)
assert img is not None, "file could not be read, check with os.path.exists()"
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

cv.imwrite('output.tif', img)

# Plot the original image and its histogram
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 1].imshow(gray, cmap='gray')
axs[0, 1].set_title('Grayscale')

# Plot the equalized image and its histogram
axs[1, 0].imshow(thresh, cmap='gray')
axs[1, 0].set_title('Threshold Image')

# Show the plots
plt.show()