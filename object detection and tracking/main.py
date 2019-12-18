import cv2
import numpy as np

def object_detection_and_tracking():
    """ object_detection_and_tracking function """
    img = cv2.imread("ball.jpg", 1)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.namedWindow("Tracking")
    while True:
        cv2.imshow("Tracking", img)
        cv2.imshow("HSV", img_hsv)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
object_detection_and_tracking()
