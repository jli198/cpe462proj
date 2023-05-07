import cv2

img_rgb = cv2.imread('Fig0630(01).tif', cv2.IMREAD_COLOR)

r, g, b = cv2.split(img_rgb)

R1 = r[129:256]

print(R1)