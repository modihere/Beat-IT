import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while (True):

	ret,frame=cap.read()

	hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
	lower_green = np.array([50,100,100])
	upper_green = np.array([70,255,255])
	mask = cv.inRange(hsv,lower_blue,upper_blue)
	mask_green = cv.inRange(hsv,lower_green,upper_green)
	masking = mask+mask_green
	res = cv.bitwise_and(frame,frame, mask = masking)
	ret,thresh = cv.threshold(mask,127,255,0)
	contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
	ret1,thresh1 = cv.threshold(mask_green,127,255,0)
	contours1, hierarchy1 = cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
	# cnt = contours[0]
	# area = cv.contourArea(cnt)
	# print(area)
	cv.drawContours(frame,contours,-1,(0,255,0),3)
	cv.drawContours(frame,contours1,-1,(255,51,51),3)
	cv.imshow('frame',frame)
	cv.imshow('mask',masking)
	cv.imshow('res',res)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()