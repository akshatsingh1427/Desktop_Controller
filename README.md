<div align="center">

# 🖐️ AI Gesture-Based Virtual Desktop Controller

### Computer Vision–Powered Hands-Free Desktop Control System

<img src="https://img.shields.io/badge/Domain-Computer%20Vision-2563EB?style=for-the-badge">
<img src="https://img.shields.io/badge/Category-Artificial%20Intelligence-EA580C?style=for-the-badge">
<img src="https://img.shields.io/badge/Type-Human%20Computer%20Interaction-16A34A?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</div>

<br>

An AI-powered computer vision system that lets users control their computer using hand gestures — no keyboard or mouse required. The project combines **MediaPipe hand tracking** with a **machine learning gesture classifier** to perform mouse movement, clicking, dragging, volume control, brightness adjustment, media control, and desktop navigation in real time.

---

## Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Step-by-Step Guide](#-step-by-step-guide-to-build-the-project)
- [Gesture Controls](#-gesture-controls)
- [System Workflow](#-system-workflow)
- [Applications](#-applications)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🚀 Features

- Mouse movement using hand gestures
- Left click and right click using gestures
- Drag and drop functionality
- Volume control via gesture recognition
- Screen brightness control
- Play / Pause media control
- Show desktop gesture
- AI-based gesture classification using Machine Learning
- Real-time webcam gesture detection

---

## 🛠️ Technologies Used

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
<img src="https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">

</div>

| Category | Tools |
|----------|-------|
| **Language** | Python |
| **Computer Vision** | OpenCV, MediaPipe |
| **Machine Learning** | Scikit-learn, NumPy, Pandas |
| **System Control** | PyAutoGUI, Screen Brightness Control |
| **Model Persistence** | Pickle |

---

## 📂 Project Structure

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
├── requirements.txt
└── README.md               # Project documentation
```

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install opencv-python mediapipe scikit-learn numpy pyautogui screen-brightness-control pandas
```

---

## 🧩 Step-by-Step Guide to Build the Project

### Step 1 — Collect Gesture Dataset

Run the data collection script:

```bash
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

Collect **200–300 samples per gesture**. All samples are automatically saved to `data.csv`.

### Step 2 — Train the AI Model

```bash
python train_model.py
```

This script will:

- Read the dataset
- Train a **Random Forest classifier**
- Evaluate model accuracy
- Save the trained model as `model.pkl`

### Step 3 — Run the Gesture Controller

```bash
python predict.py
```

The webcam opens and the system begins recognizing gestures in real time.

---

## ✋ Gesture Controls

| Gesture | Action |
|---------|--------|
| Index finger up | Move mouse |
| Thumb + Index pinch | Left click |
| Index + Middle finger | Right click |
| Index + Middle + Ring | Drag |
| Volume gesture | Increase volume |
| Brightness gesture | Increase brightness |
| Fist | Play / Pause media |
| Open palm | Show desktop |

---

## 🧠 System Workflow

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

## 🎯 Applications

- Touchless computer control
- Accessibility for physically impaired users
- Gesture-based human-computer interaction
- Smart environments and automation systems
- AI-based interface research

---

## 🏆 Future Improvements

- [ ] Add gesture-based scrolling
- [ ] Support multiple monitors
- [ ] Add gesture customization UI
- [ ] Use deep learning (CNN) for higher accuracy
- [ ] Add voice + gesture hybrid control

---

## 📌 Project Title

**AI Gesture-Based Virtual Desktop Controller Using Computer Vision and Machine Learning**

---

## 👨‍💻 Author

**Akshat Singh**
