import cv2

def test_webcam():
    for i in range(5):  # Try the first 5 indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Successfully opened webcam at index {i}")
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to read frame.")
                    break
                cv2.imshow('Webcam Test', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            return
        else:
            print(f"Error: Could not open webcam at index {i}")
    print("Error: Could not open any webcam.")

if __name__ == "__main__":
    test_webcam()
