import cv2


def display_and_save_images(image_path):
    original_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if original_image is None:
        print("Error: Unable to read the image.")
        return

    cv2.imshow("Unchanged Image", original_image)

    color_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    cv2.imshow("Color Image", color_image)

    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)

    key = cv2.waitKey(0)

    if key == ord('a'):
        cv2.imwrite("unchanged_image.png", original_image)
        cv2.imwrite("color_image.png", cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR))
        cv2.imwrite("gray_image.png", gray_image)
        print("Images saved successfully.")

    cv2.destroyAllWindows()


image_path = "/Users/manvithchandra/Desktop/PCV/LAB 1/INLAB 1/IMG.png"

display_and_save_images(image_path)