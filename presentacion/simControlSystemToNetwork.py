# -*- coding: utf-8 -*-

#!/usr/bin/env python

import matplotlib.pyplot as mpl
import numpy             as np
import control           as ctrl
import closedLoop        as cl
import eulerModified     as em
# ... ... ... ... ... ... ... #
import time              as time
import redis             as redis
import json              as json
import threading         as threading


redis = redis.Redis('localhost')
redisList = "messageToSimulator"
commHMI   = "messageFromHMI"

# Valores iniciales de la simulación
#
x0c = x0p = np.matrix ([0,0]).transpose()
u0 = np.matrix ([0])
xref = np.matrix ([1])

class simulador ():
  def __init__ (self, C, P, delay, lim):
    self.C = C
    self.P = P
    self.delay = delay
    self.lim = lim
    self.i = 0
    self.next_call = time.time()
    # conversión de las funciones transferencias a
    # representación en matríces de transición de estados
    Ac,Bc,Cc,Dc = ctrl.matlab.ssdata(self.C)
    Ap,Bp,Cp,Dp = ctrl.matlab.ssdata(self.P)

    self.eulController = em.EulerModified (Ac, Bc, Cc, Dc, x0c, u0, self.delay)
    self.eulPlant = em.EulerModified (Ap, Bp, Cp, Dp, x0p, u0, self.delay)

  def limiter (self, num):
      limite = num
      if (limite[0,0] >= self.lim):
         limite [0,0] = self.lim
      elif  (limite[0,0] <= -1*self.lim):
         limite[0,0] = -1*self.lim

      return limite

  def worker(self):
    self.i = self.i + 1
    self.next_call = self.next_call + self.delay
    myTime = time.time()
    threading.Timer( self.next_call - myTime, self.worker).start()
    self.eulController.iteration()
    self.eulPlant.iteration()
    self.y = self.eulPlant.yk
    self.e = xref - self.y
    self.eulController.uk = self.e

    #self.eulPlant.uk = self.eulController.yk
    self.eulPlant.uk = self.limiter (self.eulController.yk)

    if not (self.i%200):    
       mesg = {'outs':[self.y[0,0], self.e[0,0], self.eulPlant.uk[0,0]], 'ts':myTime, 'msg_id':self.i}
       # self.y  salida del sistema
       # self.e  error, entrada al controlador 
       # self.eulPlant.uk  entrada a la planta
       redis.publish (redisList,json.dumps(mesg))
       #print  mesg, self.i
       print xref

class commandFromHMI ():

  def __init__ (self):
      self.ps_obj=redis.pubsub()
      self.ps_obj.subscribe(commHMI)

  def worker (self):
    for item in self.ps_obj.listen():
        global xref
	try:
          xref = np.matrix ([float (item['data'])])
          print xref 
	except ValueError:
	  pass	



if __name__ == "__main__":
   N = cl.N; limite = 1
   sim = simulador (cl.C, cl.P, cl.DT, limite)
   sim.worker ()

   sfh = commandFromHMI ()
   sfh.worker()
