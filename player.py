#play a video from a file
import numpy as np
import cv2 as cv

cap=cv2.VideoCapture('video.mp4')

while(cap,isOpened()):

	ret,frame=cap.read()

	cv.imshow('frame',frame)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()