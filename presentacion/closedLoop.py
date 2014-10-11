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
Kp = 4; Kd = 2; Ki = .1; pd = 1
integ = ctrl.tf ([Ki],[1,0])
deriv = ctrl.tf ([Kd, 1], [0.1,1])
prop  = Kp
C = ctrl.parallel (deriv + prop, integ)




#derivPuro = ctrl.tf ([Kd, Kp], [0,1])

l = ctrl.series (C,P)
sys = ctrl.feedback(l,1)

y,t = ctrl.matlab.step(sys, T = np.arange(0, Ttotal, DT) )


#print y.shape, t.shape

#mag, phase, omega = bode(C)
#mpl.plot(omega,mag)
#mpl.show()

#mpl.plot(t,y)
#mpl.show()
