# pip install opencv-python
import cv2

def capture_image(camera_index=0, output_filename='captured_image.jpg'):
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_filename, frame)
        print(f"Image captured and saved as {output_filename}")
    else:
        print("Failed to capture image")
    cap.release()

if __name__ == "__main__":
    capture_image()