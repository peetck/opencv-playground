import cv2
def read_write_display_images_example():
    """ read_write_display_images_example function """
    image = cv2.imread("space.jpg", 1) # read space.jpg image file
    cv2.imshow("Space Image", image) # display image(space.jpg)
    cv2.imwrite("new_space.jpg", image) # copy space.jpg and save it as new_space.jpg
    cv2.waitKey(0)
    cv2.destroyAllWindows()
read_write_display_images_example()
