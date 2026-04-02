import matplotlib.pyplot as plt
import cv2

image=cv2.imread('Sunflower.jpg')
hieght,width,_=image.shape

rect1_width,rect1_height=200,200
top_left1=(20,20)
bottom_right1=(top_left1[0]+rect1_width,top_left1[1]+rect1_height)
cv2.rectangle(image,top_left1,bottom_right1,(0,255,0),3)

rect2_width,rect2_height=200,150
top_left2=(width-rect2_width-20,hieght-rect2_height-20)
bottom_right2=(top_left2[0]+rect2_width,top_left2[1]+rect2_height)
cv2.rectangle(image,top_left2,bottom_right2,(0,255,0),3)

circle_xcenter1=top_left1[0]//2
circle_ycenter1=top_left1[1]//2
circle_xcenter2=top_left2[0]//2
circle_ycenter2=top_left2[1]//2
cv2.circle(image,(circle_xcenter1,circle_ycenter1),15,(255,0,0),-1)
cv2.circle(image,(circle_xcenter2,circle_ycenter2),15,(255,0,0),-1)

cv2.line(image,(circle_xcenter1,circle_ycenter1),(circle_xcenter2,circle_ycenter2),(0,255,0),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'region 1',(top_left1[0],top_left1[1]-10),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(image,'region 2',(top_left2[0],top_left2[1]-10),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(image,'center 1',(circle_xcenter1-40,circle_ycenter1+40),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(image,'center 2',(circle_xcenter2-40,circle_ycenter2+40),font,0.5,(255,255,255),2,cv2.LINE_AA)

arrow_start=(width-50,20)
arrow_end=(width-50,hieght-20)

cv2.arrowedLine(image,arrow_start,arrow_end,(255,0,0),3)
cv2.arrowedLine(image,arrow_end,arrow_start,(255,0,0),3)

lbl_hieght=(arrow_start[0]-150,arrow_start[1]+arrow_end[1]//2)
cv2.putText(image,f'height:{hieght}px',(lbl_hieght[0],lbl_hieght[1]),font,0.5,(255,255,255),2,cv2.LINE_AA)

plt.figure(figsize=(12,10))
plt.title('Annotated Image')
plt.axis('off')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()