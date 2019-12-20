import cv2
import numpy as np
from matplotlib import pyplot as plot

"""
The Canny edge detector is an edge detection operator that uses a
multi-stage algorithm to detect a wide range of edges in images.
"""

"""
The Process of Canny edge detection algorithm can be broken down to 5 different steps:
    1. Apply Gaussian filter to smooth the image in order to remove the noise.
    2. Find the intensity gradients of the image.
    3. Apply non-maximum suppression to get rid of spurious response to edge detection.
    4. Apply double threshold to determine potential edges.
    5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.
"""

def show(value):
    """ show function """
    print(value) # display current trackbar value

def canny_edge_detection_example():
    """ canny_edge_detection_example function """
    img = cv2.imread("penguin.jpg", 0) # read penguin.jpg

    cv2.namedWindow("Trackbar") # namedWindow "Trackbar"

    cv2.createTrackbar("threshold1", "Trackbar", 0, 255, show) # create threshold 1 trackbar
    cv2.createTrackbar("threshold2", "Trackbar", 0, 255, show) # create threshold 2 trackbar

    cv2.setTrackbarPos("threshold1", "Trackbar", 100) # set default value (threshold 1 trackbar)
    cv2.setTrackbarPos("threshold2", "Trackbar", 200) # set default value (threshold 2 trackbar)

    cv2.imshow("Image", img) # display original Image

    while True:
        # canny edge img with threshold 1 & 2 (from trackbar)
        canny = cv2.Canny(img, cv2.getTrackbarPos("threshold1", "Trackbar"), cv2.getTrackbarPos("threshold2", "Trackbar"))

        cv2.imshow("Trackbar", canny) # display canny

        if cv2.waitKey(1) & 0xFF == ord("q"): # if press "q"
            break # break the loop

    cv2.destroyAllWindows()
canny_edge_detection_example()
