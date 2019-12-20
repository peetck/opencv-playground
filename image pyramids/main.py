import cv2
import numpy as np

def image_pyramids_example():
    """ image_pyramids_example function """
    img = cv2.imread("chicky_512.png")

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_pyramids_example()
