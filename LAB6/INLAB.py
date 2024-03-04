import cv2

# Function to denoise grayscale image
def denoise_grayscale_image(input_image_path, output_image_path):
    # Read the grayscale image
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    # Apply Gaussian Denoising
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    # Save the denoised image
    cv2.imwrite(output_image_path, denoised_image)

# Function to denoise color image
def denoise_color_image(input_image_path, output_image_path):
    # Read the color image
    image = cv2.imread(input_image_path)
    # Apply Gaussian Denoising to each channel
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    # Save the denoised image
    cv2.imwrite(output_image_path, denoised_image)

# Function to denoise video frames
def denoise_video(input_video_path, output_prefix):
    # Read the video
    cap = cv2.VideoCapture(input_video_path)
    frame_count = 0
    # Read and denoise the first 5 frames
    while frame_count < 5:
        ret, frame = cap.read()
        if ret:
            # Convert to grayscale if necessary
            if len(frame.shape) > 2:
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            else:
                frame_gray = frame
            # Apply denoising
            denoised_frame = cv2.GaussianBlur(frame_gray, (5, 5), 0)
            # Save the denoised frame
            cv2.imwrite(f'{output_prefix}_{frame_count}.jpg', denoised_frame)
            frame_count += 1
    cap.release()

# Denoise grayscale image
denoise_grayscale_image('grayscale_image.jpg', 'denoised_grayscale_image.jpg')

# Denoise color image
denoise_color_image('color_image.jpg', 'denoised_color_image.jpg')

# Denoise grayscale video frames
denoise_video('video_grayscale.mp4', 'denoised_frame_grayscale')

# Denoise color video frames
denoise_video('video_color.mp4', 'denoised_frame_color')
