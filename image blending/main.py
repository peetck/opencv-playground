import cv2
import numpy as np
from matplotlib import pyplot as plot

"""
Blending using pyramids in 5 Step:
    1. Load two images (apple & orange).
    2. Find the gaussian pyramids for each images (in this example, number of levels is 6).
    3. From gaussian pyramids, find their laplacian pyramids.
    4. Join the left (left half of apple) and the right (right half of orange) in each levels of laplacian pyramids.
    5. From the join image pyramids, reconstruct it.
"""

def image_blending_example():
    """ image_blending_example function """
    apple = cv2.imread("apple.jpg") # read apple.jpg
    orange = cv2.imread("orange.jpg") # read orange.jpg

    print(apple.shape) # print apple shape (col, row, ch)
    print(orange.shape) # print orange shape  (col, row, ch)

    apple_orange = np.hstack((apple[:, :256, :], orange[:, 256:, :])) # combine it half/half

    # generate gaussian pyramid for apple and orange

    apple_cpy = apple.copy() # copy apple img
    orange_cpy = orange.copy() # copy orange img

    gaussian_apple = [apple_cpy] # create list of gaussian pyramid (apple)
    gaussian_orange = [orange_cpy] # create list of gaussian pyramid (orange)

    for i in range(6): # doing 6 time
        apple_cpy = cv2.pyrDown(apple_cpy) # pyramid down (apple)
        orange_cpy = cv2.pyrDown(orange_cpy) # pyramid down (orange)

        gaussian_apple.append(apple_cpy) # after pyramid down add it to gaussian list (apple)
        gaussian_orange.append(orange_cpy) # after pyramid down add it to gaussian list (orange)

    # generate laplacian pyramid for apple and orange

    apple_cpy = gaussian_apple[5] # get last index of gaussian pyramid (upper level) (apple)
    orange_cpy = gaussian_orange[5] # get last index of gaussian pyramid (upper level) (orange)

    laplacian_apple = [apple_cpy] # create list of laplacian pyramid (apple)
    laplacian_orange = [orange_cpy] # create list of laplacian pyramid (orange)
    
    for i in range(4, -1, -1):
        gaussian_expanded_apple = cv2.pyrUp(gaussian_apple[i + 1]) # pyramid up (gaussian apple)
        gaussian_expanded_orange = cv2.pyrUp(gaussian_orange[i + 1]) # pyramid up (gaussian orange)

        # add it to laplacian list
        laplacian_apple.append(cv2.subtract(gaussian_apple[i], gaussian_expanded_apple))
        laplacian_orange.append(cv2.subtract(gaussian_orange[i], gaussian_expanded_orange))
    
    # add left and right halves of images in each level

    apple_orange_py = [] # create apple orange pyramid list

    for i, j in zip(laplacian_apple, laplacian_orange):
        col, row, ch = i.shape # get shape of apple (or orange) * same size *
        laplacian = np.hstack((i[:, :int(col / 2), :], j[:, int(row / 2):, :])) # combine it half/half
        apple_orange_py.append(laplacian) # add to apple orange pyramid list

    # reconstruct

    apple_orange_reconstruct = apple_orange_py[0] # get last index of apple orange pyramid

    for i in range(1, 6):
        apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct) # pyramid up apple orange
        apple_orange_reconstruct = cv2.add(apple_orange_py[i], apple_orange_reconstruct) # add it with each level of apple orange pyramid

    titles = ["Apple", "Orange", "Simple combine", "Using Pyramids"]
    images = [apple, orange, apple_orange, apple_orange_reconstruct]

    for i in range(len(titles)):
        plot.subplot(2, 2, i + 1)
        plot.title(titles[i])
        plot.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plot.xticks([])
        plot.yticks([])

    plot.show()
image_blending_example()
