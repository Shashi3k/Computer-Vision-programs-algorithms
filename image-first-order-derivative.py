import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'image.jpg'
image=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Could not open or find the image at '{image_path}")

else:
    sobel_x = cv2.Sobel(image,cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image,cv2.CV_64F, 1, 0, ksize=3)
    
    plt.figure(figsize=(10, 5))

    plt.subplot(1,3,1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(sobel_x, cmap='gray')
    plt.title('Sobel X (1st Order Derivative)')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(sobel_y, cmap='gray')
    plt.title('Sobel Y (1st Order Derivative)')
    plt.axis('off')

    plt.show()