import cv2
import numpy as np
import os
from pathlib import Path


def remove_background(image_path, threshold=127):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    foreground_mask = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(img, img, mask=foreground_mask)
    return foreground


def process_dataset(input_dir, output_dir, threshold=127):
    # Create the output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Iterate through all JPEG images in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):  # Check if the file is a JPEG
            image_path = os.path.join(input_dir, filename)
            foreground = remove_background(image_path, threshold=threshold)

            # Save the processed image to the output directory
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, foreground)
            print(f"Processed {filename}")


# Example usage
input_dir = '/Users/manvithchandra/Downloads/Original Data/train/Black Rot'
output_dir = '/Users/manvithchandra/Downloads/untitled folder 4'
process_dataset(input_dir, output_dir)

# Example usage
