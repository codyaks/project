import cv2, mediapipe as mp, numpy as np
from pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
TH, IX= Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

try:
    dev= AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, 'GetDefaultOutputDevice') else AudioUtilities.GetSpeakers()
    volctrl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    volmin, volmax = volctrl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Audio device error: {e}");exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera"); exit()

win="Hand Gesture Control"; cv2.namedWindow(win, cv2.WINDOW_NORMAL)

while True:
    ok, img = cap.read()
    if not ok:break
    img = cv2.flip(img, 1)
    h,w= img.shape[:2]
    res=hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    