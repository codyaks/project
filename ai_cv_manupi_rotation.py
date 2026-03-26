import matplotlib.pyplot as plt
import cv2
import numpy as np
image=cv2.imread('Sunflower.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
(h,w)=image.shape[:2]
center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,46,1.0)
rotated=cv2.warpAffine(image,m,(w,h))
rotate_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotate_rgb)
plt.title("rotated image")
plt.show()

brightmatrix= np.ones(image.shape, dtype="uint8")*50
brighter=cv2.add(image,brightmatrix)
brighter_rgb=cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("brighter image")
plt.show()
