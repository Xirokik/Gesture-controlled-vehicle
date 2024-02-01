#include <VirtualWire.h>

#define receive_pin 11
#define en1 8
#define en2 9
#define en3 6
#define en4 7
#define righttrack 3
#define lefttrack 5
int value_left, value_right; // value of decoded signals
int left = 0; //pwm for left track
int right = 0; // pwm for right track
void setup() {
  pinMode(lefttrack, OUTPUT);
  pinMode(en3, OUTPUT);
  pinMode(en4, OUTPUT);
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);
  pinMode(righttrack, OUTPUT);
  digitalWrite(en3, LOW);
  digitalWrite(en4, LOW);
  digitalWrite(en2, LOW);
  digitalWrite(en1, LOW);
  vw_set_rx_pin(receive_pin);
  vw_setup(2000);
  vw_rx_start();  // receive data begin
}
void loop() {
  delay(50);
  uint8_t buf[7]; //buffor
  uint8_t buflen = 7; // buffor lenght

  if (vw_get_message(buf, &buflen))  // receive data
  {
    String wiad;
    for (int i = 0; i < buflen; i++)  // data from receiver
    {
      wiad += char(buf[i]);
    }
    // decode signals
    value_left = wiad.substring(1, 4).toInt();
    value_right = wiad.substring(4, 7).toInt();
  }
  // drive backward right track
  if (value_right < 400 && value_right > 300) {

    right = value_right - 150;
    if (right > 150 && right < 250) {
      // Serial.println(right);
      analogWrite(righttrack, right);
      digitalWrite(en1, HIGH);
      digitalWrite(en2, LOW);
    }
  }
  // drive forward right track
  else if (value_right < 250 && value_right > 150) {
    right = 400 - value_right;
    if (right > 150 && right < 250) {
      analogWrite(righttrack, right);
      digitalWrite(en1, LOW);
      digitalWrite(en2, HIGH);
    }
  } else {
    digitalWrite(en1, LOW);
    digitalWrite(en2, LOW);
  }
  // drive backward left track
  if (value_left < 400 && value_left > 300) {
    left = value_left - 150;
    if (left > 150 && left < 250) {
      analogWrite(lefttrack, left);
      digitalWrite(en3, HIGH);
      digitalWrite(en4, LOW);
    }
  }
  // drive forward left track
  else if (value_left < 250 && value_left > 150) {
    left = 400 - value_left;
    if (left > 150 && left < 250) {
      analogWrite(lefttrack, left);
      digitalWrite(en3, LOW);
      digitalWrite(en4, HIGH);
    }
  } else {
    digitalWrite(en3, LOW);
    digitalWrite(en4, LOW);
  }
}