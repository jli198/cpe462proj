import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img_rgb = cv2.imread('Fig0631(a).tif', cv2.IMREAD_COLOR)

r, g, b = cv2.split(img_rgb)
print(r)

R1 = r[129:256, 86:170]
print(R1)
R1_ave = np.mean(np.mean(R1))
print(R1_ave)
[M, N] = np.shape(R1)
sd = 0.0
for i in range(M):
  for j in range(N):
    sd = sd + (R1[i, j] - R1_ave) * (R1[i, j] - R1_ave)

R1_d = math.sqrt(sd/(M*N))

img_rgb = np.array(img_rgb)

R2 = np.zeros(img_rgb.shape, img_rgb.shape)
index = np.argwhere((R1 > R1_ave - 1.25 * R1_d) & (r < R1_ave + 1.25*R1_d))

cv2.imwrite('test.jpg', R2)