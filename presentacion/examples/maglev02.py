# -*- coding: utf-8 -*-

'''
http://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlStateSpace#24
'''

#!/usr/bin/env python

from matplotlib.pyplot import * # Grab MATLAB plotting functions
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from numpy import linalg
from control import statefbk

A = matrix ([[0, 1, 0],[980, 0, -2.8],[0,0,-100]])
B = matrix ([[0],[0],[100]])
C = matrix ([[1,0, 0]])

sys = ss(A, B, C, 0)

poles = linalg.eig(A)[0]

print "polos: ", poles

(y, t) = step(sys)
plot(t, y)
show()

p1 = -20 + 20j;
p2 = -20 - 20j;
p3 = -100;

K = place(A,B, [p1,p2,p3]) 
Af  = A -B*K

polesFb = linalg.eig(Af)[0]

print "polos fb ", polesFb

sysfb = ss(Af, B, C, 0)

x0 = matrix ([[0.01],[0],[0]])
T = arange (0,2, .01)  # t = 0:0.01:2;
#u = zeros(T.shape)    # zeros(size(t))

#(y, t, x) = lsim(sysfb, U=u, T=T, X0 = x0)

Nbar = -285.7143   # 1/y t -> oo

u = ones(T.shape)    # ones(size(t))

(y, t, x) = lsim(sysfb, U=Nbar*u, T=T)

plot(t, y)
show()

