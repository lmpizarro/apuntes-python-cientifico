# -*- coding: utf-8 -*-

#!/usr/bin/env python

import matplotlib.pyplot as mpl
import  numpy            as np
import control           as ctrl
import closedLoop        as cl
import eulerModified     as em

# Matrices de Controlador y Planta
#
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


  def generator(self, n):
    for j in range (n):
      self.eulController.iteration()
      self.eulPlant.iteration()
      self.y = self.eulPlant.yk
      self.e = xref - self.y
      self.eulController.uk = self.e


      #self.eulPlant.uk = self.eulController.yk
      self.eulPlant.uk = self.limiter (self.eulController.yk)
      

      mesg = {'outs':[self.y[0,0], self.e[0,0], self.eulPlant.uk[0,0]]}
      # self.y  y,   self.e  e,  self.eulPlant.uk  u,

      yield  mesg

if __name__ == "__main__":

  N = cl.N; limite = 25
  sim = simulador (cl.C, cl.P, cl.DT, limite)
  gen = sim.generator (N)

  t = np.zeros(N); y = np.zeros(N); e = np.zeros(N); u = np.zeros(N); ec = np.zeros(N)

  i = 0
  for data in gen: 
    t[i] = i * cl.DT 
    y[i] = data['outs'][0]
    e[i] = data['outs'][1]
    u[i] = data['outs'][2]
    i +=1

  # representación gráfica de la salida, error y el actuador
  mpl.plot(t,y, label='salida'); mpl.legend(loc='upper right')
  mpl.plot(t,e, label='error', color='green'); mpl.legend(loc='upper right')
  mpl.plot(t,u, label='actuacion', color='red'); mpl.legend(loc='upper right')
  mpl.show()

  # representación gráfica de la salida calculada por scipy y euler modificado
  mpl.plot(cl.t,cl.y, label='y scipy'); mpl.legend(loc='upper right')
  mpl.plot(t,y, label='y euler modificado'); mpl.legend(loc='upper right')
  mpl.show()
 
  # cálculo del error 
  for i in range (0,N):
    ec[i] = cl.y[i] - y[i]
 
  # representación gráfica del error
  mpl.plot(t, ec, label='error calc'); mpl.legend(loc='upper right')
  mpl.show()

  # cálculo del error porcentual
  for i in range (0,N):
    ec[i] = 100*ec[i]/(cl.y[i] + 1e-10)

  # representación gráfica del error porcentual
  mpl.plot(t, ec, label='error % calc'); mpl.legend(loc='upper right')
  mpl.show()
