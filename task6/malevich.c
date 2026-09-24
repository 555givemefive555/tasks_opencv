#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {

    Mat canvas(512, 512, CV_8UC1, Scalar(255));

    Rect roi(192, 192, 128, 128);
    canvas(roi).setTo(Scalar(0));

    string output_path = "/home/nikita/Desktop/tasks_opencv/task6/result_c.jpg";
    imwrite(output_path, canvas);
    return 0;
}
