//How to change pwm frequency
//https://www.etechnophiles.com/change-frequency-pwm-pins-arduino-uno/


//Program to run a brushless motor in open loop mode
//By Juan Pablo Angulo, modificado por Francisco Arcos
//email: juanpablocanguro@hotmail.com
//Use a Power Stage, such as AO4606 to drive the 3 coils of your motor.
//Can be run on a board such as https://www.ebay.com/itm/124316900944
//Arduino forum thread: https://forum.arduino.cc/index.php?topic=672887.0

const int potPin = A1;  // INPUT pot control for speed or position

int sensorPin = A2; //final de carrera

//use ports 9, 10, 11 
const int motorPin1 =9;
const int motorPin2 =10;
const int motorPin3 =11;

// Variables
int pwmSin[] = {127,110,94,78,64,50,37,26,17,10,4,1,0,1,4,10,17,26,37,50,64,78,94,110,127,144,160,176,191,204,217,228,237,244,250,253,255,253,250,244,237,228,217,204,191,176,160,144,127}; // array of PWM duty values for 8-bit timer - sine function
int currentStepA=0; //initial pointer at 0   degrees for coil A
int currentStepB=16;//initial pointer at 120 degrees for coil B
int currentStepC=32;//initial pointer at 240 degrees for coil C
int pos;
unsigned long previusMillis = 0;
unsigned long currentMillis;
const long ts = 2; //tiempo de muestreo en milisegundos 


//SETUP
void setup() {
  Serial.begin(250000);
//next commands will change the PWM frequency, so the annoying sound generated can be moved above human ear capability.
  TCCR0B = TCCR0B & 0b11111000 | 0x03 ;// changing this will also affect millis() and delay(), better to leave it default (0x03).
  //TCCR1B = TCCR1B & 0b11111000 | 0x01; // set PWM frequency @ 31250 Hz for Pins 9 and 10, (0x03 is default value, gives 490 Hz).
  //TCCR2B = TCCR2B & 0b11111000 | 0x01; // set PWM frequency @ 31250 Hz for Pins 11 and 3, (0x03 is default value, gives 490 Hz).

  TCCR1B = TCCR1B & 0b11111000 | 0x01; // set PWM frequency @ 31250 Hz for Pins 9 and 10, (0x03 is default value, gives 490 Hz).
  TCCR2B = TCCR2B & 0b11111000 | 0x01; // set PWM frequency @ 31250 Hz for Pins 11 and 3, (0x03 is default value, gives 490 Hz).
  
  ICR1 = 255 ; // 8 bit resolution for PWM
 
  pinMode(potPin, INPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
}
 
void loop() {
  move();
}
  
void move()
{
  //Read pot value
  int sensorValue = analogRead(potPin);

  int final_carrera = analogRead(sensorPin);
  
  Serial.print(sensorValue);
  Serial.print(",");
  Serial.print(0);
  Serial.print(",");
  Serial.println(1023); 
  delay(2);

  //Serial.print(pwmSin[currentStepA]);
  //Serial.print(",");
  //Serial.print(pwmSin[currentStepB]);
  //Serial.print(",");
  //Serial.println(pwmSin[currentStepC]);
  //Serial.print(",");

  if(sensorValue>200 && sensorValue<500 && final_carrera < 500){

  currentMillis = millis();
  if(currentMillis - previusMillis >= ts){
    previusMillis = currentMillis;
          
    currentStepA = currentStepA + 1;  //Add 1 to make the motor move step by step.
    currentStepB = currentStepA + 16; //add 120 deg of phase to whatever position StepA is. 
    currentStepC = currentStepA + 32; //add 240 deg of phase to whatever position StepA is.
  
    currentStepA = currentStepA%48; //I used remainder operation or modulo to "wrap" the values between 0 and 47
    currentStepB = currentStepB%48;
    currentStepC = currentStepC%48;  

    analogWrite(motorPin1, pwmSin[currentStepA]*0.5); //multipliying by 0.5 to reduce output torque to half as its being supplied with 12V and can get pretty warm. make this 1 if supply is 5V or if you know what you are doing ;)
    analogWrite(motorPin2, pwmSin[currentStepB]*0.5);
    analogWrite(motorPin3, pwmSin[currentStepC]*0.5);
    
  }
  }

  if(sensorValue>600 && sensorValue<900){

  currentMillis = millis();
  if(currentMillis - previusMillis >= ts){
    previusMillis = currentMillis;
          
    currentStepA = currentStepA + 1;  //Add 1 to make the motor move step by step.
    currentStepB = currentStepA + 16; //add 120 deg of phase to whatever position StepA is. 
    currentStepC = currentStepA + 32; //add 240 deg of phase to whatever position StepA is.
  
    currentStepA = currentStepA%48; //I used remainder operation or modulo to "wrap" the values between 0 and 47
    currentStepB = currentStepB%48;
    currentStepC = currentStepC%48;  

    analogWrite(motorPin1, pwmSin[currentStepA]*0.5); //multipliying by 0.5 to reduce output torque to half as its being supplied with 12V and can get pretty warm. make this 1 if supply is 5V or if you know what you are doing ;)
    analogWrite(motorPin2, pwmSin[currentStepC]*0.5);
    analogWrite(motorPin3, pwmSin[currentStepB]*0.5);
    
  }
  }
 ////////////

   
//Serial.println(currentStepA);
  //pos=pulseIn(encoder,HIGH);
  //Serial.println(pos);
}
