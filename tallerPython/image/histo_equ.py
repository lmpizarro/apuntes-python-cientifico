#
# Histogram equalization with Python and NumPy
#
# http://www.janeriksolem.net/2009/06/histogram-equalization-with-python-and.html
#
from PIL import Image
from scipy import misc
import numpy
import matplotlib.pyplot as plt


def histeq(im,nbr_bins=256):

   #get image histogram
   imhist,bins = numpy.histogram(im.flatten(),nbr_bins,normed=True)
   plt.plot(imhist)
   plt.show()


   cdf = imhist.cumsum() #cumulative distribution function
   cdf = 255 * cdf / cdf[-1] #normalize
   plt.plot(cdf)
   plt.show()


   #use linear interpolation of cdf to find new pixel values
   im2 = numpy.interp(im.flatten(),bins[:-1],cdf)

   return im2.reshape(im.shape), cdf



im = numpy.array(Image.open('dna.jpeg').convert('L'))
im2,cdf = histeq(im)

im_p = numpy.uint8(im2)
im_png = Image.fromarray(im_p)
misc.imsave('histo_equ.png', im_png)


