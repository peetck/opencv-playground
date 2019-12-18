import cv2
import numpy as np
def operations_on_images_example():
    """ operations_on_images_example function """
    img = cv2.imread("football.jpg", 1) # read football.jpg img
    logo = cv2.imread("logo.png", 1) # read logo.png img

    img = cv2.resize(img, (700, 400)) # resize img to (700 * 400)
    logo = cv2.resize(logo, (700, 400)) # resize logo to (700 * 400)

    print(img.shape) # print a tuple of number of rows, columns, and channels
    print(img.size) # print total number of pixels is accessed
    print(img.dtype) # print image datatype is obtained

    b, g, r = cv2.split(img) # get numpy array (blue, green, red) from img
    print(b, g, r)

    copy_img = cv2.merge((b, g, r)) # merge numpy array (blue, green, red) to img(copy_img)

    crop = copy_img[280:340, 330:390] # get numpy array in some of pixels from copy_img
    copy_img[273:333, 100:160] = crop # copy it to another place in copy_img

    cv2.imshow("Original Image", img) # display img
    cv2.imshow("Copy Image", copy_img) # display copy_img
    cv2.imshow("Logo Image", logo) # display logo

    #add = cv2.add(img, logo)
    add = cv2.addWeighted(img, .9, logo, .1, 0) # add logo to img with img weight = .9 logo = .1
    cv2.imshow("Add logo to Image", add) # display add

    cv2.waitKey(0)
    cv2.destroyAllWindows()
operations_on_images_example()
