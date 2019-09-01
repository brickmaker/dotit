import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

if len(sys.argv) < 3:
    print("Usage: python3 dotit.py dot-size image-path")
    exit(-1)
print(sys.argv)
dot_size = int(sys.argv[1])
image = cv2.imread(sys.argv[2])
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

dot_image = np.zeros(gray_image.shape, np.uint8)
dot_image[:] = 255

for x in range(0, dot_image.shape[0] - dot_size, dot_size):
    for y in range(0, dot_image.shape[1] - dot_size, dot_size):
        gray_val = cv2.mean(gray_image[x:x+dot_size, y:y+dot_size])[0]
        radius = (255 - gray_val) / 255 * dot_size / 2
        cv2.circle(dot_image, (int(y + dot_size / 2), int(x + dot_size / 2)), int(radius), 0, -1)

cv2.imwrite('./dotted_image.png', dot_image)
