import cv2
from cvzone.SerialModule import SerialObject
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
leftbar=0
rightbar=0
detektor = HandDetector(maxHands=2, detectionCon=0.7)
arduino=SerialObject("/dev/ttyACM0",9600,1)
while True:
    success, img=cap.read()
    hands, img = detektor.findHands(img)
    cv2.rectangle(img, (20, 147), (35, 353), (0, 255, 0), 3)
    cv2.rectangle(img, (610, 147), (625, 353), (0, 255, 0), 3)
    brak = "275275"
    if len(hands) ==2 :
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        handType1=hand1["type"]
        hand2=hands[1]
        lmList2=hand2["lmList"]
        handType2=hand2["type"]
        dl=f'{round(lmList1[8][1]):03d}'
        dl2=f'{round(lmList2[8][1]):03d}'
        if(handType1=="Left"):
            dl3=dl+dl2
            leftbar=lmList2[8][1]
            rightbar=lmList1[8][1]
        else:
            dl3=dl2+dl
            leftbar=lmList1[8][1]
            rightbar=lmList2[8][1]
        arduino.sendData(dl3)

        if leftbar > 150:
            if leftbar < 250:
                cv2.rectangle(img, (23, leftbar), (32, 250), (255, 0, 0), cv2.FILLED)
        else:
            cv2.rectangle(img, (23, 150), (32, 250), (255, 0, 0), cv2.FILLED)

        if leftbar < 400:
            if leftbar > 300:
                cv2.rectangle(img, (23, 250), (32, leftbar-50), (0, 0, 255), cv2.FILLED)
        else:
            cv2.rectangle(img, (23, 250), (32, 350), (0, 0, 255), cv2.FILLED)
        if rightbar > 150:
            if rightbar < 250:
                cv2.rectangle(img, (613, rightbar), (622, 250), (255, 0, 0), cv2.FILLED)
        else:
            cv2.rectangle(img, (613, 150), (622, 250), (255, 0, 0), cv2.FILLED)
        if rightbar < 400:
            if rightbar > 300:
                cv2.rectangle(img, (613, 250), (622, rightbar-50), (0, 0, 255), cv2.FILLED)
        else:
            cv2.rectangle(img, (613, 250), (622, 350), (0, 0, 255), cv2.FILLED)
        print(dl3)
    if len(hands) ==1:
        arduino.sendData(brak)

    if len(hands) ==0:
        arduino.sendData(brak)
    cv2.rectangle(img, (20, 249), (35, 251), (255, 255, 255), cv2.FILLED)
    cv2.rectangle(img, (610, 249), (625, 251), (255, 255, 255), cv2.FILLED)
    cv2.rectangle(img, (20, 199), (35, 201), (155, 155, 155), cv2.FILLED)
    cv2.rectangle(img, (610, 199), (625, 201), (155, 155, 155), cv2.FILLED)
    cv2.rectangle(img, (20, 299), (35, 301), (155, 155, 155), cv2.FILLED)
    cv2.rectangle(img, (610, 299), (625, 301), (155, 155, 155), cv2.FILLED)
    cv2.putText(img, f'50', (43, 205), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'50', (570, 205), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'50', (43, 305), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'50', (570, 305), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'100', (43, 155), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'100', (560, 155), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'100', (43, 355), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'100', (560, 355), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'0', (43, 255), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(img, f'0', (580, 255), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)

    cv2.imshow("Imgae", img)
    cv2.waitKey(1)