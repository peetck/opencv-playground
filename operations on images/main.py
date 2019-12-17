import cv2
import numpy as np
def main():
    img = cv2.imread("football.jpg", 1) # read football.jpg img

    print(img.shape) # print a tuple of number of rows, columns, and channels
    print(img.size) # print total number of pixels is accessed
    print(img.dtype) # print image datatype is obtained

    cv2.imshow("Football", img) # display img

    b, g, r = cv2.split(img) # get numpy array (blue, green, red) from img
    print(b, g, r)

    mergeImage = cv2.merge((b, g, r)) # merge numpy array (blue, green, red) to img
    cv2.imshow("merge", mergeImage) # display mergeImage

    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()

# 592 304 >> 676 351
