#include <Arduino.h>
#include <math.h>
#include <analogWrite.h>

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(115200);

}
int rojo = 11;
int verde = 9;
int azul = 10;

double R;
double G;
double B;

// the loop function runs over and over again forever
void loop() {
  for(double i = 0;i<6.28;i+=0.01){
    R = cos(i)+1;
    G = cos(i+2.1)+1;
    B = cos(i+4.2)+1;

    R = int((R*85)+85);
    G = int(G*127);
    B = int(B*127);

    Serial.print(R);Serial.print(' ');
    Serial.print(G);Serial.print(' ');
    Serial.println(B);

    analogWrite(rojo,R);
    analogWrite(verde,G);
    analogWrite(azul,B);

  } 
}