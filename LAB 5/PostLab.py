import cv2

def rotate_image(image, angle):
    """
    Rotate the image by a given angle.
    """
    height, width = image.shape[:2]
    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

if __name__ == "__main__":
    # Read the image
    image = cv2.imread('img.png')

    # Initialize angle
    angle = 0

    while True:
        # Rotate the image
        rotated = rotate_image(image, angle)
        # Display the rotated image
        cv2.imshow('Rotated Image', rotated)
        # Wait for 30 milliseconds and check for key press
        key = cv2.waitKey(30)
        # If 'q' is pressed, break the loop
        if key == ord('q'):
            break
        # Increment the angle for the next rotation
        angle += 1
        # If angle reaches 360, reset it
        if angle == 360:
            angle = 0

    # Close all OpenCV windows
    cv2.destroyAllWindows()
