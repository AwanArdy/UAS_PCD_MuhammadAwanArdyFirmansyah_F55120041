import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('basarnas.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

light_orange=(1,190,200)
dark_orange =(18, 255, 255)

mask = cv2.inRange(hsv_img, light_orange, dark_orange)
result=cv2.bitwise_and(img, img, mask=mask)

plt.subplot(1,4,1)
plt.imshow(img)
plt.title('Citra Asli')
plt.subplot(1,4,2)
plt.imshow(hsv_img)
plt.title('Citra Negatif')
plt.subplot(1,4,3)
plt.imshow(mask)
plt.title('Citra HUE')
plt.subplot(1,4,4)
plt.imshow(result)
plt.title('Citra Hasil')
plt.show()