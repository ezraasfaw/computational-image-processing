import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def Histogram(Channel):

# Histogram returns a histogram for an 8-bit grayscale image.

  if Channel.dtype != ‘uint8’:
    return(-1)
  r, c = Channel.shape
  H = np.zeros(256, dtype=int)
  for x in range(c):
    for y in range(r):
      H[Channel[y, x]] += 1
return H


# region Open image, convert it to a NumPy array and then split it up into its channels.
Raw_Image = Image.open(r’Media\gettyimages-162623666.jpg’)
RGB_Image = np.asarray(Raw_Image)
R_Channel = RGB_Image[:, :, 0]
G_Channel = RGB_Image[:, :, 1]
B_Channel = RGB_Image[:, :, 2]
# endregion

# region Compute the histogram for each channel in the image.
R_Histogram = Histogram(R_Channel)
G_Histogram = Histogram(G_Channel)
B_Histogram = Histogram(B_Channel)
# endregion

# region Plot each channel with it’s corresponding histogram.
 plt.figure(1)
 plt.subplot(2, 3, 1)
 plt.imshow(R_Channel, cmap=’gray’)
 plt.title(‘Red Channel’)
 plt.subplot(2, 3, 4)
 plt.plot(R_Histogram)

 plt.subplot(2, 3, 2)
 plt.imshow(G_Channel, cmap=’gray’)
 plt.title(‘Green Channel’)
 plt.subplot(2, 3, 5)
 plt.plot(G_Histogram)

 plt.subplot(2, 3, 3)
 plt.imshow(B_Channel, cmap=’gray’)
 plt.title(‘Blue Channel’)
 plt.subplot(2, 3, 6)
 plt.plot(B_Histogram)
 # endregion

# region Plot the original image with the channel histograms superimposed for comparison on a log scale.
plt.figure(2)
plt.subplot(1, 2, 1)
plt.imshow(RGB_Image)
plt.subplot(1, 2, 2)
plt.semilogy(R_Histogram, ‘r’)
plt.semilogy(G_Histogram, ‘g’)
plt.semilogy(B_Histogram, ‘b’)
plt.title(‘Combined RGB Profile (Log Scale)’)
ax = plt.gca()
ax.set_aspect(50)
plt.show()
# endregion
