import cv2
import numpy as np
from matplotlib import pyplot as plot

def image_gradients_and_edge_detection():
    """ image_gradients_and_edge_detection function """
    img = cv2.imread("sudoku.png", 0) # read sudoku.png

    lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # Laplace's method (kernal size = 3) use 64 bit float for support negative number we'll dealing with
    lap = np.uint8(np.abs(lap)) # take abs value and convert back to unsigned 8 bit integer

    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) # Sobel X
    sobelX = np.uint8(np.abs(sobelX))

    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) # Sobel Y
    sobelY = np.uint8(np.abs(sobelY))

    sobelCombined = cv2.bitwise_or(sobelX, sobelY) # or (sobel X, sobel Y)

    titles = ["Image", "Laplacian", "Sobel X", "Sobel Y", "Sobel Combined"]
    images = [img, lap, sobelX, sobelY, sobelCombined]

    for i in range(len(titles)):
        plot.subplot(2, 3, i + 1)
        plot.title(titles[i])
        plot.imshow(images[i], "gray")
        plot.xticks([])
        plot.yticks([])

    plot.show()
image_gradients_and_edge_detection()
