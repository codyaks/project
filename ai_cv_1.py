import cv2

image=cv2.imread("Sunflower.jpg")

cv2.namedWindow("image1",cv2.WINDOW_NORMAL)
cv2.resizeWindow("image1",700,500)
cv2.imshow("image1",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"image dimensions:{image.shape}")