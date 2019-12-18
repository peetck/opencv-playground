import cv2
import numpy as np

def show(value):
    """ On change function show """
    print(value) # display current value

def object_detection_and_tracking_example():
    """ object_detection_and_tracking function """
    cv2.namedWindow("Tracking") # create window "Tracking"
    # camera = cv2.VideoCapture(0)

    # add trackbar to Tracking window
    cv2.createTrackbar("Lower H", "Tracking", 0, 255, show)
    cv2.createTrackbar("Lower S", "Tracking", 0, 255, show)
    cv2.createTrackbar("Lower V", "Tracking", 0, 255, show)
    cv2.createTrackbar("Upper H", "Tracking", 0, 255, show)
    cv2.createTrackbar("Upper S", "Tracking", 0, 255, show)
    cv2.createTrackbar("Upper V", "Tracking", 0, 255, show)

    # set start value of each trackbar
    cv2.setTrackbarPos("Lower H", "Tracking", 110)
    cv2.setTrackbarPos("Lower S", "Tracking", 50)
    cv2.setTrackbarPos("Lower V", "Tracking", 50)
    cv2.setTrackbarPos("Upper H", "Tracking", 170)
    cv2.setTrackbarPos("Upper S", "Tracking", 255)
    cv2.setTrackbarPos("Upper V", "Tracking", 255)

    while True:
        img = cv2.imread("ball.jpg", 1) # read ball.jpg
        #_, img = camera.read()
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert img to hsv color and save it as img_hsv

        # get lower and upper color range from each trackbar and create to numpy array
        lower = np.array([cv2.getTrackbarPos("Lower H", "Tracking"), \
                        cv2.getTrackbarPos("Lower S", "Tracking"), \
                        cv2.getTrackbarPos("Lower V", "Tracking")])
        upper = np.array([cv2.getTrackbarPos("Upper H", "Tracking"), \
                        cv2.getTrackbarPos("Upper S", "Tracking"), \
                        cv2.getTrackbarPos("Upper V", "Tracking")])

        mask = cv2.inRange(img_hsv, lower, upper) # create mask

        result = cv2.bitwise_and(img, img, mask=mask) # bitwise img + img + mask

        cv2.imshow("Original Image", img) # display original img
        cv2.imshow("Mask", mask) # display mask
        cv2.imshow("Tracking", result) # display Tracking window

        if cv2.waitKey(1) & 0xFF == ord("q"): # if press "q"
            break # break the loop
    #camera.release()
    cv2.destroyAllWindows()
object_detection_and_tracking_example()
