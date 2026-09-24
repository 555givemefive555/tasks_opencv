import cv2
import numpy as np

def create_malevich_square(output_path='malevich.jpg'):

    canvas = np.full((512, 512), 255, dtype="uint8")
    canvas[192:320, 192:320] = 0
    cv2.imwrite(output_path, canvas)

output_path = '/home/nikita/Desktop/tasks_opencv/task5/result.jpg'
create_malevich_square(output_path)