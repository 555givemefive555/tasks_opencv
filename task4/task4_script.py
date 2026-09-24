import cv2
import os

def scale_first_frame(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return

    current = frame
    for i in range(1, 4):
        h, w = current.shape[:2]
        new_size = (int(w * 0.75), int(h * 0.75))
        current = cv2.resize(current, new_size, interpolation=cv2.INTER_AREA)
        path = os.path.join(output_folder, f"scaled_{i}.jpg")
        cv2.imwrite(path, current)

    return

input_path = '/home/nikita/Desktop/tasks_opencv/task4/audi.mp4'
output_path = '/home/nikita/Desktop/tasks_opencv/task4/output'

scale_first_frame(input_path, output_path)