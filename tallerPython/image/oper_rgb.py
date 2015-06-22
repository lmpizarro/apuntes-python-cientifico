
# coding: utf-8

# In[33]:

import numpy
from scipy import misc
from PIL import Image
import matplotlib.pyplot as plt

# Lectura de la imagen
im = Image.open("dna.jpeg")

# Lectura de las propiedades
print("formato PIL ", im.format, im.size, im.mode, type(im))
im = im.convert("RGB")


# In[36]:

# Conversión a array numpy
pix = numpy.array(im)

# Lectura de las propiedades de pix
print("formato NUMPY ", pix.shape, pix.dtype, pix.max(), pix.min())
r, g, b = im.split()

image_slice_red =  pix[:,:,0]
image_slice_green =  pix[:,:,1]
image_slice_blue =  pix[:,:,2]

image_slice_blue *=  0.5
image_slice_green *= 1

im_p = Image.fromarray(pix)

im_p.show()


# In[13]:

#print(b_n.max(), g_n.max(), r_n.max())
#print(b_n.min(), g_n.min(), r_n.min())


# In[ ]:
w = 100
h = 100
im_p = numpy.zeros( (w,h,3), dtype=numpy.uint8)
#
#
#
for i in range(10):
    im_red = numpy.random.random_integers(0, 255, 10000).reshape((100, 100))
    im_green = numpy.random.random_integers(0, 255, 10000).reshape((100, 100))
    im_blue = numpy.random.random_integers(0, 255, 10000).reshape((100, 100))
    im_p[:,:,0] = numpy.uint8(im_red)
    im_p[:,:,1] =  numpy.uint8(im_green)
    im_p[:,:,2] =  numpy.uint8(im_blue)
    im_png = Image.fromarray(im_p)
    misc.imsave('random_%02d.png' % i, im_png)

    im_red = numpy.array([0 for i in range(10000)]).reshape((100, 100))
    im_green = numpy.array([250 for i in range(10000)]).reshape((100, 100))
    im_blue = numpy.array([0 for i in range(10000)]).reshape((100, 100))
    im_p[:,:,0] = numpy.uint8(im_red)
    im_p[:,:,1] =  numpy.uint8(im_green)
    im_p[:,:,2] =  numpy.uint8(im_blue)
    im_png = Image.fromarray(im_p)
    misc.imsave('constant.png', im_png)

from glob import glob

filelist = glob('*.png')
filelist.sort()

print(filelist)

