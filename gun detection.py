import numpy as np
import cv2
import imutils 
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera=cv2.VideoCapture(0)

firstFrame=True
# gun_exist=None

while True:
    ret,frame=camera.read()
    
    if not ret:
        print("Could not access camera")
        break
    
    frame=imutils.resize(frame,width=500)
    # making easier for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun=gun_cascade.detectMultiScale(
        gray,
        1.3,
        5,
        minSize=(100,100)
    )
    
    if len(gun)>0:
        gun_exist=True
        print("Gun detected!")
    else:
        gun_exist=False
        print("Gun not detected.")
        
    for (x,y,w,h) in gun:
        
        frame=cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )
        
       
        cv2.imshow("Security feed",frame)
        key=cv2.waitKey(1) & 0xFF
        
        if key==ord('q'):
            break
        
camera.release()
cv2.destroyAllWindows()