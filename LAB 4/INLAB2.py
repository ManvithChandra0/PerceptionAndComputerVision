import cv2
from matplotlib import pyplot as plt

image_path = 'img.png'
original_image = cv2.imread(image_path)

region_of_interest = cv2.selectROI("Select Region of Interest", original_image, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

selected_region = original_image[int(region_of_interest[1]):int(region_of_interest[1] + region_of_interest[3]),
                                 int(region_of_interest[0]):int(region_of_interest[0] + region_of_interest[2])]

plt.subplot(121), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(selected_region, cv2.COLOR_BGR2RGB))
plt.title('Selected Region'), plt.xticks([]), plt.yticks([])

plt.show()
