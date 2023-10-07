import cv2
import matplotlib.pyplot as plt

image_path='image.jpg'
image = cv2.imread(image_path,0)

if image is None:
    print(f"Could not open or find the image at '{image_path}")

else:
    histogram = cv2.calcHist([image],[0],None,[256],[0,256])

    plt.figure(figsize=(8,6))
    plt.title('Image Histogram')
    plt.xlabel('Image Histogram')
    plt.ylabel('Frequency')
    plt.plot(histogram, color='black')
    plt.xlim([0,256])
    plt.grid(True)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()