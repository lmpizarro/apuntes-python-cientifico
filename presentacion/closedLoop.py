# -*- coding: utf-8 -*-

#!/usr/bin/env python

import control as ctrl
import matplotlib.pyplot as mpl
import numpy as np

#  Parametros de la simulacion
DT = 0.001; Ttotal = 10; N = int(Ttotal/DT)

# Modelo de la planta
P = ctrl.tf([1],[1,2,0])

# Modelo del primer Controlador
#Kp = 2; Kd = 3; Ki = 0.000000001; pd = 1
#integ = ctrl.tf ([Ki],[1,0])
#deriv = ctrl.tf ([Kd, Kp], [1,pd])
#C = ctrl.parallel (integ, deriv)

# Modelo del Controlador
Kp = 4; Kd = 2; Ki = .1
integ = ctrl.tf ([Ki],[1,0])
deriv = ctrl.tf ([Kd, 0], [0.1,1])
prop  = Kp

# Interconección del controlador
C = ctrl.parallel (deriv + prop, integ)

#derivPuro = ctrl.tf ([Kd, Kp], [0,1])

# Serie del Controlador y la Planta
l = ctrl.series (C,P)
# Realimentación Unitaria
sys = ctrl.feedback(l,1)

# Respuesta al escalón unitario
y,t = ctrl.matlab.step(sys, T = np.arange(0, Ttotal, DT) )

# Gráfica del escalón unitario
#mpl.plot(t,y)
#mpl.show()



#print y.shape, t.shape

#mag, phase, omega = bode(C)
#mpl.plot(omega,mag)
#mpl.show()

print C

print integ

print deriv


