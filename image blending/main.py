import cv2
import numpy as np
from matplotlib import pyplot as plot

def image_blending_example():
    """ image_blending_example function """
    apple = cv2.imread("apple.jpg")
    orange = cv2.imread("orange.jpg")


    titles = ["Apple", "Orange"]
    images = [apple, orange]

    for i in range(len(titles)):
        plot.subplot(2, 2, i + 1)
        plot.title(titles[i])
        plot.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plot.xticks([])
        plot.yticks([])

    plot.show()
image_blending_example()
