# Gesture-controlled-vehicle

## Descriptions
The project is a remotely controlled vehicle using gesture recognition. A Python program is responsible for hand recognition. Then the data is sent to Arduino via USART. Arduino transmits data to the microcontroller on the vehicle using a radio transmitter. The microcontroller, in my case, the second Arduino Uno R3, receives data and, based on them, controls the engines in the vehicle.

## Functionality
Appropriate positioning of the hand in the image recorded by the camera allows you to control the direction and speed of rotation of the engines in the vehicle. 

The program must recognize both hands to function properly. Otherwise it will not be possible to start the engines. Each hand controls one motor. The program includes functions that prevent the exchange of hands assigned to specific engines.

The control is quite intuitive, raising your hand causes the track to move forward. The higher hand is, the faster the engine spin. Driving backwards is similar, but the lower the hand is, the faster the motor rotates in the opposite direction. The engine does not rotate, when the hand is in the center of the recorded image.

The operating ranges are 150-250 pixels for forward driving and 300-400 pixels for backward driving. The motors do not spin when the hand is between 250 and 300 pixels.

## Library for Arduino
```
#include <VirtualWire.h>
```

## Libraries for Python
```
cvzone (version 1.5.1)
mediapipe (version 0.8.11)
pyserial (version 3.5)
```
WARNING

In order for the code to work properly, you must modify the HandTrackingModule.py file in the project.
```
def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []
```

## Components
1) Camera (I used the built-in one in the laptop)
2) 2x Arduino Uno rev 3
3) Tank chassis (I used Black gladiator chassis, 6-12V motors included)
4) Two-channel motor controller L298N
5) Cable USB-B to USB-A (to connect arduino to laptop/pc)
6) Radio module transmitter FS100A + receiver 433 MHz
7) 9v battery with Adapter plug DC 5.5 / 2.1 for Arduino
8) 6x 1,5V (AA batteries) for motors
9) Battery basket 6x1,5V (AA batteries)
10) Bunch of cables
11) Tape or glue for assembly

### Watch the project in action [here](https://youtu.be/2UdCnZrh9oA)

### Vehicle 
![IMG](https://github.com/Xirokik/Gesture-controlled-vehicle/blob/main/Project's%20files/Vehicle.jpg)

### Test stand
![IMG](https://github.com/Xirokik/Gesture-controlled-vehicle/blob/main/Project's%20files/Test_stand.jpg)
