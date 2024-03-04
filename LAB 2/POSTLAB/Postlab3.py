import cv2
import numpy as np
import matplotlib.pyplot as plt

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

mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

result_image = cv2.addWeighted(original_image, 0.7, mask_colored, 0.3, 0)

def plot_histogram(image, title):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color='b')
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

plt.figure(figsize=(15, 5))

plt.subplot(131)
plot_histogram(original_image, 'Original Image Histogram')

plt.subplot(132)
plot_histogram(mask, 'Mask Histogram')

plt.subplot(133)
plot_histogram(result_image, 'Result Image Histogram')

plt.tight_layout()
plt.show()
