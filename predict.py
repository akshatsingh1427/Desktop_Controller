import cv2
import mediapipe as mp
import pickle
import pyautogui
import numpy as np
import time
import screen_brightness_control as sbc

model = pickle.load(open("model.pkl", "rb"))

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0
smoothening = 7
last_action_time = 0
cooldown = 0.7

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            row = []
            lmList = []

            for lm in handLms.landmark:
                row.append(lm.x)
                row.append(lm.y)
                lmList.append((int(lm.x * img.shape[1]),
                               int(lm.y * img.shape[0])))

            prediction = model.predict([row])[0]
            confidence = max(model.predict_proba([row])[0])

            cv2.putText(img, f"{prediction} ({round(confidence*100,2)}%)",
                        (50,50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0,255,0), 3)

            current_time = time.time()

            # ======================
            # MOUSE MOVE
            # ======================
            if prediction == "mouse":
                x = np.interp(lmList[8][0], [0, img.shape[1]], [0, screen_w])
                y = np.interp(lmList[8][1], [0, img.shape[0]], [0, screen_h])

                curr_x = prev_x + (x - prev_x) / smoothening
                curr_y = prev_y + (y - prev_y) / smoothening

                pyautogui.moveTo(screen_w - curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

            # ======================
            # LEFT CLICK
            # ======================
            elif prediction == "left_click":
                if current_time - last_action_time > cooldown:
                    pyautogui.click()
                    last_action_time = current_time

            # ======================
            # RIGHT CLICK
            # ======================
            elif prediction == "right_click":
                if current_time - last_action_time > cooldown:
                    pyautogui.rightClick()
                    last_action_time = current_time

            # ======================
            # DRAG
            # ======================
            elif prediction == "drag":
                pyautogui.mouseDown()

            # ======================
            # VOLUME
            # ======================
            elif prediction == "volume":
                pyautogui.press("volumeup")

            # ======================
            # BRIGHTNESS
            # ======================
            elif prediction == "brightness":
                sbc.set_brightness('+5')

            # ======================
            # PLAY / PAUSE
            # ======================
            elif prediction == "pause":
                if current_time - last_action_time > cooldown:
                    pyautogui.press("space")
                    last_action_time = current_time

            # ======================
            # SHOW DESKTOP
            # ======================
            elif prediction == "desktop":
                if current_time - last_action_time > cooldown:
                    pyautogui.hotkey("win", "d")
                    last_action_time = current_time

            else:
                pyautogui.mouseUp()

    cv2.imshow("AI Gesture Desktop Controller", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

