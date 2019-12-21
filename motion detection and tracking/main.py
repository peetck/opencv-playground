import cv2
import numpy as np

"""
Detect if people in video is moving
"""

def motion_detection_and_tracking_example():
    """ motion_detection_and_tracking_example function """
    video = cv2.VideoCapture("vtest.avi") # read vtest.avi

    _, current_frame = video.read() # get first frame
    _, next_frame = video.read() # get first frame

    while video.isOpened():

        diff = cv2.absdiff(current_frame, next_frame) # calculate difference between current frame and next frame

        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # convert difference to grayscale

        # difference has noises because of details and light on video so gaussian blurring is eliminating the noises
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #  threshold

        dilated = cv2.dilate(thresh, None, iterations=4) # dilating it

        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # finding contours from clean threshold

        # eliminating small contour which can not be a human
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 600 or w >= h:
                continue

            cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # drawing rectangle

        cv2.imshow("Difference", gray) # display difference
        cv2.imshow("Blur Difference", blur) # display blur Difference
        cv2.imshow("Threshold", thresh) # display threshold
        cv2.imshow("dilated", dilated) # display dilated
        cv2.imshow("Video", current_frame) # display frame

        current_frame = next_frame
        _, next_frame = video.read()

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

motion_detection_and_tracking_example()
