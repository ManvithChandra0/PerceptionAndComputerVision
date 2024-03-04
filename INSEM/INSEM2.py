import cv2


def apply_color_filter(image, option):
    if option == 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image[:, :, 1] = 255
        image[:, :, 2] = 255

    elif option == 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image[:, :, 0] = 0
        image[:, :, 2] = 255

    elif option == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    elif option == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image[:, :, 0] = 0
        image[:, :, 1] = 0

    elif option == 5:
        image[:, :, 0] = 0
        image[:, :, 2] = 0

    elif option == 6:
        image = cv2.add(image, image)

    return image


def main():
    image_path = 'img.png'
    original_image = cv2.imread(image_path)

    if original_image is not None:
        option = int(input(
            "[1] Hue\n[2] Saturation\n[3] HSV Image\n[4] Value\n[5] Green Channel\n[6] Doubled image\nChoose an option: "))

        filtered_image = apply_color_filter(original_image, option)

        cv2.imshow("Original Image", original_image)
        cv2.imshow("Filtered Image", filtered_image)

        save_option = input("Do you want to save the filtered image? (yes/no): ")
        if save_option.lower() == 'yes':
            output_path = input("Enter the path to save the filtered image: ")
            cv2.imwrite(output_path, filtered_image)
            print("Filtered image saved successfully.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error loading the image. Please check the file path.")


if __name__ == "__main__":
    main()
