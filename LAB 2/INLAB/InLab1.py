import cv2
import numpy as np

image_path = "img.png"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Image not loaded.")
    exit()

ycrcb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2YCrCb)
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
edge_map = np.uint8(np.absolute(laplacian))

heatmap = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)
spectral_map = cv2.applyColorMap(edge_map, cv2.COLORMAP_RAINBOW)

cv2.imshow("Original Image", original_image)
cv2.imshow("YCrCb Image", ycrcb_image)
cv2.imshow("HSV Image", hsv_image)
cv2.imshow("LAB Image", lab_image)
cv2.imshow("Edge Map", edge_map)
cv2.imshow("Heat Map", heatmap)
cv2.imshow("Spectral Map", spectral_map)

cv2.waitKey(0)
cv2.destroyAllWindows()
