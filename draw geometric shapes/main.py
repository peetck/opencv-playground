import cv2
import numpy as np
def draw_geometric_shapes_example():
    """ draw_geometric_shapes_example function """
    img = np.zeros([1914, 1080, 3], np.uint8) # create img with black bg (1914 x 1080)

    # draw line to img from (0, 0) to (255, 255) with red color (0, 0, 255) (B G R) and 5 thickness
    img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

    # draw arrow line to img from (0, 200) to (255, 500) with blue color (255, 0, 0) (B G R) and 5 thickness
    img = cv2.arrowedLine(img, (0, 200), (255, 500), (255, 0, 0), 5)

    # draw rectagle to img with green color (255, 0, 0) (B G R) and 5 thickness
    # x1,y1 -------
    # |           |
    # |           |
    # |           |
    # ------- x2,y2
    img = cv2.rectangle(img, (600, 100), (900, 400), (0, 255, 0), 5)

    # draw circle to img at (1000, 40) 50 radius with red color (0, 0, 255) (B G R) and 5 thickness
    img = cv2.circle(img, (1000, 400), 50, (0, 0, 255), 5)

    # put text msg "Hello world!!" to img at (70, 750) hershey font 5 font size with text color white (255, 255, 255)
    # and thickness 5 with line type AA
    img = cv2.putText(img, "Hello world!!", (70, 750), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 5, cv2.LINE_AA)

    cv2.imshow("Image", img) # display img
    cv2.waitKey(0)
    cv2.destroyAllwindows()
draw_geometric_shapes_example()
