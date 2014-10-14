/*
  program: controller.ino 
  Language: Wiring/Arduino
  Author: lmpizarro 

 */

int firstSensor = 0;    // first analog sensor
int inByte = 0;         // incoming serial byte

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

float sum_error;
float old_error = 0;
float kp = .5;
float kd = .75;
float ki = .5;

float pid (float error){
    float calc;
    

    calc = kp * error + kd*(error - old_error) + ki * sum_error;
    old_error = error;
    sum_error = sum_error + error;

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
int recFlag, yOut, ref, error, actuInt;
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
	       yOutString = msgFromMaster.substring(1,5);
	       refString = msgFromMaster.substring(6,10);
               yOut = yOutString.toInt();
               ref = refString.toInt();

               actuInt = controller (yOut, ref);

               Serial.println('#' + String(actuInt) + '!');
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
}

void loop()
{
    Serial.println("#estadoPlanta!");
    delay(100);
    recMsgFromMaster ();
    delay(900);
}

