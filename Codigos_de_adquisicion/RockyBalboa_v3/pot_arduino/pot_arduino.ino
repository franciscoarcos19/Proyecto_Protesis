unsigned long previusMillis = 0;
unsigned long currentMillis;
const long ts = 50; //tiempo de muestreo en milisegundos 
int number1, number2, number3, number4;
int i;
char result[50];
int a = 10;
int b = 15;
char lectura[50];
int analogPin0 = A0;
int analogPin1 = A1;
int analogPin2 = A2;
int analogPin3 = A3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sprintf(result, "%d,%d", a, b);
  //Serial.println("Lecturas de sensores");
}

void loop() {
  // put your main code here, to run repeatedly:
  currentMillis = millis();

  if(currentMillis - previusMillis >= ts){
    i=i+1;
    //Serial.println(i);

    delay(1);
    number1 = analogRead(analogPin0); 
    delay(1);
    number2 = analogRead(analogPin1);
    delay(1);
    number3 = analogRead(analogPin2);
    delay(1);
    number4 = analogRead(analogPin3);
    
    
    sprintf(lectura, "%d,%d,%d,%d", number1, number2, number3, number4);
    Serial.println(lectura);
    previusMillis = currentMillis;
    
  }

}
