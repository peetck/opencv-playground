import cv2
import numpy as np
def main():
    img = cv2.imread("football.jpg", 1) # read football.jpg img
    
    print(img.shape) # print a tuple of number of rows, columns, and channels
    print(img.size) # print total number of pixels is accessed
    print(img.dtype) # print image datatype is obtained

    cv2.imshow("Football", img) # display img

    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()

# 592 304 >> 676 351
