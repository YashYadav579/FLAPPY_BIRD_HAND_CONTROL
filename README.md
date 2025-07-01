# 🐤 Flappy Bird - Hand Controlled (Python + MediaPipe + Pygame)

### ✅ Project Task – (Computer Vision / Python Game Development)

This project is a modern twist on the classic Flappy Bird game, controlled entirely by your hand movements detected via your webcam. Using MediaPipe for hand tracking and Pygame for game mechanics, the bird flies when you lift your hand, creating an interactive and fun experience.

---

## 🧠 What is This?

An experimental game that uses Computer Vision to allow gesture-controlled gameplay.
It can help you learn:
 - 👋 How to track hand movement in real-time
 - 🎮 How to integrate OpenCV and MediaPipe with Pygame
 - 🧠 How to build interactive GUI games using Python

---

## 🎯 Features of This Project

- 🖐️ Hand-tracking controlled bird movement
- 🎮 Pygame-based gameplay
- 🌇 Custom assets: background, pipes, and bird
- 🧱 Obstacle (pipe) generation and collision detection
- 🧠 Game over screen with score
- 🔁 Auto restart on spacebar press

---

## 📂 File Structure

```bash
FLAPPY_BIRD_HAND_CONTROL/
├── flappy_hand.py        # Main game file
├── hand_tracker.py       # Hand detection logic using MediaPipe
├── assets/
│   ├── bg.png            # Background image
│   ├── bird.png          # Bird image
│   └── pipe.png          # Pipe image
├── README.md             # Project documentation

```

---

## 🖥️ GUI Preview

![image](https://github.com/user-attachments/assets/1b25029a-d14d-4683-9c25-6d65302dfb2f)
![image](https://github.com/user-attachments/assets/420fd05b-aea4-4c5f-8ae6-876fb81ec03e)
![image](https://github.com/user-attachments/assets/5cea16b6-97ba-4301-b0b4-7744fdc04f54)

---


## 🛠️ How to Run

### ⚙️ Prerequisites:
- Python 3.x
- pygame
- opencv-python
- mediapipe

### 🧪 Steps:
```bash
git clone https://github.com/YashYadav579/FLAPPY_BIRD_HAND_CONTROL.git
cd FLAPPY_BIRD_HAND_CONTROL
pip install pygame opencv-python mediapipe
python flappy_hand.py
```

---

## ⚠️ Notes

 - Webcam must be enabled for hand tracking.
 - Lighting affects tracking accuracy—prefer bright, clear conditions.
 - Game uses vertical hand movement (lift hand quickly to flap).

---

## 🙋‍♂️ About Me

**Name**: _Yash Yadav_  
**Task**: Flappy Bird controlled by hand movement using OpenCV, MediaPipe & Pygame

---

## 🔗 Connect with Me

- 💼 [LinkedIn](https://www.linkedin.com/in/yashyadav-5790abc/)
- 💻 [GitHub](https://github.com/YashYadav579)

---

## 🏁 Conclusion

Through this project, I learned:
 - How to detect hand movement using MediaPipe
 - Integration of real-time webcam input in games
 - Working with collision detection and Pygame mechanics
 - Building fun and engaging gesture-controlled games in Python
