# -*- coding: utf-8 -*-

#!/usr/bin/env python

import numpy             as np
import control           as ctrl
import matplotlib.pyplot as mpl

#  Parametros de la simulacion
DT = 0.001; Ttotal = 10; N = int(Ttotal/DT)

# Modelo de la planta
P = ctrl.tf([1],[1,2,0])

# Modelo del Controlador
Kp = 4; Kd = 2; Ki = .1; pd = 1
integ = ctrl.tf ([Ki],[1,0])
deriv = ctrl.tf ([Kd, 1], [0.1,1])
prop  = Kp
C = ctrl.parallel (deriv + prop, integ)

Ac,Bc,Cc,Dc = ctrl.matlab.ssdata(C)
print deriv, integ, C

l = ctrl.series (C,P)
sys = ctrl.feedback(l,1)

y,t = ctrl.matlab.step(sys, T = np.arange(0, Ttotal, DT) )
mpl.plot(t,y, label='C*Planta CL')

#print y.shape, t.shape
#mag, phase, omega = bode(C)
#mpl.plot(omega,mag)
#mpl.show()


sys1 = ctrl.feedback(P,1)
y,t = ctrl.matlab.step(sys1, T = np.arange(0, Ttotal, DT) )
mpl.plot(t,y, label='Planta CL'); mpl.legend(loc='lower right')

sys2 = ctrl.feedback(prop*P,1)
y,t = ctrl.matlab.step(sys2, T = np.arange(0, Ttotal, DT) )
mpl.plot(t,y, label='prop*Planta CL' ); mpl.legend(loc='lower right')

sys3 = ctrl.feedback((deriv + prop)*P,1)
y3,t = ctrl.matlab.step(sys3, T = np.arange(0, Ttotal, DT) )
mpl.plot(t,y3, label='(deriv+ prop)*Planta CL'); mpl.legend(loc='lower right')

e = np.zeros(N)
i = 0
for d in  y3:
  e[i] = y[i] - d 
  i += 1	


mpl.show()

mpl.plot(t,e, label='error CL PID vs CL PD'); mpl.legend(loc='lower right')
mpl.show()
