import cv2
import numpy as np
from matplotlib import pyplot as plot

def morphological_transformations_example():
    """ morphological_transformations_example function """
    img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE) # read smarties.png (gray scale)
    img2 = cv2.imread("j.png", 0) # read j.png (gray scale)

    _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) # create mask from img using thresh_binary_inv

    kernal = np.ones((5, 5), np.uint8) # create kernal

    dilation = cv2.dilate(mask, kernal, iterations=2) # increase area of shape
    erosion = cv2.erode(mask, kernal, iterations=1) # erode shape
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # applies erosion first follow by dilation
    closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # applies dilation first follow by erosion
    mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal) # difference between dilation and erosion of image
    th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal) # difference between the input image and opening

    dilation2 = cv2.dilate(img2, kernal, iterations=2)
    erosion2 = cv2.erode(img2, kernal, iterations=1)
    opening2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernal)
    closing2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernal)
    mg2 = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kernal)
    th2 = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernal)

    titles = ["image", "mask", "dilation", "erosion", "opening", "closing", "mg", "th"\
            , "image", "mask", "dilation", "erosion", "opening", "closing", "mg", "th"]
    images = [img, mask, dilation, erosion, opening, closing, mg, th\
            , img2, img2, dilation2, erosion2, opening2, closing2, mg2, th2]

    plot.rcParams["figure.figsize"] = (16,8) # set figure size

    for i in range(len(titles)):
        plot.subplot(4, 4, i + 1)
        plot.title(titles[i])
        plot.imshow(images[i], "gray")
        plot.xticks([])
        plot.yticks([])
    plot.show()
morphological_transformations_example()
