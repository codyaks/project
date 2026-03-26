import matplotlib.pyplot as plt
import cv2

image=cv2.imread('Sunflower.jpg')
crop_img=image[400:550,400:550]
croprgb=cv2.cvtColor(crop_img,cv2.COLOR_BGR2RGB)
plt.imshow(croprgb)
plt.title("cropped region")
plt.show()

