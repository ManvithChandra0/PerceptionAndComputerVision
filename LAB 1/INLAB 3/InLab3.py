import cv2

def blend_images(image1_path, image2_path, output_path, alpha=0.6, beta=0.4, gamma=0):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    height, width = min(image1.shape[0], image2.shape[0]), min(image1.shape[1], image2.shape[1])
    image1 = cv2.resize(image1, (width, height))
    image2 = cv2.resize(image2, (width, height))

    if image1.shape[:2] != image2.shape[:2]:
        raise ValueError("Images must have the same size for blending.")

    blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

    cv2.imshow('Blended Image', blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the blended image
    cv2.imwrite(output_path, blended_image)

if __name__ == "__main__":
    image1_path = 'IMG.png'
    image2_path = 'certificate.jpg'

    output_path = '/Users/manvithchandra/Desktop/PCV/LAB 1/INLAB 3/blended_image.jpg'

    alpha = 0.6
    beta = 0.4

    blend_images(image1_path, image2_path, output_path, alpha, beta)
