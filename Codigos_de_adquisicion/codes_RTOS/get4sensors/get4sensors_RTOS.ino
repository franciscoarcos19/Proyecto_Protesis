#include <Arduino_FreeRTOS.h>
#define led 7
#define Pot1 A0
#define Pot2 A1
#define Pot3 A2
#define Pot4 A3

int number1, number2, number3, number4;
char lectura[50];

typedef int TaskProfiler;

TaskProfiler LedTaskProfiler;
TaskProfiler PotTaskProfiler;

void setup(){
  Serial.begin(230400);
  xTaskCreate(LedControllerTask,"Led Task", 128, NULL, 1, NULL);
  xTaskCreate(PotControllerTask,"Pot1 Task", 128, NULL, 5, NULL);
}

void LedControllerTask(void *pvParameters){
  pinMode(led, OUTPUT);
  while(1){
    digitalWrite(led, digitalRead(led)^1);
    delay(50);
  }
}

void PotControllerTask(void *pvParameters){
  while(1){
    //Serial.println("Pot1 task");
    //Serial.println(analogRead(Pot1));
    //delay(100);

    number1 = analogRead(Pot1); 
    number2 = analogRead(Pot2);
    number3 = analogRead(Pot3);
    number4 = analogRead(Pot4);
    sprintf(lectura, "%d,%d,%d,%d", number1, number2, number3, number4);
    Serial.println(lectura);

    delayMicroseconds(50);
    
  }
}

void loop(){}
