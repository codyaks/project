import cv2, time, pyautogui
import mediapipe as mp

mp_hands= mp.solutions.hands
hands= mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw= mp.solutions.drawing_utils

scroll_speed = 300
scroll_delay = 1
cam_width, cam_height = 640, 480

def detect_gesture(hand_landmarks, handedness):
    fingers = []
    tips= [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == 'Right' and thumb_tip.x > thumb_ip.x) or (handedness == 'Left' and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    return 'scroll_up' if sum(fingers) == 5 else 'scroll_down' if sum(fingers) == 1 else 'none'
cap = cv2.VideoCapture(0)
cap.set(3, cam_width)
cap.set(4, cam_height)
last_scroll_time = p_time = 0
print('to scroll up: show all fingers, to scroll down: \n and to quit: press "q"')

while cap.isOpened():
    success, img = cap.read()
    if not success:break
    img=cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
    results= hands.process(img)
    gesture, handedness = 'none', 'unknown'
    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness = hand_handedness.classification[0].label
            gesture = detect_gesture(hand_landmarks, handedness)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if (time.time() - last_scroll_time) > scroll_delay:
                if gesture == 'scroll_up':
                    pyautogui.scroll(scroll_speed)
                elif gesture == 'scroll_down':
                    pyautogui.scroll(-scroll_speed)
                last_scroll_time = time.time()
    fps = 1 / (time.time()- p_time) if (time.time()- p_time) > 0 else 0
    p_time = time.time()
    cv2.putText(img, f'FPS: {int(fps)} | hand: {handedness} | gesture: {gesture}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow('Hand Gesture Scroll', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()