# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:16:41 2015

@author: lpizarro
"""

import numpy
from PIL import Image
from scipy import ndimage

footprint = [[1,1,1],[1,1,1],[1,1,1]]

im = Image.open("dna_part.pgm")
im.show()
a = numpy.array(im)

pix_filter = ndimage.generic_filter(a, numpy.median, footprint=footprint)
pix_filter = numpy.uint8(pix_filter)
pix_gen = numpy.copy(pix_filter)
im_p = Image.fromarray(pix_filter)
im_p.show()


pix_filter = ndimage.filters.median_filter(a, size=(3,3))
pix_filter = numpy.uint8(pix_filter)
im_p = Image.fromarray(pix_filter)
im_p.show()

pix_diff = pix_gen - pix_filter
#pix_filter = numpy.uint8(pix_diff)
#im_p = Image.fromarray(pix_diff)
#im_p.show()


print(pix_diff.min(), pix_diff.max(), pix_diff.mean())
