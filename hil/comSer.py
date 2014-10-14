import serial
import planta as planta

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    #parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 1
)

#
#  send message to Arduino
#
def sendMessage (messS):
  ser.flushInput()
  ser.write(str(messS))

def armaMsg (y,ref):
	return '#'+str(y).zfill(4)+','+str(ref).zfill(4) +'!'

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
  #print "error", floatToDigital(error), refFloat, yFloat
  
  return (y,ref)

if __name__ == '__main__':
  planta = planta.Integral(0.0)	
  planta.ref = 1.0

  while 1:
    msgFromController = ser.readline().strip()
    if (msgFromController=="#estadoPlanta!"):
      # y, ref
      #(a,b) = genRandomPairs()
      # envia (y , ref)
      msg = armaMsg(floatToDigital(planta.out), floatToDigital(planta.ref))
      print "estado planta: ",planta.out, planta.ref
      sendMessage (msg)
    else: 
      actu = msgFromController.strip('#').strip('!')
      try:
        planta.iterate( digitalToFloat(int(actu)))
      except:
	pass
 
