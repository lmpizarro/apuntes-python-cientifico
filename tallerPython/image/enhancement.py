import numpy
from scipy import misc
from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt

# Lectura de la imagen
im = Image.open("dna.jpeg")

# Conversión a array numpy
pix = numpy.array(im)

'''
plt.imshow(pix)
plt.annotate ("original", xy=(100,100), color="white")
plt.gray()
plt.show()
'''

# Lectura de las propiedades de pix
print("formato NUMPY ", pix.shape, pix.dtype, pix.max(), pix.min())

smooth = ndimage.gaussian_filter(pix, 2)
g = pix - smooth 
k = 0.1
enhan = pix + k * g 
print(enhan.max(), enhan.min())

im_p = numpy.uint8(enhan)
im_png = Image.fromarray(im_p)
misc.imsave('gaussian_enhancement.png', im_png)

'''
plt.imshow(im_p)
plt.annotate ("gaussian smooth", xy=(100,100), color="white")
plt.gray()
plt.show()
'''

smooth = ndimage.median_filter(pix, 1)
g = pix - smooth 
print(smooth.max(), smooth.min())
k = 0.7
enhan = pix + k * g 

im_p = numpy.uint8(enhan)
im_png = Image.fromarray(im_p)
misc.imsave('median_enhancement.png', im_png)

'''
plt.imshow(im_p)
plt.annotate ("median smooth", xy=(100,100), color="white")
plt.gray()
plt.show()
'''

smooth = ndimage.uniform_filter(pix, size=3)
g = pix - smooth 
print(smooth.max(), smooth.min())
k = 0.1
enhan = pix + k * g 

im_p = numpy.uint8(enhan)
im_png = Image.fromarray(im_p)
misc.imsave('uniform_enhancement.png', im_png)

