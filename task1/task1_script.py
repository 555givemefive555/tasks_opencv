import cv2
import os

def extract_frames_opencv(video_path, output_folder):

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Не удалось открыть видео")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_interval = int(round(fps))
    saved = 1
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_interval == 0:
            filename = os.path.join(output_folder, f"frame_{saved}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1

        frame_idx += 1

    cap.release()
    
    return

input_video_path = '/home/nikita/Desktop/tasks_opencv/task1/audi.mp4'
output_dir_path = '/home/nikita/Desktop/tasks_opencv/task1/output_frames'

extract_frames_opencv(input_video_path, output_dir_path)