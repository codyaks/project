import cv2
import numpy as np

def apply_color_filter(image,filter_type):
    filtered_image=image.copy()

    if filter_type=="red_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,0]=0
    elif filter_type=="blue_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0
    elif filter_type=="green_tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,2]=0
    elif filter_type=="increase_red":
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50)
    elif filter_type=="decrease_blue":
        filtered_image[:,:,2]=cv2.subtract(filtered_image[:,:,0],50)
    elif filter_type=="sobel":
        sobel_x=cv2.Sobel(image, cv2.CV_64F,1,0,ksize=3)
        sobel_y=cv2.Sobel(image, cv2.CV_64F,0,1,ksize=3)
        filtered_image=cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
    elif filter_type=="canny":
        filtered_image=cv2.Canny(image, 100, 200)
    elif filter_type=="laplacian":
        laplacian=cv2.Laplacian(image, cv2.CV_64F)
        filtered_image=np.abs(laplacian).astype(np.uint8)
    elif filter_type=="gaussian":
        filtered_image=cv2.GaussianBlur(image,(15, 15),0)
    elif filter_type=="median":
        filtered_image=cv2.medianBlur(image, 15)
    return filtered_image
image_path='Sunflower.jpg'
image=cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
else:
    filter_type="original"
    print("Select a filter to apply:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red")
    print("d - Decrease Blue")
    print("1. sobel edge detection")
    print("2. canny edge detection")
    print("3. laplacian edge detection")
    print("4.gaussian smoothing")
    print("5. median smoothing")
    print("q - quit")

    while True:
        filtered_image=apply_color_filter(image,filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key=cv2.waitKey(0) & 0xFF

        if key==ord('r'):
            filter_type="red_tint"
        elif key==ord('b'):
            filter_type="blue_tint"
        elif key==ord('g'):
            filter_type="green_tint"
        elif key==ord('i'):
            filter_type="increase_red"
        elif key==ord('d'):
            filter_type="decrease_blue"
        elif key==ord('1'):
            filter_type="sobel"
        elif key==ord('2'):
            filter_type="canny"
        elif key==ord('3'):
            filter_type="laplacian"
        elif key==ord('4'):
            filter_type="gaussian"
        elif key==ord('5'):
            filter_type="median"
        elif key==ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid input. Please use r, b, g, i, d or q.")

cv2.destroyAllWindows()