import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.measure import regionprops, label
from scipy import ndimage

# load image
image_rgb = plt.imread("picture_1.png")

# convert image to grayscale
image_gray = rgb2gray(image_rgb) # values between 0 and 1

# plt.imshow(image_gray)
# print(image_gray)

# definition of saturation
Ibinary = image_gray > 150/255 # try different values for your problem, 
# plt.imshow(Ibinary)

# fill holes
Ibinary = ndimage.binary_fill_holes(Ibinary).astype(int)
# plt.imshow(Ibinary)

# get labeled image and number of blobs
# labeled image is made of integers, where each integer corresponds to one blob
# https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.label
labeledImage, numberOfBlobs = label(Ibinary, return_num=True)
# plt.imshow(labeledImage)

# 
# https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops
blobMeasurements = regionprops(labeledImage)

C = 0.008; # Conversion factor m/pixel. 

equivDiameter = []
for item in blobMeasurements:
  if item.equivalent_diameter > 10:
    equivDiameter.append(item.equivalent_diameter*C)

# plt.imshow(labels_im)
plt.hist(equivDiameter)


#plt.imshow(labels_im)
plt.show()