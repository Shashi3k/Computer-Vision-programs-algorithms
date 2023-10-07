import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'image.jpg'
image=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Could not open or find the image at '{image_path}")

else:
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    plt.figure(figsize=(10,5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian (2nd Order Derivative)')
    plt.axis('off')

    plt.show()