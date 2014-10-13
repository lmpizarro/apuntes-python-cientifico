import serial
import time
import json
import string

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
#
# receive message from Arduino
#
def receiveMessage ():  
  message = ""
  c= ser.read(1)
  print c

  while 1:
    if  c!="\n":
      message +=c
    else: 
      return message

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



def genRandomPairs ():
  y = random.randint(0,4095)
  ref = random.randint(0,4095)
  yFloat = digitalToFloat (y)
  refFloat = digitalToFloat (ref)
  error = refFloat - yFloat
  print "error", floatToDigital(error), refFloat, yFloat
  
  return (y,ref)


if __name__ == '__main__':
  while 1:
    val = ser.readline().strip()
    if (val=="#data!"):
      print val
      # y, ref
      (a,b) = genRandomPairs()
      msg = armaMsg(a,b)
      sendMessage (msg)
    else: #if val=="#actuacion!":
      print val	    
 
