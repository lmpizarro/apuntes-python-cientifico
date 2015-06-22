# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import matplotlib.pyplot as plt

print("hola", np.random.normal(4,5))

xs = np.array([1, 2, 3, 4, 5, 6, 7, np.pi, 9, np.e], float)

def vect_trivial (x, y):    
    z = np.sin ((x + y)**2)
    z = z * 2


vect_trivial(xs, xs)


def sin_add_square(x, y):
    z = np.sin ((x + y)**2)
    if z <= 0.0:
        z = 0.0
    return z
    
    
print(sin_add_square(2,3))



'''
Así se produce un error
la función no está definida  para
arrays 
sin_add_square(xs, xs)
'''


vadd_square = np.vectorize(sin_add_square)

'''
Así está vectorizada y opera sobre los
arrays
'''
print(vadd_square(xs, xs))

plt.plot(xs)
