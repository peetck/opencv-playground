import cv2
import numpy as np

def camera_parameters_example():
    """ camera_parameters_example """
    camera = cv2.VideoCapture(0) # get camera
    
    print(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) # print cam width (or .get(3))
    print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) # print cam height (or .get(4))

    camera.set(3, 500) # set camera width
    camera.set(4, 500) # set camera height
    while True:
        _, frame = camera.read() # read camera

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to gray scale
        cv2.imshow("Frame", gray) # display frame

        if cv2.waitKey(1) & 0xFF == ord("q"): # if press "q"
            break # break the loop

    camera.release() # release camera
    cv2.destroyAllWindows()
    
camera_parameters_example()
