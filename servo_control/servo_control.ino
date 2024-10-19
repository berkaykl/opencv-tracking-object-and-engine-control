#include <Servo.h>

Servo servo1;
int servo1pin = 9;
int gelenDeger;
int deger;


void setup() {
  Serial.begin(9600);
  servo1.attach(servo1pin);
}

void loop() {
  if(Serial.available() > 0) {
    gelenDeger = Serial.parseInt();
    deger = map(gelenDeger, 0, 480, 0, 180);
    servo1.write(deger);
  }
}
