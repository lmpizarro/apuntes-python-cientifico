/*
  Serial Call and Response
 Language: Wiring/Arduino
 
 This program sends an ASCII A (byte of value 65) on startup
 and repeats that until it gets some data in.
 Then it waits for a byte in the serial port, and 
 sends three sensor values whenever it gets a byte in.
 
 Thanks to Greg Shakar and Scott Fitzgerald for the improvements
 
   The circuit:
 * potentiometers attached to analog inputs 0 and 1 
 * pushbutton attached to digital I/O 2
 
 Created 26 Sept. 2005
 by Tom Igoe
 modified 24 April 2012
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SerialCallResponse

 */

int firstSensor = 0;    // first analog sensor
int inByte = 0;         // incoming serial byte

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}

/*
0     ->  -2
4095  ->  2

(4/4095)*(r) - 2
*/
float digitalToFloat (int r){
    return 0.000976*(r) - 2;
} 


int floatToDigital(float f){
   return int((4095/4)*f + 2048);
}

float kp = 1.0;
float pid (float error){
    float calc;

    calc = kp * error;

    if (calc >2) calc =2;  
    if (calc < -2) calc = -2;
    return calc;
}

int controller (int youtInt, int refInt){
   int actuInt;
   float errorFloat;
   float actu;

   float refFloat = digitalToFloat(refInt);
   float youtFloat = digitalToFloat(youtInt);

   errorFloat = refFloat - youtFloat;
   actu = pid (errorFloat);
   actuInt = floatToDigital (actu);

   return actuInt;
}


String msgFromMaster = "";
int recFlag, yOut, ref, error, act;
String yOutString, refString;
void recMsgFromMaster (){
  char iC;
  
  recFlag = 0;
  while(Serial.available()>0)
    {
       iC = Serial.read();
       if (iC == '#')msgFromMaster = "";
       msgFromMaster += iC;
         if (iC == '!') {
            if (msgFromMaster.length() == 11){
               //Serial.println("#actuacion!");
	       yOutString = msgFromMaster.substring(1,5);
	       refString = msgFromMaster.substring(6,10);
               Serial.println(msgFromMaster);
               yOut = yOutString.toInt();
               ref = refString.toInt();

               act = controller (yOut, ref);

               Serial.println('#' + String(act) + '!');
	    } else 
	      msgFromMaster ="";
         }
    }

}

void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  pinMode(2, INPUT);   // digital sensor is on digital pin 2
  //establishContact();  // send a byte to establish contact until receiver responds 
}

void loop()
{
    Serial.println("#data!");
    delay(100);
    recMsgFromMaster ();
    delay(900);
}

