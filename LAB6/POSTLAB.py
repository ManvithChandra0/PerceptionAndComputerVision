import cv2
import matplotlib.pyplot as plt

# Read the original image
original_image = cv2.imread('original_image.jpg', cv2.IMREAD_GRAYSCALE)

# Read the noisy image
noisy_image = cv2.imread('noisy_image.jpg', cv2.IMREAD_GRAYSCALE)

# Read the denoised image
denoised_image = cv2.imread('denoised_image.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histograms
original_hist = cv2.calcHist([original_image], [0], None, [256], [0, 256])
noisy_hist = cv2.calcHist([noisy_image], [0], None, [256], [0, 256])
denoised_hist = cv2.calcHist([denoised_image], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(original_hist, color='black')
plt.title('Original Image Histogram')

plt.subplot(3, 1, 2)
plt.plot(noisy_hist, color='red')
plt.title('Noisy Image Histogram')

plt.subplot(3, 1, 3)
plt.plot(denoised_hist, color='blue')
plt.title('Denoised Image Histogram')

plt.tight_layout()
plt.show()
