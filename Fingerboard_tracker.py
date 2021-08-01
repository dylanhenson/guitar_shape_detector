# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:21:03 2021

@author: Dylan
"""

import cv2

cap = cv2.VideoCapture(1)


# object detection from stable camera
object_detector = cv2.createBackgroundSubtractorMOG2()



while True:
    ret, frame = cap.read()
    
    mask = object_detector.apply(frame)
    
        
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()

cap.destroyAllWindows()












'''
Below is going off this video: https://www.youtube.com/watch?v=1FJWXOO1SRI&t=536s
The cv2.legacy_TrackerMOSSE() function/method isnt working because its been
moved to legacy

tracker = cv2.legacy_TrackerMOSSE().create()

# Take one frame before while loop begins 
success, img = cap.read()
bounding_box = cv2.selectROI("Tracking", img, False) # The bounding box that selects the image
tracker.init(img, bounding_box)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read() # gives us the frame
    
    fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer) 
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    
    cv2.imshow("Tracking", img) # shows the frame
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cv2.destroyAllWindows() 
'''