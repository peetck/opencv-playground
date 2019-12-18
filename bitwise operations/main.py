import cv2
import numpy as np
def bitwise_example():
    img1 = np.zeros((250, 500, 3), np.uint8) # create black img
    img2 = cv2.imread("half_black_white.png", 1) # read half_black_white.png

    cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1) # add white rectangle to img1

    cv2.imshow("img1", img1) # display img1
    cv2.imshow("img2", img2) # display img2

    cv2.imshow("bitwise AND", cv2.bitwise_and(img1, img2)) # display and(img1, img2)
    cv2.imshow("bitwise OR", cv2.bitwise_or(img1, img2)) # display or(img1, img2)
    cv2.imshow("bitwise XOR", cv2.bitwise_xor(img1, img2)) # display xor(img1, img2)
    cv2.imshow("bitwise NOT (img1)", cv2.bitwise_not(img1)) # display not(img1)
    cv2.imshow("bitwise NOT (img2)", cv2.bitwise_not(img2)) # display not(img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
bitwise_example()
