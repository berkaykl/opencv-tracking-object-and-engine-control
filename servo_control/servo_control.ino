#include <Servo.h>

Servo servo1;
Servo servo2;
int servo1pin = 9;
int servo2pin = 10;

void setup() {
  Serial.begin(9600);
  servo1.attach(servo1pin);
  servo2.attach(servo2pin);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    int commaIndex = data.indexOf(',');

    if (commaIndex > 0) {
      String xVal = data.substring(0, commaIndex);
      
      String yVal = data.substring(commaIndex + 1);

      int xPos = xVal.toInt();
      int yPos = yVal.toInt();
      
      servo1.write(map(xPos, 0, 640, 0, 180));
      servo2.write(map(yPos, 0, 480, 0, 180));
    }
  }
}
