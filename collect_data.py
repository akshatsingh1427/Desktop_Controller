import cv2
import mediapipe as mp
import csv
import os

gesture_name = input("Enter gesture name: ")

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

file_exists = os.path.isfile("data.csv")

with open("data.csv", mode='a', newline='') as f:
    writer = csv.writer(f)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                row = []
                for lm in handLms.landmark:
                    row.append(lm.x)
                    row.append(lm.y)

                row.append(gesture_name)
                writer.writerow(row)   # 🔥 SAVE IMMEDIATELY

                cv2.putText(img, f"Saving...",
                            (50,50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0,255,0), 3)

        cv2.imshow("Collecting Data", img)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:
            break

cap.release()
cv2.destroyAllWindows()

print("Data Saved Successfully")
