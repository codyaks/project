import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(image, title):
    plt.figure(figsize=(8,8))
    if len(image.shape)==2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return
    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray_image, "Grayscale Image")

    print("select an opton")
    print("1. sobel edge detection")
    print("2. canny edge detection")
    print("3. laplacian edge detection")
    print("4.gaussian smoothing")
    print("5. median smoothing")
    print("6. exit")

    while True:
        choice=input("Enter your choice: (1-6)")
        if choice=="1":
            sobel_x=cv2.Sobel(gray_image, cv2.CV_64F,1,0,ksize=3)
            sobel_y=cv2.Sobel(gray_image, cv2.CV_64F,0,1,ksize=3)
            combined_sobel=cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image(combined_sobel, "Sobel Edge Detection")
        elif choice=="2":
            print("Enter lower and upper thresholds for Canny edge detection default is (100- 200):")
            lower_thresh=int(input("Lower threshold: "))
            upper_thresh=int(input("Upper threshold: "))
            edge=cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image(edge, "Canny Edge Detection")
        elif choice=="3":
            lapplacian=cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image(np.abs(lapplacian).astype(np.uint8),"Laplacian Edge Detection")
        elif choice=="4":
            print("enter kernel size for gaussian smoothing (must be an odd number default is 5):")
            kernel_size=int(input("Kernel size: odd number: "))
            blur=cv2.GaussianBlur(image,(kernel_size, kernel_size),0)
            display_image(blur, "Gaussian Smoothing")
        elif choice=="5":
            print("enter kernel size for median filtering (must be an odd number default is 5):")
            kernel_size=int(input("Kernel size: odd number: "))
            median_filtered=cv2.medianBlur(image, kernel_size)
            display_image(median_filtered, "Median Smoothing")
        elif choice=="6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
interactive_edge_detection("Sunflower.jpg")

            


