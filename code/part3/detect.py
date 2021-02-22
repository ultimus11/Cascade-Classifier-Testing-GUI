import numpy as np
import cv2
img = cv2.imread('F:/pythonSeries/ai_series/cascade_classifier/gr5.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier('F:/pythonSeries/ai_series/cascade_classifier/haarcascade_eye.xml')
objectt = cascade.detectMultiScale(gray,1.3,5) 
for (x,y,w,h) in objectt:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.putText(img, '1', (x,y-10), font, 1, (255,255,255), 3)
cascade = cv2.CascadeClassifier('F:/pythonSeries/ai_series/cascade_classifier/haarcascade_frontalface_default.xml')
objectt = cascade.detectMultiScale(gray,1.3,5) 
for (x,y,w,h) in objectt:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.putText(img, '2', (x,y-10), font, 1, (255,255,255), 3)
cascade = cv2.CascadeClassifier('F:/pythonSeries/ai_series/cascade_classifier/cascade.xml')
objectt = cascade.detectMultiScale(gray,1.01,5) 
for (x,y,w,h) in objectt:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.putText(img, '3', (x,y-10), font, 1, (255,255,255), 3)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
