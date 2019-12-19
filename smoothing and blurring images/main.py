import cv2
import numpy as np
from matplotlib import pyplot as plot

def smoothing_and_blurring_images_example():
    """ smoothing_and_blurring_images_example function """
    #img = cv2.cvtColor(cv2.imread("opencv-logo.png"), cv2.COLOR_BGR2RGB) # read image
    img = cv2.cvtColor(cv2.imread("water.png"), cv2.COLOR_BGR2RGB) # read image
    #img = cv2.cvtColor(cv2.imread("lena-1.jpg"), cv2.COLOR_BGR2RGB) # read image

    filter2d = cv2.filter2D(img, -1, np.ones((5, 5), np.float32) / 25) # filter 2d
    blur = cv2.blur(img, (5, 5)) # blur filter
    gblur = cv2.GaussianBlur(img, (5, 5), 0) # gaussian blur filter
    median = cv2.medianBlur(img, 5) # median blur filter (good with salt and pepper noise)
    bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # bilateral filter

    titles = ["Image", "2D Convolution", "Blur", "Gaussian Blur", "Median", "Bilateral Filter"]
    images = [img, filter2d, blur, gblur, median, bilateralFilter]

    for i in range(len(titles)):
        plot.subplot(2, 3, i + 1)
        plot.title(titles[i])
        plot.imshow(images[i])
        plot.xticks([])
        plot.yticks([])
    plot.show()

smoothing_and_blurring_images_example()
