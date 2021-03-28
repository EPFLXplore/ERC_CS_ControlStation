# transcription of volume2.m
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from scipy import ndimage
from skimage.feature import canny
from skimage.transform import hough_line, hough_line_peaks
import numpy as np
import cv2 as cv

# # read image
# image_rgb = plt.imread("picture_1.png") # values between 0 and 1, float, 3d image (h, w, channel)

# # convert to gray image
# image_gray = rgb2gray(image_rgb) # values between 0 and 1, float, 2d image (h, w)
# # plt.imshow(image_gray, cmap="gray")

# # convert grayscale to boolean field of intensity larger than given factor
# Ibinary = image_gray > 120 / 255
# # plt.imshow(Ibinary, cmap="gray")

# # fill holes
# Ibinary = ndimage.binary_fill_holes(Ibinary).astype(int)
# # plt.imshow(Ibinary, , cmap="gray")

# # detect edges in image using edge-detection algorithm "canny"
# # https://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.canny
# BW = canny(Ibinary*1.0) # binary edge map
# plt.imshow(BW)

# # # perform a straight line Hough transform, returns hough transform accumulator, angles and distance
# # # https://scikit-image.org/docs/dev/api/skimage.transform.html?highlight=hough%20circle#skimage.transform.hough_line
# # H, theta, rho  = hough_line(BW)

# # # return peaks in a straight line Hough transform. Identifies most prominent lines separated by a certain angle and distance in a Hough transform. 
# # # https://scikit-image.org/docs/dev/api/skimage.transform.html?highlight=hough%20circle#skimage.transform.hough_line_peaks
# # H, theta, rho = hough_line_peaks(H, theta, rho, threshold=np.ceil(0.5*max(H)), num_peaks=6)
# # lines = HoughLines(BW)


img = cv.imread(cv.samples.findFile('picture_1.png'))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # between 0 and 255
print(gray)
# gray = (gray>120)*255.0
gray = (gray>120)

print(gray)

# # fill holes
Ibinary = np.uint8(ndimage.binary_fill_holes(gray))*255
# # plt.imshow(Ibinary, , cmap="gray")

print(Ibinary)

edges = cv.Canny(Ibinary,0,255,apertureSize = 3)

# while(True):
# 	cv.imshow('frame', edges)
# 	if cv.waitKey(1) & 0xFF == ord('q'):
# 		break
average=0
lines = cv.HoughLinesP(edges,1,np.pi/360,98,minLineLength=7,maxLineGap=5)
for line in lines:
    x1,y1,x2,y2 = line[0]
    average+= (y1+y2)/2.0

print(average/len(lines))