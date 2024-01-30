# add libraries
from skimage import io, color, data
from pylab import *

# read the image of interest
img = io.imread("colorful-2468874_640.jpg")

# convert the image to HSV
# img_hsv = color.rgb2hsv(img)
# img_xyz = color.rgb2xyz(img)
# img_grey = color.rgb2gray(img)
img_grey = color.rgb2lab(img)


# show both images
# figure(0)
# io.imshow(img_hsv)
# title('HSV Image')

figure(0)
io.imshow(img_grey)
title('HSV Image')

# figure(1)
# io.imshow(img_xyz)
# title('XYZ Image')

# figure(2)
# io.imshow(img_grey)
# title('GREY Image')


show()