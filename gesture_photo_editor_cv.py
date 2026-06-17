import cv2 , time, numpy as np
import mediapipe as mp
H=mp.solutions.hands
tip=H.HandLandmark
ids={
    'thumb':tip.THUMB_TIP,
    'index':tip.INDEX_FINGER_TIP,
    'middle':tip.MIDDLE_FINGER_TIP,
    'ring':tip.RING_FINGER_TIP,
    'pinky':tip.PINKY_TIP
}
hands=H.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
draw=mp.solutions.drawing_utils
pairs={"middle":("SEPIA","NEGATIVE"), "ring":("BLUR","GLITCH"),"pinky":("EDGE","CARTOON")}
st = {k:0 for k in pairs}; cur="SEPIA"
DEB, CAP, TT, TP=0.6,1.2,30,20
la= lc=0; pinch_on=False
main,pop="gesture_photo_editor_cv.py","captured press ESC/ close to resume"
paused= False; freeze= None
SEPIA_M = np.array([[0.272,0.534,0.131],[0.349,0.686,0.168],[0.393,0.769,0.189]])
def apply(img,t):
    if t=="SEPIA":
        return np.clip(cv2.transform(img,SEPIA_M),0,255).astype(np.uint8)
    if t=="NEGATIVE":
        return cv2.bitwise_not(img)
    if t=="BLUR":
        return cv2.GaussianBlur(img,(15,15),0)
    if t == "GLITCH": 
        h,w = img.shape[:2]; r,g,b = img[:,:,2], img[:,:,1], img[:,:,0] 
        return cv2.merge([np.roll(b, -int(0.02*w), 1), g, np.roll(r, int(0.04*w), 1)]) 
    if t == "EDGE": return cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 160) 
    if t == "CARTOON": 
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        e = cv2.adaptiveThreshold(cv2.medianBlur(g, 7), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2) 
        c = cv2.bilateralFilter(img, 9, 75, 75) 
        return cv2.bitwise_and(c, c, mask=e) 
    return img 
cap = cv2.VideoCapture(0) 
if not cap.isOpened(): print("Error: Could not access the webcam."); exit()
cv2.namedWindow(main, cv2.WINDOW_NORMAL)
while True:
    if paused:
        cv2.imshow(main, freeze)
        k = cv2.waitKey(1) & 0xFF
        if k == 27: 
            paused = False ;pinch_on = False
            try: cv2.destroyWindow(pop)
            except: pass
            continue
        try: 
            if cv2.getWindowProperty(pop, cv2.WND_PROP_VISIBLE) <= 0: paused = False; pinch_on = False
        except cv2.error:
            paused = False; pinch_on = False

    ok, frame = cap.read()
    if not ok: print("Error: Could not read frame."); break
    img=cv2.flip(frame,1); h,w=img.shape[:2]
    res=hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    now=time.time(); capture=False
    if res.multi_hand_landmarks:
        hand=res.multi_hand_landmarks[0]; draw.draw_landmarks(img,hand,H.HAND_CONNECTIONS)
        lm=hand.landmark; 


        

