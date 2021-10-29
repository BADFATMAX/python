import cv2
import numpy as np

# Video Capture 
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(0)

green = np.array([0, 0, 255], dtype=np.uint8)
red = np.array([0, 255, 0], dtype=np.uint8)

# History, Threshold, DetectShadows 
fgbg = cv2.createBackgroundSubtractorMOG2(50, 200, False)

# Keeps track of what frame we're on
frameCount = 0

while capture.isOpened():
	# Return Value and the current frame
	ret, frame = capture.read()
	ret2, frame2 = capture.read()

	#  Check if a current frame actually exist
	if not ret:
		break

	frameCount += 1
	# Resize the frame
	resizedFrame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)

	# Get the foreground mask
	fgmask = fgbg.apply(resizedFrame)

	contour = cv2.absdiff(frame, frame2)
	contour_r = cv2.GaussianBlur(contour, (5, 5), cv2.BORDER_DEFAULT)
	contour_r = cv2.inRange(contour_r, (0, 20, 0), (255, 255, 255))
	contour_r = cv2.cvtColor(contour_r, cv2.IMREAD_COLOR)

	mask_r = np.where(np.all(contour_r != (255, 255, 255), axis=-1, keepdims=True), red, green)

	# Result
	res1 = cv2.addWeighted(frame, 1, mask_r, 1, 0)

	# Count all the non zero pixels within the mask
	count = np.count_nonzero(fgmask)

	print('Frame: %d, Pixel Count: %d' % (frameCount, count))

	# Determine how many pixels do you want to detect to be considered "movement"
	if frameCount > 1 and count > 300:
		print('MOTION DETECTED')
		cv2.putText(res1, 'MOTION DETECTED', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

	cv2.imshow('Frame', resizedFrame)
	cv2.imshow('Mask', fgmask)
	cv2.imshow('Contour', contour)
	cv2.imshow('Contour_r', contour_r)
	cv2.imshow('GREEN-RED MASK', mask_r)
	cv2.imshow('RESULT', res1)

	k = cv2.waitKey(1) & 0xff
	if k == 27: # esc to stop
		break

capture.release()
cv2.destroyAllWindows()
