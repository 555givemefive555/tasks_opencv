import subprocess

def imagemagick_convolve(input_img, output_img, kernel_str):
    cmd = ['magick', input_img, '-morphology', 'Convolve', kernel_str, output_img]
    subprocess.run(cmd, check=True)


input_path = '/home/nikita/Desktop/tasks_opencv/task3/frame_22.jpg'
output_path = '/home/nikita/Desktop/tasks_opencv/task3/output.jpg'

imagemagick_convolve(input_path, output_path, "1 2 1 2 4 2 1 2 1")