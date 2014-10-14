import serial
import time
import planta as planta
import redis             as redis
import json              as json
import threading         as threading


redis = redis.Redis('localhost')
toRedisOut = "estadoHIL"
fromRedisIn   = "refHIL"
xref = 1.0

import random

def digitalToFloat (d):
    nf =  0.000976*d - 2;
    if nf > 2: nf= 2.0
    if nf < -2: nf = -2.0
    return nf

def floatToDigital(f):
    nd = int((4095/4)*f + 2048)
    if nd > 4095: nd= 4095
    if nd < 0: nd = 0
    return nd
#
#   Test
#
def genRandomPairs ():
  y = random.randint(0,4095)
  ref = random.randint(0,4095)


  yFloat = digitalToFloat (y)
  refFloat = digitalToFloat (ref)
  error = refFloat - yFloat
  #print "valor esperado", floatToDigital(error), refFloat, yFloat
  
  return (y,ref)



class simulador ():
  
  def __init__ (self, serialPort):
      global xref
      self.planta = planta.Integral(0.0)	
      self.planta.ref = xref 
      self.iteration = 0
      self.ser = serialPort
      self.next_call = time.time()
      self.delay = .5 

  def armaMsg (self, y, ref):
	return '#'+str(y).zfill(4)+','+str(ref).zfill(4) +'!'
  #
  #  send message to Arduino
  #
  def sendMessageToController (self, msg):
    self.ser.flushInput()
    self.ser.write(str(msg))

  def  worker (self):

       print "simulador worker"
       while 1:
         msgFromController = self.ser.readline().strip()
         if (msgFromController=="#estadoPlanta!"):
           self.planta.ref = xref 
           # y, ref
           # Tests
           #(a,b) = genRandomPairs()
           # envia (y , ref)
           self.iteration += 1 
           myTime = time.time()
        
           estado = {'outs':[self.planta.out, self.planta.ref - self.planta.out, self.planta.actu], 'ts':myTime, 'msg_id':self.iteration}
           redis.publish (toRedisOut, json.dumps(estado))
           print "estado planta: ", estado
        
           msg = self.armaMsg(floatToDigital(self.planta.out), floatToDigital(self.planta.ref))
           self.sendMessageToController (msg)

         else: 
           try:
             actu = msgFromController.strip('#').strip('!')
             self.planta.iterate( digitalToFloat(int(actu)))
           except:
             pass


def callback():
        global xref
	#r = redis.client.StrictRedis()
	sub = redis.pubsub()
	sub.subscribe(fromRedisIn)
	while True:
		for m in sub.listen():
                        xref = float (m['data']) #'Recieved: {0}'.format(m['data'])
			print "xref: ", xref

def commandFromHMI():
	t = threading.Thread(target=callback)
	t.setDaemon(True)
	t.start()

if __name__ == '__main__':
  # configure the serial connections 
  ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    #parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 1
  )

  # para buscar el valor de la referencia 
  commandFromHMI ()



  sim = simulador (ser)
  sim.worker ()



