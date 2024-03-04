import cv2

def resize_certificate(image_path):
    certificate_image = cv2.imread(image_path)
    resized_image1 = cv2.resize(certificate_image, (450, 550))

    aspect_ratio = certificate_image.shape[1] / certificate_image.shape[0]
    new_width = int(450 * aspect_ratio)
    resized_image2 = cv2.resize(certificate_image, (new_width, 450))

    scale_percent = 50
    width = int(certificate_image.shape[1] * scale_percent / 100)
    height = int(certificate_image.shape[0] * scale_percent / 100)
    resized_image3 = cv2.resize(certificate_image, (width, height))

    cv2.imshow('Original Certificate', certificate_image)
    cv2.imshow('Resized to 450x550', resized_image1)
    cv2.imshow('Resized Height to 450', resized_image2)
    cv2.imshow('Downscaled (50%)', resized_image3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'certificate.jpg'

    resize_certificate(image_path)
