import cv2 as cv
import numpy as np
import time
import serial

ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)


cap = cv.VideoCapture(0)

#ton (0-179), doygunluk(0-255), parlaklık(0-255)
lower_red = np.array([170, 120, 70]) 
upper_red = np.array([180, 255, 255])

lower_green = np.array([35, 100, 50])
upper_green = np.array([85, 255, 150])

while cap.isOpened():
    ret,frame = cap.read()

    hsvConvert = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hsvGreenMask = cv.inRange(hsvConvert, lower_green, upper_green)
    hsvRedMask = cv.inRange(hsvConvert, lower_red, upper_red)


    findGreenContours, _ = cv.findContours(hsvGreenMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contourGreen in findGreenContours:

        if (cv.contourArea(contourGreen) > 3000):

            x,y,w,h = cv.boundingRect(contourGreen)
            cv.rectangle(frame, (x,y), (x+w, y+h), [0,255,0], 2)
            cv.putText(frame, "Dost", (x-5, y-10), cv.FONT_HERSHEY_COMPLEX, 1, [0,255,0], 2)

    findRedContours, _ = cv.findContours(hsvRedMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contourRed in findRedContours:

        if (cv.contourArea(contourRed) > 3000):

            x,y,w,h = cv.boundingRect(contourRed)
            ser.write(f"{int(x)}\n".encode())  # Açıyı byte olarak gönder
            cv.rectangle(frame, (x,y), (x+w, y+h), [0,0,255], 2)
            cv.putText(frame, "Dusman", (x-5, y-10), cv.FONT_HERSHEY_COMPLEX, 1, [0,0,255], 2)




  

    cv.imshow("tracking", frame)

    if (cv.waitKey(1) & 0XFF == ord("q")):
        break


cap.release()
cv.destroyAllWindows()