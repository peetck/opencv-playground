import cv2
import numpy as np

def image_pyramids_example():
    """ image_pyramids_example function """
    img = cv2.imread("chicky_512.png")

    layer = img.copy()
    #gaussian_pyramid = [layer]
    for i in range(5):
        cv2.imshow(str(i + 1), layer)
        layer = cv2.pyrDown(layer)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_pyramids_example()
