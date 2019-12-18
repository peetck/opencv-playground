import cv2
import numpy as np

def show(value):
    """ On change function show """
    print(value) # display current value
def trackbar_example():
    """ trackbar_example function """
    img = np.zeros((300, 512, 3), np.uint8) # create black img (300 * 512)
    football = cv2.imread("football.jpg") # read football.jpg

    cv2.namedWindow("Color") # namedWindow "Color"

     # create trackbar name (R, G, B) to window "Color" with range 0 - 255 and on change is show(function)
    cv2.createTrackbar("R", "Color", 0, 255, show)
    cv2.createTrackbar("G", "Color", 0, 255, show)
    cv2.createTrackbar("B", "Color", 0, 255, show)

    cv2.namedWindow("Football") # namedWindow "Football"
     # create trackbar name switch to window "Football" with range 0 - 1 and in change is show(function)
    cv2.createTrackbar("Switch", "Football", 0, 1, show)

    while True:
        r = cv2.getTrackbarPos("R", "Color") # get trackbar "R" value in "Color" window
        g = cv2.getTrackbarPos("G", "Color") # get trackbar "G" value in "Color" window
        b = cv2.getTrackbarPos("B", "Color") # get trackbar "B" value in "Color" window

        img[:] = [b, g, r] # convert img color

        if cv2.getTrackbarPos("Switch", "Football") == 1: # if trackbar "Switch" value in "Football" window = 1
            cv2.imshow("Football" , cv2.cvtColor(football, cv2.COLOR_BGR2GRAY)) # display football as gray scale
        else:
            cv2.imshow("Football" , football) # display football

        cv2.imshow("Color", img) # display img

        if cv2.waitKey(1) & 0xFF == ord("q"): # if press "q"
            break # break the loop

    cv2.destroyAllWindows()
trackbar_example()
