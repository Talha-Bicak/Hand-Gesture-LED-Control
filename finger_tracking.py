import cv2
import mediapipe as mp
import pyttsx3
import threading
import serial
import time

# Kamera ve pyttsx3 motorunu başlat
camera = cv2.VideoCapture(1)
engine = pyttsx3.init()

# Mediapipe eller modülünü başlat
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Arduino ile seri bağlantı kur
arduino = serial.Serial('COM7', 9600)  # COM portu ve baudrate ayarlayın
time.sleep(2)  # Bağlantı stabil hale gelmesi için bekleyin

def speak(message):
    engine.say(message)
    engine.runAndWait()

while True:
    success, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hlms = hands.process(imgRGB)
    height, width, channel = img.shape

    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:
            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)
                cv2.putText(img, str(fingerNum), (positionX, positionY),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            # Koşulları öncelik sırasına göre kontrol et
            if (handlandmarks.landmark[4].y < handlandmarks.landmark[5].y and
                handlandmarks.landmark[12].y < handlandmarks.landmark[9].y and
                handlandmarks.landmark[8].y < handlandmarks.landmark[5].y and
                handlandmarks.landmark[16].y < handlandmarks.landmark[13].y and
                handlandmarks.landmark[20].y < handlandmarks.landmark[17].y):
                threading.Thread(target=speak, args=("Five",)).start()
                arduino.write(b'5')
            elif (handlandmarks.landmark[12].y < handlandmarks.landmark[9].y and
                  handlandmarks.landmark[8].y < handlandmarks.landmark[5].y and
                  handlandmarks.landmark[16].y < handlandmarks.landmark[13].y and
                  handlandmarks.landmark[20].y < handlandmarks.landmark[17].y):
                threading.Thread(target=speak, args=("Four",)).start()
                arduino.write(b'4')
            elif (handlandmarks.landmark[12].y < handlandmarks.landmark[9].y and
                  handlandmarks.landmark[8].y < handlandmarks.landmark[5].y and
                  handlandmarks.landmark[16].y < handlandmarks.landmark[13].y):
                threading.Thread(target=speak, args=("Three",)).start()
                arduino.write(b'3')
            elif (handlandmarks.landmark[12].y < handlandmarks.landmark[9].y and
                  handlandmarks.landmark[8].y < handlandmarks.landmark[5].y):
                threading.Thread(target=speak, args=("Two",)).start()
                arduino.write(b'2')
            elif handlandmarks.landmark[8].y < handlandmarks.landmark[5].y:
                threading.Thread(target=speak, args=("One",)).start()
                arduino.write(b'1')

            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()