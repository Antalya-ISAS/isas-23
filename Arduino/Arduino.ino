/// ANTALYA ISAS ///
#include <Servo.h>
String incomingByte ;

Servo frri, frle, reri, rele, frriup, frleup, reriup, releup;
int frri_speed, frle_speed, reri_speed, rele_speed, frriup_speed, frleup_speed, reriup_speed, releup_speed = 1500;
int condition1, condition2, condition3, condition4;

#define mx 1940 //max 2000 oluyor escler 1000-2000 arası calisir
#define mn 1060

//#define TERSONSAG
//#define TERSONSOL
//#define TERSARKASOL
//#define TERSARKASAG

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  frri.attach(10, 1000, 2000);// Doğru
  frle.attach(2, 1000, 2000);// Ters
  reri.attach(4, 1000, 2000);// Doğru
  rele.attach(13, 1000, 2000);// Ters
  frriup.attach(11, 1000, 2000);// Doğru
  frleup.attach(3, 1000, 2000);// Doğru
  reriup.attach(5, 1000, 2000);// Doğru
  releup.attach(12, 1000, 2000);// Ters
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

void  loop() {
  while (!Serial.available());
  incomingByte = Serial.readStringUntil('\n');
  if (incomingByte.length() == 32) {
    convertAllToInt();
    Serial.print("3D Teleop Drive Mode");
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
  if (incomingByte.length() == 16) {
    convertAllToInt();
    Serial.print("2D Teleop Drive Mode");
    frri.writeMicroseconds(frri_speed);
    frle.writeMicroseconds(frle_speed);
    reri.writeMicroseconds(reri_speed);
    rele.writeMicroseconds(rele_speed);
    delay(5);
  }
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