import cv2

image_path='image.jpg'
image=cv2.imread(image_path)

if image is None:
    print(f"Could not open or find the image at '{image_path}")
else:
    width=2000
    height=2000
    ksize=(5,5)
    resized_image = cv2.resize(image, (width, height))
    blurred_image = cv2.GaussianBlur(resized_image,ksize,0)

    cv2.imshow('Original Image',resized_image)
    cv2.imshow('Smoothed Image',blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()