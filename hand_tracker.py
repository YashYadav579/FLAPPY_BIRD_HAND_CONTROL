import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.hand_y = 0.5  # Default Y position

    def get_hand_y(self):
        ret, frame = self.cap.read()
        if not ret:
            return self.hand_y

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        hand_landmarks = getattr(result, "multi_hand_landmarks", None)
        if hand_landmarks:
            for handLms in hand_landmarks:
                self.hand_y = handLms.landmark[0].y

        return self.hand_y
