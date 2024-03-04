import cv2
from matplotlib import pyplot as plt

def count_edges(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 50)
    num_edges = cv2.countNonZero(edges)

    plt.subplot(121), plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])
    plt.show()

    return num_edges

image_path = 'img.png'
edges_count = count_edges(image_path)
print(f'Total number of edges: {edges_count}')
