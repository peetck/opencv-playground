import cv2
import numpy as np

def adaptive_thresholding_example():
    """ adaptive_thresholding_example function """
    img = cv2.imread("sudoku.png", 0) # read sudoku.png

    _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # simple threshold

    # adaptive thresholding (maximum = 255, blocksize = 11, C = 2)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    cv2.imshow("Image", img) # display img
    cv2.imshow("THRESH_BINARY", th1) # display th1
    cv2.imshow("ADAPTIVE_THRESH_MEAN_C (THRESH_BINARY)", th2) # display th2
    cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C (THRESH_BINARY)", th3) # display th3

    cv2.waitKey(0)
    cv2.destroyAllWindows()
adaptive_thresholding_example()
