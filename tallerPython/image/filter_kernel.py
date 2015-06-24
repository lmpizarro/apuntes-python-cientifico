# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:48:15 2015

refs: 

Digital Filters    
http://homepages.inf.ed.ac.uk/rbf/HIPR2/filtops.htm
http://homepages.inf.ed.ac.uk/rbf/HIPR2/unsharp.htm

Multidimensional image processing
http://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html

Digital mammography image enhancement using improved unsharp masking approach

http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=5647218

https://github.com/kovimesterr/SSIP2013

@author: lpizarro
"""

import numpy
from PIL import Image
import kernels3x3 as k33
from scipy import ndimage

def num_update(u):
    u[1:-1,1:-1] = (-u[2:,1:-1] - u[:-2,1:-1] + u[1:-1,1:-1] +
        u[1:-1,2:] - u[1:-1,:-2])/-3

def equal_values_cruz(u):
    u[1:-1,1:-1] = (u[2:,1:-1] + u[:-2,1:-1] + u[1:-1,1:-1] +
    u[1:-1,2:] + u[1:-1,:-2]) / 5

def equal_values(u):
    u[1:-1,1:-1] = (u[2:,1:-1] + u[:-2,1:-1] + u[:-2,:-2] + u[:-2,2:] + u[1:-1,1:-1] +
    u[2:,2:] + u[2:,:-2] + u[1:-1,2:] + u[1:-1,:-2]) / 5

def equal_values_diagonal(u):
    u[1:-1,1:-1] = (u[:-2,:-2] + u[:-2,2:] + 
    u[1:-1,1:-1] +
    u[2:,2:] + u[2:,:-2]) / 9

def calc(u, Niter=1, func=num_update, args=()):
    print("args", args)
    for i in range(Niter):
        func(u,args)
    return u

print(k33.filter1, k33.norm_filter1)
# Lectura de la imagen
im = Image.open("dna.jpeg")
im.show()
# Conversión a array numpy
pix = numpy.array(im)
pix_buffer = numpy.copy(pix)

pix_filter = calc(pix, func=k33.kernel_update, args = (k33.gaussian, k33.norm_gaussian,))

pix_sharp = pix_buffer + 0.4 * (pix_buffer - pix_filter)

print("original", pix_buffer.min(), pix_buffer.max(), pix_buffer.mean(), numpy.median(pix_buffer))
print("filtered", pix_filter.min(), pix_filter.max(), pix_filter.mean(), numpy.median(pix_filter))

im_p = Image.fromarray(pix_sharp)

im_p.show()


