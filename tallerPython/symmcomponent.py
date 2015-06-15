"""
file    symcomp.py
author  Ernesto P. Adorio, Ph.D.
UPDEPP (U.P. Clarkfield)
desc    basic symmetrical components for three phase phasors.
Phasors are tuples of the form (r, phi) where r and phi are the
magnitude(absolute value) and phi is the phase angle.
version 0.0.1 april 20, 2011
"""

import math as mt
import cmath as cm

zTOL = 1.0e-8
DTOR = mt.pi / 180.0
RTOD = 180.0 / mt.pi



ONETWENTYRAD = 120 * DTOR
_a_  = cm.rect(1, 120 * mt.pi/ 180.0)
_a2_ = _a_.conjugate()

def dtor(degree):
    """
    Converts degree to radians.
    """
    return degree * DTOR

def rtod(radian):
    """
    Converts radians to degree.
    """
    return radian * RTOD

def  z2pair(z):
    """
    returns z in pair form.
    """ 
    return (z.real, z.imag)

def  pair2z(re, im):
    """
    returns a complex number from the components. 
    """
    return re + im*1j

def  polar2pair(v):
    """
    (r, phi) to (re, im) pair form.
    """
    # Special checking for zero imaginaries!
    # some computations result in an additional 0j
    r, phi = v
    if type(r) == type(1j):
        r =r.real
    if type(phi) == type(1j):
         phi = phi.real

    z = cm.rect(r, phi)
    return z.real, z.imag

def  pair2polar(re, im):
    return polar(pair2z(re,im))

def  zround(v):
    if abs(v[0]) < zTOL:
        return (0.0, 0.0)

def  a(v):
     """
     Applies the a operator to a phasor v in polar form.
     It adds a 120 degree to the phase of the phasor v.
     if v is real, the angle is zero.
     """
     if type(v) != type((0,0)):
        v = (v, 0)
     r     = abs(v[0])
     theta = v[1]

     newangle = theta + ONETWENTYRAD
     return (r * cos(newangle), r * sin(newangle))

def a2(v):
     """
     Applies the a operator to a phasor v in polar form.
     It adds a 120 degree to the phase of the phasor v.
     """
     if type(v) != type((0,0)):
        v = (v, 0)
     r     = abs(v[0])
     theta = v[1]

     newangle = theta + 2*ONETWENTYRAD
     return (r * cos(newangle), r * sin(newangle))


def  symcomp(v1, v2, v3):
     """
     Returns the symmetrical components of the three phasors v1, v2, v3
     which are in tuple (r, theta) form.
     """
     #Convert first to complex rectangular form.
     v1z  = cm.rect(v1[0], v1[1])
     v2z  = cm.rect(v2[0], v2[1])
     v3z  = cm.rect(v3[0], v3[1]) 

     av2  = _a_ * v2z
     a2v2 = _a2_ * v2z
     av3  = _a_* v3z
     a2v3 = _a2_* v3z

     #Null sequence  component.
     E0 = cm.polar((v1z.real+ v2z.real+  v3z.real)/3.0 +  (v1z.imag+ v2z.imag+ v3z.imag)/3.0*1j)

     #Positive sequence component.
     E1 = cm.polar((v1z.real + av2.real +  a2v3.real)/3.0+ (v1z.imag+ av2.imag+ a2v3.imag)/3.0*1j)

     #Negative sequence component.
     E2 = cm.polar((v1z.real + a2v2.real +  av3.real)/3.0+ (v1z.imag+ a2v2.imag+ av3.imag)/3.0*1j)

     return (E0, E1, E2)


def  symcompz(v1, v2, v3):
     """
     Returns the symmetrical components of the three phasors v1, v2, v3
     which are in tuple (r, theta) form.
     """
     av2  = _a_ * v2
     a2v2 = _a2_ * v2
     av3  = _a_* v3
     a2v3 = _a2_* v3

     #Null sequence  component.
     E0 = polar((v1.real+ v2.real+  v3.real)/3.0 +  (v1.imag+ v2.imag+ v3.imag)/3.0*1j)

     #Positive sequence component.
     E1 = polar((v1.real + av2.real +  a2v3.real)/3.0+ (v1.imag+ av2.imag+ a2v3.imag)/3.0*1j)

     #Negative sequence component.
     E2 = polar((v1.real + a2v2.real +  av3.real)/3.0+ (v1.imag+ a2v2.imag+ av3.imag)/3.0*1j)

     return (E0, E1, E2)

def  symcomp2phasors(E0, E1, E2):
     """
     Recreates the phasors form the symmetrical components.
     """
     V1 = cm.polar(cm.rect(E0[0], E0[1]) + cm.rect(E1[0], E1[1]) + cm.rect(E2[0], E2[1]))
     V2 = cm.polar(cm.rect(E0[0], E0[1]) + _a2_* cm.rect(E1[0], E1[1]) + _a_ *cm.rect(E2[0], E2[1]))
     V3 = cm.polar(cm.rect(E0[0], E0[1]) + _a_* cm.rect(E1[0], E1[1]) + _a2_ * cm.rect(E2[0], E2[1]))
     return V1, V2, V3

