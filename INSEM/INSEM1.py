import cv2


def blend_images(image1_path, image2_path, output_path, alpha=0.6, beta=0.4, gamma=0):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    height, width = min(image1.shape[0], image2.shape[0]), min(image1.shape[1], image2.shape[1])
    image1 = cv2.resize(image1, (width, height))
    image2 = cv2.resize(image2, (width, height))

    blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

    cv2.imshow('Blended Image', blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image1_path = 'IMG.png'
    image2_path = 'img2.jpg'

    output_path = '/Users/manvithchandra/Desktop/PCV/INSEM/blended_image.jpg'

    alpha = 0.6
    beta = 0.4

    blend_images(image1_path, image2_path, output_path, alpha, beta)
