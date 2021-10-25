
import cv2
import mediapipe as mp
import time 

cap = cv2.VideoCapture(0) #create video object from cam 0
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils
ptime = 0
ctime = 0

while (True):
    success, img = cap.read() #read frame 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if (results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 3)
    cv2.imshow("Image", img) 
    cv2.waitKey(1) #wait 1 millisecond 