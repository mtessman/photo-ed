# point.py
import numpy
import cv2


def pointillize(img, upthresh=255, lowerthresh=0):
    # Creates a grid of random numbers between zero and 0 the same size as the image and multiplies with the img
    randgrid = numpy.random.ranf(img.shape)

    product = numpy.where(img > upthresh, 240, img) # Upper threshhold makes light part of the image lighter
    product = numpy.where(img < lowerthresh, 20, product) #Lower threshhold makes dark parts darker
    product = numpy.multiply((product.copy()), randgrid)

    return product


def main():

    filename = 'flower.jpg'
    img = cv2.imread(filename, 0)  # Imports image from file

    product = pointillize(img, 220, 60) #Calls pointillize on the image

    # Saves the pointallized image
    savename = filename[:-4] + 'Point.jpg'
    cv2.imwrite(savename, product)
    print 'Image saved as: ' + savename

    # # Shows the image(s) on screen
    # cv2.imshow('Image', img)
    # cv2.imshow('Result', product)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()

# Notes
#    - Squaring each index of the grid provides more contrast
#    - product = product and threshhold
