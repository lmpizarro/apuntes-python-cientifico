# -*- coding: utf-8 -*-
'''

Feedback Control of Dynamec Systems
Franklin - Powell - Emami-Naeini
Pag 405

'''

#!/usr/bin/env python

import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from scale import *

w0 = 1

A = matrix ([[0,1],[-w0*w0, 0]])
B = matrix ([[0],[1]])
C = matrix ([1,0])
D = matrix ([[0]])

(Nx,Nu) = scale (A,B,C,D)

print 4*'\n'
print Nx
print 4*'\n'
print Nu


