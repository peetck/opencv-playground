import cv2
import numpy as np

"""
Pyramid, or pyramid representation, is a type of multi-scale signal representation
in which a signal or an image is subject to repeated smoothing and subsampling.
"""

def image_pyramids_example():
    """ image_pyramids_example function """
    img = cv2.imread("lena-1.jpg") # read lena-1.jpg
    cv2.imshow("Original Image", img) # display original image

    layer = img.copy() # copy img
    gaussian_pyramid = [layer] # create gaussian pyramid list

    for i in range(6):
        layer = cv2.pyrDown(layer) # pyramid down current layer
        gaussian_pyramid.append(layer) # append it to gaussian pyramid list
        cv2.imshow("GP " + str(i), layer) # display after pyramid down current layer

    layer = gaussian_pyramid[5] # set layer to last index of gaussian pyramid (upper level of gaussian pyramid)

    # A level in Laplacian pyramid is formed by the difference between that level in Gaussian Pyramid and
    # expanded version of its upper level in Gaussian Pyramid

    for i in range(4, -1, -1):
        gaussian_extended = cv2.pyrUp(gaussian_pyramid[i + 1]) # pyramid up current level
        laplacian = cv2.subtract(gaussian_pyramid[i], gaussian_extended) #  difference between current level and upper level
        cv2.imshow("LP " + str(i), laplacian) # display

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_pyramids_example()
