import cv2
import numpy as np
from matplotlib import pyplot as plot

def thresholding_example(): # Thresholding is the simplest method of segmenting image from a grayscale image.
    """ thresholding_example function """
    img = cv2.imread("threshold.jpg") # read threshold.jpg

    _, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) # pixels more than 120 will be white
    _, th2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) # invert of th1
    _, th3 = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC) # pixels more than 128 less than 255 will be 128
    _, th4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) # pixels less than 120 will be 0 (black)
    _, th5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV) # invert of th4

    titles = ["Original Image", "BINARY", "BINARY INV", "TRUNC", "TOZERO", "TOZERO INV"]
    images = [img, th1, th2, th3, th4, th5]

    for i in range(len(titles)):
        plot.subplot(2, 3, i + 1)
        plot.title(titles[i])
        plot.xticks([])
        plot.yticks([])
        plot.imshow(images[i])

    plot.show()
thresholding_example()
