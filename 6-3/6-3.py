import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the TIFF image
img = cv2.imread('Fig0635.tif', cv2.IMREAD_UNCHANGED)

img_rgb = cv2.imread('Fig0635.tif', cv2.IMREAD_COLOR)


# Separate the RGB channels
r, g, b = cv2.split(img_rgb)

# Apply histogram equalization to the R, G, and B channels
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)

# Merge the equalized R, G, and B channels into a single RGB image
img_eq = cv2.merge((r_eq, g_eq, b_eq))

# Convert the equalized image back to TIFF format
cv2.imwrite('output.tif', img_eq)

# Plot the original image and its histogram
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 1].hist(img.ravel(), 256, [0, 256])
axs[0, 1].set_title('Original Histogram')
axs[0, 1].set_xlim([0, 256])


# Plot the equalized image and its histogram
axs[1, 0].imshow(img_eq, cmap='gray')
axs[1, 0].set_title('Equalized Image')
axs[1, 1].hist(img_eq.ravel(), 256, [0, 256])
axs[1, 1].set_title('Equalized Histogram')
axs[1, 1].set_xlim([0, 256])


# Show the plots
plt.show()