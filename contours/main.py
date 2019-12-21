import cv2
import numpy as np

def contours_example():
    """ contours_example function """
    img = cv2.imread("img.jpg") # read img.jpg
    #img = cv2.imread("logo.png") # read logo.png

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    _, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY) # threshold (170, 255) pixels more than 170 will be white

    # find contours
    # (ct is a python list of all the contours in the image. Each individual contour is a Numpy array of (x, y) of boundary points of the object.)
    ct, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    print(str(len(ct))) # print number of contours found on image.

    result = img.copy() # copy img

    cv2.drawContours(result, ct, -1, (255, 0, 255), 2) # draw contours (-1 mean all of contours) on result with color (BGR) (255, 0, 255) thickness 2

    cv2.imshow("Image", img)
    cv2.imshow("Threshold", thresh)
    cv2.imshow("Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
contours_example()
