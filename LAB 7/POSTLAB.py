import cv2
import matplotlib.pyplot as plt

# Read the original image
original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)


original=cv2.imread('',cv2.IMREAD_UNCHANGED)


x=cv2.cvtColor('',cv2.COLOR_BGR2RGB)
y=cv2.cvtColor('',cv2.COLOR_BGR2GRAY)


# Apply histogram equalization using equalizeHist
equalized_image = cv2.equalizeHist(original_image)

# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(original_image)

# Plot the histograms
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.hist(original_image.ravel(), 256, [0, 256], color='r')
plt.title('Original Image Histogram')

plt.subplot(1, 3, 2)
plt.hist(equalized_image.ravel(), 256, [0, 256], color='g')
plt.title('Histogram Equalized Image Histogram')

plt.subplot(1, 3, 3)
plt.hist(clahe_image.ravel(), 256, [0, 256], color='b')
plt.title('CLAHE Image Histogram')

plt.tight_layout()
plt.show()
