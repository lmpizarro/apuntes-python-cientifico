# -*- coding: utf-8 -*-

from control.matlab import *    # Load the controls systems library


# Modelo del Controlador
Kp = 60; Kd = 10; Ki = 45; Td = 0.1
integ = tf ([Ki],[1,0])
deriv = tf ([Kd, 0], [Td,1])
prop  = Kp

# Interconección del controlador
C = parallel (deriv + prop, integ)

'''

The effects of each of controller parameters, Kp, Kd, and Ki on a closed-loop system 

http://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID

CL RESPONSE |  RISE TIME    |   OVERSHOOT |  SETTLING TIME | S-S ERROR 

Kp          |  Decrease     |   Increase  |  Small Change  | Decrease

Ki          |  Decrease     |   Increase  |  Increase      | Eliminate

Kd          |  Small Change |  Decrease   |  Decrease      | No Change 
'''
