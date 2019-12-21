import cv2
import numpy as np
from matplotlib import pyplot as plot

def detect_simple_geometric_shapes_example():
    """ detect_simple_geometric_shapes_example function """

    img = cv2.imread("shapes_and_colors.jpg") # read shapes_and_colors.jpg

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert img to grayscale

    blur = cv2.GaussianBlur(gray, (5, 5), 0) # gaussian blurring for eliminating the noises

    _, thresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY) # threshold the img after blurring

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # find contours

    result = img.copy() # copy img

    for contour in contours:

        # find number of corners of contour (True mean the contour is closed)
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)

        # draw contour to result with pink color thickness 2
        cv2.drawContours(result, [contour], -1, (255, 0, 255), 2)

        x = approx.ravel()[0] # get the x pos
        y = approx.ravel()[1] # get the y pos

        if len(approx) == 3: # if corners of contour == 3

            # put msg Triangle to result img
            cv2.putText(result, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, .3, (255, 255, 255), 1, cv2.LINE_AA)

        elif len(approx) == 4: # if corners of contour == 4

            x, y, w, h = cv2.boundingRect(contour) # get contour (x, y) position and width & height

            if 1.05 >= float(w) / float(h) >= 0.95: # check if it's square or not

                # put msg Square to result img
                cv2.putText(result, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, .3, (255, 255, 255), 1, cv2.LINE_AA)

            else:

                # put msg Rectangle to result img
                cv2.putText(result, "Rectangle", (x, y + (h // 2)), cv2.FONT_HERSHEY_SIMPLEX, .3, (255, 255, 255), 1, cv2.LINE_AA)

        elif len(approx) == 5: # if corners of contour == 5

            # put msg Pentagon to result img
            cv2.putText(result, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, .3, (255, 255, 255), 1, cv2.LINE_AA)

        else:
            # put msg Circle to result img
            cv2.putText(result, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, .3, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Image", img) # display original img
    cv2.imshow("GaussianBlur", blur) # display img after gaussianblur
    cv2.imshow("threshold", thresh) # display img after threshold
    cv2.imshow("Result", result) # display the result img

    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_simple_geometric_shapes_example()
