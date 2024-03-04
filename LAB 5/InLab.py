import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def apply_thresholding(method):
    global original_image_label

    # Read the image
    image_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.png")])
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply the selected thresholding method
    if method == "BINARY":
        _, result_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    elif method == "BINARY_INV":
        _, result_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    elif method == "TOZERO":
        _, result_image = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
    elif method == "TOZERO_INV":
        _, result_image = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
    elif method == "TRUNC":
        _, result_image = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
    elif method == "MEAN_C":
        result_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    elif method == "GAUSSIAN_C":
        result_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Display the result in a new window
    result_window = tk.Toplevel(root)
    result_window.title("Result Image")

    # Convert result image to RGB for displaying with PIL
    result_image_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    result_image_pil = ImageTk.PhotoImage(Image.fromarray(result_image_rgb))

    result_image_label = tk.Label(result_window, image=result_image_pil)
    result_image_label.image = result_image_pil
    result_image_label.pack()

# Create the main window
root = tk.Tk()
root.title("Image Thresholding GUI")

# Create buttons for different thresholding methods
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

thresholding_methods = ["BINARY", "BINARY_INV", "TOZERO", "TOZERO_INV", "TRUNC", "MEAN_C", "GAUSSIAN_C"]

for method in thresholding_methods:
    button = tk.Button(buttons_frame, text=method, command=lambda m=method: apply_thresholding(m))
    button.pack(side=tk.LEFT, padx=5)

# Label for displaying the original image
original_image_label = tk.Label(root, text="Original Image will be displayed here")
original_image_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()