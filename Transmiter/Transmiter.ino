#include <VirtualWire.h>
 
#define led_pin 11
#define transmit_pin 10
#define numOfValueRec 6 
#define digitsPerValRec 1
int valsRec[numOfValueRec];
int stringLength= numOfValueRec * digitsPerValRec +1; 
int counter =0;
bool counterStart= false;
String receivedString;

void receieveData(){
  while(Serial.available()){
    char c = Serial.read();
    // serial transmission from python starts with $
    if( c == '$'){
      counterStart=true;
    }
    // start receiving data from PC
    if(counterStart){
      if(counter<stringLength){
        receivedString=String(receivedString+c);
        counter++;
      }
      if (counter>=stringLength) {
        char msg[6];
        receivedString.toCharArray(msg, receivedString.length() + 1); // change string to char array
        vw_send((uint8_t *)msg, strlen(msg));// sending data to receiver 
        vw_wait_tx();
        // reset buffor
        receivedString=""; 
        counter=0; 
        counterStart=false;
      }
    }
  }
}


void setup() {
  Serial.begin(9600);
  vw_set_tx_pin(transmit_pin);
    vw_setup(2000);
}

void loop() {
  receieveData();
}
