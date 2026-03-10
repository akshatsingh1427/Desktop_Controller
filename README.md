# 🖐️ AI Gesture-Based Virtual Desktop Controller

An AI-powered computer vision system that allows users to control their computer using hand gestures.
The project uses **MediaPipe for hand tracking** and a **Machine Learning model for gesture recognition** to perform actions like mouse movement, clicking, volume control, brightness adjustment, media control, and desktop navigation without touching the keyboard or mouse.

---

# 🚀 Features

• Mouse movement using hand gestures
• Left click and right click using gestures
• Drag and drop functionality
• Volume control using gesture recognition
• Screen brightness control
• Play / Pause media control
• Show desktop gesture
• AI-based gesture classification using Machine Learning
• Real-time webcam gesture detection

---

# 🧠 Technologies Used

Python
OpenCV
MediaPipe
Scikit-learn
NumPy
PyAutoGUI
Screen Brightness Control
Pickle (for saving trained model)

---

# 📂 Project Structure

```
AI_Gesture_Desktop_Controller/
│
├── collect_data.py        # Collect gesture samples
├── train_model.py         # Train machine learning model
├── predict.py             # Run the gesture controller
│
├── data.csv               # Dataset generated from gestures
├── model.pkl              # Trained ML model
│
├── requirements.txt       # Required libraries
└── README.md              # Project documentation
```

---

# ⚙️ Installation

Install the required libraries:

```
pip install opencv-python mediapipe scikit-learn numpy pyautogui screen-brightness-control pandas
```

---

# 🧩 Step-by-Step Guide to Build the Project

## Step 1 — Collect Gesture Dataset

Run the data collection script:

```
python collect_data.py
```

Enter the gesture name when prompted:

```
mouse
left_click
right_click
drag
volume
brightness
pause
desktop
```

Collect **200–300 samples per gesture**.

All samples will automatically be saved in:

```
data.csv
```

---

## Step 2 — Train the AI Model

Run:

```
python train_model.py
```

This will:

• Read the dataset
• Train a **Random Forest classifier**
• Evaluate model accuracy
• Save the trained model as:

```
model.pkl
```

---

## Step 3 — Run the Gesture Controller

Run the final system:

```
python predict.py
```

The webcam will open and the system will start recognizing gestures.

---

# ✋ Gesture Controls

| Gesture               | Action              |
| --------------------- | ------------------- |
| Index finger up       | Move mouse          |
| Thumb + Index pinch   | Left click          |
| Index + Middle finger | Right click         |
| Index + Middle + Ring | Drag                |
| Volume gesture        | Increase volume     |
| Brightness gesture    | Increase brightness |
| Fist                  | Play / Pause media  |
| Open palm             | Show desktop        |

---

# 🧠 System Workflow

```
Webcam Input
     ↓
MediaPipe Hand Detection
     ↓
Extract 21 Hand Landmarks
     ↓
Machine Learning Model Prediction
     ↓
Gesture Recognized
     ↓
Execute OS Action (Mouse / Volume / Brightness)
```

---

# 🎯 Applications

Touchless computer control
Accessibility for physically impaired users
Gesture-based human-computer interaction
Smart environments and automation systems
AI-based interface research

---

# 🏆 Future Improvements

• Add gesture-based scrolling
• Support multiple monitors
• Add gesture customization UI
• Use deep learning (CNN) for higher accuracy
• Add voice + gesture hybrid control

---

# 📌 Project Title

**AI Gesture-Based Virtual Desktop Controller Using Computer Vision and Machine Learning**

---

# 👨‍💻 Author

Akshat Singh
