import cv2
import datetime
import numpy as np

def capture_and_display_video():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open the camera.")
        return

    cv2.namedWindow('Live Video', cv2.WINDOW_NORMAL)

    zoom_factor = 1.0
    rotation_angle = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to read frame.")
            break

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        zoomed_frame = cv2.resize(frame, None, fx=zoom_factor, fy=zoom_factor)
        rotation_matrix = cv2.getRotationMatrix2D((zoomed_frame.shape[1] / 2, zoomed_frame.shape[0] / 2), rotation_angle, 1)
        rotated_frame = cv2.warpAffine(zoomed_frame, rotation_matrix, (zoomed_frame.shape[1], zoomed_frame.shape[0]))

        cv2.putText(rotated_frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Live Video', rotated_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('i'):  # Zoom in
            zoom_factor += 0.1
        elif key == ord('o'):  # Zoom out
            zoom_factor = max(0.1, zoom_factor - 0.1)
        elif key == ord('r'):  # Rotate clockwise
            rotation_angle = (rotation_angle + 1) % 360
        elif key == ord('l'):  # Rotate counterclockwise
            rotation_angle = (rotation_angle - 1) % 360

    cap.release()
    cv2.destroyAllWindows()

capture_and_display_video()
