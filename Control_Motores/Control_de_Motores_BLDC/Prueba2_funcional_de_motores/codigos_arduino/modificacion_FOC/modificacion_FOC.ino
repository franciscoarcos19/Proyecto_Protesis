//Program to run a brushless motor in open loop mode
//By Juan Pablo Angulo modificado por Francisco Arcos
//email: juanpablocanguro@hotmail.com
//Use a Power Stage, such as AO4606 to drive the 3 coils of your motor.
//Can be run on a board such as https://www.ebay.com/itm/124316900944
//Arduino forum thread: https://forum.arduino.cc/index.php?topic=672887.0

const int potPin = A1;  // INPUT pot control for speed or position
//use ports 9, 10, 11 
const int motorPin1 =9;
const int motorPin2 =10;
const int motorPin3 =11;

int sensorValue = 0;
int sentido = 1;

// Variables
int pwmSin[] = {128,132,136,140,144,148,152,156,160,163,167,171,175,178,182,186,189,193,196,199,203,206,209,212,215,218,221,223,226,228,231,233,235,237,239,241,243,245,246,247,249,250,251,252,253,253,254,254,255,255,255,255,255,254,254,253,253,252,251,250,249,247,246,245,243,241,239,237,235,233,231,228,226,223,221,218,215,212,209,206,203,199,196,193,189,186,182,178,175,171,167,163,160,156,152,148,144,140,136,132,128,124,120,116,112,108,104,100,96,93,89,85,81,78,74,70,67,63,60,57,53,50,47,44,41,38,35,33,30,28,25,23,21,19,17,15,13,11,10,9,7,6,5,4,3,3,2,2,1,1,1,1,1,2,2,3,3,4,5,6,7,9,10,11,13,15,17,19,21,23,25,28,30,33,35,38,41,44,47,50,53,57,60,63,67,70,74,78,81,85,89,93,96,100,104,108,112,116,120,124,128}; // array of PWM duty values for 8-bit timer - sine function

int desfase = 68;

int currentStepA=0; //initial pointer at 0   degrees for coil A
int currentStepB=desfase;//initial pointer at 120 degrees for coil B
int currentStepC=desfase*2;//initial pointer at 240 degrees for coil C
int pos;

//SETUP
void setup() {
  Serial.begin(115200);
//next commands will change the PWM frequency, so the annoying sound generated can be moved above human ear capability.
  TCCR0B = TCCR0B & 0b11111000 | 0x03 ;// changing this will also affect millis() and delay(), better to leave it default (0x03).
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
  currentStepA = currentStepA + 1;  //Add 1 to make the motor move step by step.
  currentStepB = currentStepA + desfase; //add 120 deg of phase to whatever position StepA is. 
  currentStepC = currentStepA + desfase*2; //add 240 deg of phase to whatever position StepA is.
  
  currentStepA = currentStepA%201; //I used remainder operation or modulo to "wrap" the values between 0 and 47
  currentStepB = currentStepB%201;
  currentStepC = currentStepC%201;

  analogWrite(motorPin1, pwmSin[currentStepA]*1); //multipliying by 0.5 to reduce output torque to half as its being supplied with 12V and can get pretty warm. make this 1 if supply is 5V or if you know what you are doing ;)
  analogWrite(motorPin2, pwmSin[currentStepC]*1);
  analogWrite(motorPin3, pwmSin[currentStepB]*1);

  //Following send data to PLX-DAQ macro for Excel
  //Serial.print("DATA,");
  //Serial.print(pwmSin[currentStepA]);
  //Serial.print(","); 
  //Serial.print(pwmSin[currentStepB]);
  //Serial.print(","); 
  //Serial.println(pwmSin[currentStepC]);

   //Read pot value
  //int sensorValue = analogRead(potPin); 

  
  if(sensorValue == 500){
    sentido = 0;
  }
  if(sensorValue == 0){
    sentido = 1;
  }
  if(sentido == 1){
    sensorValue = sensorValue + 1;
  }
  if(sentido == 0){
    sensorValue = sensorValue - 1;
  }
  //Serial.println(sensorValue);

  //delay(5);

// Select ONLY ONE of the following lines for constant speed, speed control or position control:

  //This will give you constant speed, remember if you changed TCCR0B to 0x01, then delay(64000) = ~1 second
  //delay(5); 

  //This will give you open loop speed control with the potentiometer
  //delay(sensorValue/10);

  //This will give you open loop position control with the potentiometer
  currentStepA = sensorValue/10; //divide by a number to affect the ratio of pot position : motor position

 ////////////

   
//Serial.println(currentStepA);
  //pos=pulseIn(encoder,HIGH);
  //Serial.println(pos);
}
