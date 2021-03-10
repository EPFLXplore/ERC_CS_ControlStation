import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.measure import regionprops

# load image
image_rgb = plt.imread("test.jpeg")

# convert image to grayscale
image_gray = 0.3 * image_rgb[:, :, 0] + 0.59 * image_rgb[:, :, 1] + 0.11 * image_rgb[:, :, 2]
Ibinary = image_gray > 150 # try different values for your problem

# fillhole function
def fillhole(input_image):
  '''
  input gray binary image  get the filled image by floodfill method
  Note: only holes surrounded in the connected regions will be filled.
  :param input_image:
  :return:
  '''
  im_flood_fill = input_image.copy()
  h, w = input_image.shape[:2]
  mask = np.zeros((h + 2, w + 2), np.uint8)
  im_flood_fill = im_flood_fill.astype("uint8")
  cv2.floodFill(im_flood_fill, mask, (0, 0), 255)
  im_flood_fill_inv = cv2.bitwise_not(im_flood_fill)
  img_out = input_image | im_flood_fill_inv
  return img_out

# fill the holes of the image
Ibinary = fillhole(Ibinary)

C = 0.008; # Conversion factor m/pixel. This was a guess, you should be able to find the real one

num_labels, labels_im = cv2.connectedComponents(Ibinary)

blobMeasurements = regionprops(labels_im)
equivDiameter = []
for item in blobMeasurements:
  equivDiameter.append(item.equivalent_diameter)

#equivDiameter = blobMeasurements[0].equivalent_diameter





plt.imshow(labels_im)
plt.show()