# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:22:21 2015

@author: lpizarro
"""

import numpy

kernel = numpy.asarray([i for i in range(9)]).reshape(3,3)

kernel[:,:] = -1
kernel[1,1] = 1
filter1 = numpy.copy(kernel)
norm_filter1 = filter1.sum()

kernel[:,:] = 1
mean = numpy.copy(kernel)
norm_mean = mean.sum()


kernel[0,0] = 0; kernel[0,1] = 2; kernel[0,2] = -1
kernel[1,0] = 2; kernel[1,1] = 4; kernel[1,2] = 2
kernel[2,0] = -1; kernel[2,1] = 2; kernel[2,2] = 0
filter2 = numpy.copy(kernel)
norm_filter2 = filter2.sum()

kernel[0,0] = 1; kernel[0,1] = 2; kernel[0,2] = 1
kernel[1,0] = 2; kernel[1,1] = 4; kernel[1,2] = 2
kernel[2,0] = 1; kernel[2,1] = 2; kernel[2,2] = 1
gaussian = numpy.copy(kernel)
norm_gaussian = gaussian.sum()

lap1 = numpy.copy(kernel)
lap1[0,0] = 0; lap1[0,1] = -1; lap1[0,2] = 0
lap1[1,0] = -1; lap1[1,1] = 4; lap1[1,2] = -1
lap1[2,0] = 0;lap1[2,1] = -1; lap1[2,2] = 0
norm_lap1 = 1

lap2 = numpy.copy(kernel)
lap2[0,0] = -1; lap2[0,1] = -1; lap2[0,2] = -1
lap2[1,0] = -1; lap2[1,1] = 8; lap2[1,2] = -1
lap2[2,0] = -1;lap2[2,1] = -1; lap2[2,2] = -1
norm_lap2 = 1

lap3 = numpy.copy(kernel)
lap3[0,0] = 1; lap3[0,1] = -2; lap3[0,2] = 1
lap3[1,0] = -2; lap3[1,1] = 4; lap3[1,2] = -2
lap3[2,0] = 1;lap3[2,1] = -2; lap3[2,2] = 1
norm_lap3 = 1

def kernel_update(u, args):
    kernel = args[0]
    norm = args[1]
    print("norm", norm)
    u[1: -1, 1: -1] = ( 
                    kernel[0, 0] * u[: -2, : -2] +
                    kernel[2, 2] * u[2:, 2:] + 
                    kernel[2, 0] * u[2:, : -2] + 
                    kernel[0, 2] * u[: -2, 2:] + 
                    kernel[2, 1] * u[2:, 1: -1] + 
                    kernel[0, 1] * u[: -2, 1: -1] + 
                    kernel[1, 1] * u[1: -1, 1: -1] +
                    
                    kernel[1, 2] * u[1: -1, 2:] + 
                    kernel[1, 0] * u[1: -1, : -2]
                    )/norm


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

                   
