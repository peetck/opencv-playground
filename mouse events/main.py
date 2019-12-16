import cv2
import numpy as np
def clicked(event, x, y, flags, param):
    """ click event function """
    if event == cv2.EVENT_LBUTTONDOWN: # if left click
        print("Left  clicked at (%d, %d)" %(x, y))

        # put text msg position to img
        cv2.putText(img, "Position : (%d, %d)" %(x, y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0), 2)

        # display again
        cv2.imshow("Color", img)
    elif event == cv2.EVENT_RBUTTONDOWN: # if right click
        print("Right clicked at (%d, %d)" %(x, y))
        blue = img[y, x, 0] # get blue color of img
        green = img[y, x, 1] # get green color of img
        red = img[y, x, 2] # get red color of img

        # put text msg color(BGR) to img
        cv2.putText(img, "Color(BGR) : (%s, %s, %s)" %(blue, green, red), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)

        # display again
        cv2.imshow("Color", img)

        clicked_color = np.zeros((512, 512, 3), np.uint8) # create black img (512*512)
        clicked_color[:] = [blue, green, red] # set it color to [blue, green, red]

        cv2.imshow("Clicked color", clicked_color) # show clicked_color img

img = cv2.imread("color.png", 1) # red color.png img
cv2.imshow("Color", img) # display img
cv2.setMouseCallback("Color", clicked) # set mouse call back to clicked function
cv2.waitKey(0)
cv2.destroyAllWindows()

