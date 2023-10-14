/// ANTALYA ISAS ///
#include <Servo.h>
String incomingByte ;

Servo frri, frle, reri, rele, frriup, frleup, reriup, releup;
int frri_speed, frle_speed, reri_speed, rele_speed, frriup_speed, frleup_speed, reriup_speed, releup_speed = 1500;
int condition1, condition2, condition3, condition4;

#define maxdeger 1940 //max 2000 oluyor escler 1000-2000 arası calisir
#define mindeger 1060

//#define TERSONSAG
//#define TERSONSOL
//#define TERSARKASOL
//#define TERSARKASAG

void setup() {
  Serial.begin(115200);
  frri.attach(3, 1000, 2000);// Doğru
  frle.attach(8, 1000, 2000);// Ters
  reri.attach(5, 1000, 2000);// Doğru
  rele.attach(6, 1000, 2000);// Ters
  frriup.attach(9, 1000, 2000);// Doğru
  frleup.attach(2, 1000, 2000);// Doğru
  reriup.attach(7, 1000, 2000);// Doğru
  releup.attach(4, 1000, 2000);// Ters
  frri.writeMicroseconds(1500);
  frle.writeMicroseconds(1500);
  reri.writeMicroseconds(1500);
  rele.writeMicroseconds(1500);
  frriup.writeMicroseconds(1500);
  frleup.writeMicroseconds(1500);
  reriup.writeMicroseconds(1500);
  releup.writeMicroseconds(1500);
  delay(2000);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    if (incomingByte.length() == 16) {
      Serial.write("2D Teleop Drive Mode");
      convertAllToInt();
      frri.writeMicroseconds(frri_speed);
      frle.writeMicroseconds(frle_speed);
      reri.writeMicroseconds(reri_speed);
      rele.writeMicroseconds(rele_speed);
      delay(5);
    }
    else if (incomingByte.length() == 32) {
      incomingByte = Serial.readStringUntil('\n');
      convertAllToInt();
      frri.writeMicroseconds(frri_speed);
      frle.writeMicroseconds(frle_speed);
      reri.writeMicroseconds(reri_speed);
      rele.writeMicroseconds(rele_speed);
      frriup.writeMicroseconds(frriup_speed);
      frleup.writeMicroseconds(frleup_speed);
      reriup.writeMicroseconds(reriup_speed);
      releup.writeMicroseconds(releup_speed);
      delay(5);
    }
    else {
      if (incomingByte == "forward") {
        frri.writeMicroseconds(mx);
        frle.writeMicroseconds(mn);
        reri.writeMicroseconds(mx);
        rele.writeMicroseconds(mn);
        delay(5);
        Serial.write("Driving forward");
      }
      else if (incomingByte == "back") {
        frri.writeMicroseconds(mn);
        frle.writeMicroseconds(mx);
        reri.writeMicroseconds(mn);
        rele.writeMicroseconds(mx);
        delay(5);
        Serial.write("Driving back");
      }
      else if (incomingByte == "right" ) {
        frri.writeMicroseconds(mn);
        frle.writeMicroseconds(mn);
        reri.writeMicroseconds(mn);
        rele.writeMicroseconds(mn);
        delay(5);
        Serial.write("Driving right");
      }
      else if (incomingByte == "left") {
        frri.writeMicroseconds(mx);
        frle.writeMicroseconds(mx);
        reri.writeMicroseconds(mx);
        rele.writeMicroseconds(mx);
        delay(5);
        Serial.write("Driving left");
      }
      else if (incomingByte == "off" ) {
        frri.writeMicroseconds(1500);
        frle.writeMicroseconds(1500);
        reri.writeMicroseconds(1500);
        rele.writeMicroseconds(1500);
        delay(5);
        Serial.write("Driving mode is off");
      }
      else if (incomingByte == "up" ) {
        frriup.writeMicroseconds(mx);
        frleup.writeMicroseconds(mx);
        reriup.writeMicroseconds(mx);
        releup.writeMicroseconds(mn);
        delay(5);
        Serial.write("Driving up");
      }
      else if (incomingByte == "down" ) {
        frriup.writeMicroseconds(mn);
        frleup.writeMicroseconds(mn);
        reriup.writeMicroseconds(mn);
        releup.writeMicroseconds(mx);
        delay(5);
        Serial.write("Driving down");
      }
      else {
        Serial.write("invald input");
      }
    }
  }
}

void driveMotor2D(int frri_speed, int frle_speed, int reri_speed, int rele_speed) {
  frri_speed = constrain(frri_speed, 1000, 2000);
  frle_speed = constrain(frle_speed, 1000, 2000);
  reri_speed = constrain(reri_speed, 1000, 2000);
  rele_speed = constrain(rele_speed, 1000, 2000);

  frri.writeMicroseconds(frri_speed);
  frle.writeMicroseconds(frle_speed);
  reri.writeMicroseconds(reri_speed);
  rele.writeMicroseconds(rele_speed);
}

void driveMotor2DUp(int frriup_speed, int frleup_speed, int reriup_speed, int releup_speed) {
  frriup_speed = constrain(frriup_speed, 1000, 2000);
  frleup_speed = constrain(frleup_speed, 1000, 2000);
  reriup_speed = constrain(reriup_speed, 1000, 2000);
  releup_speed = constrain(releup_speed, 1000, 2000);

  frriup.writeMicroseconds(frriup_speed);
  frleup.writeMicroseconds(frleup_speed);
  reriup.writeMicroseconds(reriup_speed);
  releup.writeMicroseconds(releup_speed);
}

void driveMotor3D(int frri_speed, int frle_speed, int reri_speed, int rele_speed, int frriup_speed, int frleup_speed, int reriup_speed, int releup_speed) {
  frriup_speed = constrain(frriup_speed, 1000, 2000);
  frleup_speed = constrain(frleup_speed, 1000, 2000);
  reriup_speed = constrain(reriup_speed, 1000, 2000);
  releup_speed = constrain(releup_speed, 1000, 2000);
  frri_speed = constrain(frri_speed, 1000, 2000);
  frle_speed = constrain(frle_speed, 1000, 2000);
  reri_speed = constrain(reri_speed, 1000, 2000);
  rele_speed = constrain(rele_speed, 1000, 2000);

  frri.writeMicroseconds(frri_speed);
  frle.writeMicroseconds(frle_speed);
  reri.writeMicroseconds(reri_speed);
  rele.writeMicroseconds(rele_speed);
  frriup.writeMicroseconds(frriup_speed);
  frleup.writeMicroseconds(frleup_speed);
  reriup.writeMicroseconds(reriup_speed);
  releup.writeMicroseconds(releup_speed);
}

void convertAllToInt() {
  if (incomingByte.length() == 32) {
    frri_speed = (incomingByte.substring(0, 4)).toInt();
    frle_speed = (incomingByte.substring(4, 8)).toInt();
    reri_speed = (incomingByte.substring(8, 12)).toInt();
    rele_speed = (incomingByte.substring(12, 16)).toInt();
    frriup_speed = (incomingByte.substring(16, 20)).toInt();
    frleup_speed = (incomingByte.substring(20, 24)).toInt();
    reriup_speed = (incomingByte.substring(24, 28)).toInt();
    releup_speed = (incomingByte.substring(28, 32)).toInt();
  }
  if (incomingByte.length() == 16) {
    frri_speed = (incomingByte.substring(0, 4)).toInt();
    frle_speed = (incomingByte.substring(4, 8)).toInt();
    reri_speed = (incomingByte.substring(8, 12)).toInt();
    rele_speed = (incomingByte.substring(12, 16)).toInt();
  }
}