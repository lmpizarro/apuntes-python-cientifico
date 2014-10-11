# -*- coding: utf-8 -*-


#!/usr/bin/env python

from matplotlib.pyplot import * # Grab MATLAB plotting functions
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from numpy import linalg
from control import statefbk

k2 = 39.6; m = 22.6 / 1000.0; k1 = 0.770; R = 19.9; L = 520.0 / 1000.0; ka = 5.0

Cx = diag ([.1,1,.2])
Cp  = matrix ( [ [1, 0, 0], [0, 0, 1] ]) 
C = Cp * Cx
A = matrix ([[0, 1, 0],[k2/m, 0, -k1],[0,0,-R/L]])

B = ka*matrix ([[0],[0],[1/L]])
D = ka*matrix ([[0],[0]])

sys = ss(A, B, C, D)

poles = linalg.eig(A)[0]

print "polos: ", poles

(y, t) = step(sys)
plot(t, y)
show()


p1 = -10 + 10j;
p2 = -10 - 10j;
p3 = -50;

K = place(A,B, [p1,p2,p3]) 
Af  = A -B*K
Cf = C - D*K

polesFb = linalg.eig(Af)[0]

print polesFb


sysfb = ss(Af, B, Cf, D)

#T = linspace(0, 1, 100)
(y, t, x) = lsim(sys, U=0, T=T)
#(y, t) = step(sysfb)
plot(t, y)
show()

#kr = C*linalg.inv(Af)*B

#print
#print kr


