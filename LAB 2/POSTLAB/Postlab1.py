import cv2
import numpy as np

image_path = "img.png"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Image not loaded.")
    exit()

hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

lower_bound = np.array([30, 50, 50])
upper_bound = np.array([70, 255, 255])

mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

masked_image = cv2.bitwise_and(original_image, original_image, mask=mask)

cv2.imshow("Original Image", original_image)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("/LAB 2/POSTLAB/mask.jpg", mask)
