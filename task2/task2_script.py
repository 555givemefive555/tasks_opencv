import cv2
import imageio
import os
import re

def create_gif_from_frames(folder, output_gif):
    files = os.listdir(folder)
    
    def extract_number(filename):
        match = re.search(r'(\d+)', filename)
        return int(match.group(1)) if match else 0

    files.sort(key=extract_number)
    files = files[:3]
    print(files)
    frames_rgb = []
    for f in files:
        img_bgr = cv2.imread(os.path.join(folder, f))
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        frames_rgb.append(img_rgb)

    imageio.mimsave(output_gif, frames_rgb, duration=0.1, loop=0)
    
    return

input_dir = '/home/nikita/Desktop/tasks_opencv/task1/output_frames'
output_path = '/home/nikita/Desktop/tasks_opencv/task2/result.gif'
create_gif_from_frames(input_dir, output_path)