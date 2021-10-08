import numpy as np
import cv2

def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

fgbg = cv2.createBackgroundSubtractorMOG2()

detects = []
detects2 = []
detects3 = []
detects4 = []

posL = 240
offset = 30

xy1 = (20, posL)
xy2 = (620, posL)


azul = 0
vermelho = 0
laranja = 0
verde = 0

# Azul (Uva)
blueLower = (94, 80, 2)
blueUpper = (126, 255, 255)

# Vermelho (Morango)
redLower = (120, 40, 30)
redUpper = (180, 255, 255)

# Laranja (Laranja)
orangeLower = (4, 120, 40)
orangeUpper = (30, 255, 255)

# Verde (Limão)
greenLower = (25, 100, 60)
greenUpper = (80, 255, 255)

while True:
	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Mascara Azul
	maskBlue = cv2.inRange(hsv, blueLower, blueUpper)
	maskBlue = cv2.erode(maskBlue, None, iterations=2)
	maskBlue = cv2.dilate(maskBlue, None, iterations=2)

	# Mascara Vermelha
	maskRed = cv2.inRange(hsv, redLower, redUpper)
	maskRed = cv2.erode(maskRed, None, iterations=2)
	maskRed = cv2.dilate(maskRed, None, iterations=2)

	# Mascara Laranja
	maskOrange = cv2.inRange(hsv, orangeLower, orangeUpper)
	maskOrange = cv2.erode(maskOrange, None, iterations=2)
	maskOrange = cv2.dilate(maskOrange, None, iterations=2)

	# Mascara Verde
	maskGreen = cv2.inRange(hsv, greenLower, greenUpper)
	maskGreen = cv2.erode(maskGreen, None, iterations=2)
	maskGreen = cv2.dilate(maskGreen, None, iterations=2)

	cv2.line(frame,xy1,xy2,(255,0,0),3)

	cv2.line(frame,(xy1[0],posL-offset),(xy2[0],posL-offset),(255,255,0),2)

	cv2.line(frame,(xy1[0],posL+offset),(xy2[0],posL+offset),(255,255,0),2)

##################### Azul #####################
	contours, hierarchy = cv2.findContours(maskBlue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	i = 0
	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)

		area = cv2.contourArea(cnt)
		
		if int(area) > 3000 :
			centro = center(x, y, w, h)

			# cv2.putText(frame, str(i), (x+5, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
			cv2.circle(frame, centro, 4, (255, 255, 255), -1)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			if len(detects) <= i:
				detects.append([])
			if centro[1]> posL-offset and centro[1] < posL+offset:
				detects[i].append(centro)
			else:
				detects[i].clear()
			i += 1

	if i == 0:
		detects.clear()

	i = 0

	if len(contours) == 0:
		detects.clear()

	else:

		for detect in detects:
			for (c,l) in enumerate(detect):


				if detect[c-1][1] < posL and l[1] > posL :
					detect.clear()
					azul+=1
					cv2.line(frame,xy1,xy2,(0,255,0),5)
					continue

				if detect[c-1][1] > posL and l[1] < posL:
					detect.clear()
					# total+=1
					# cv2.line(frame,xy1,xy2,(0,0,255),5)
					continue

				if c > 0:
					cv2.line(frame,detect[c-1],l,(0,0,255),1)

##################### Vermelho #####################
	contours, hierarchy = cv2.findContours(maskRed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	i = 0
	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)

		area = cv2.contourArea(cnt)
		
		if int(area) > 3000 :
			centro = center(x, y, w, h)

			# cv2.putText(frame, str(i), (x+5, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
			cv2.circle(frame, centro, 4, (255, 255, 255), -1)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
			if len(detects2) <= i:
				detects2.append([])
			if centro[1]> posL-offset and centro[1] < posL+offset:
				detects2[i].append(centro)
			else:
				detects2[i].clear()
			i += 1

	if i == 0:
		detects2.clear()

	i = 0

	if len(contours) == 0:
		detects2.clear()

	else:

		for detect2 in detects2:
			for (c,l) in enumerate(detect2):


				if detect2[c-1][1] < posL and l[1] > posL :
					detect2.clear()
					vermelho+=1
					cv2.line(frame,xy1,xy2,(0,255,0),5)
					continue

				if detect2[c-1][1] > posL and l[1] < posL:
					detect2.clear()
					# total+=1
					# cv2.line(frame,xy1,xy2,(0,0,255),5)
					continue

				if c > 0:
					cv2.line(frame,detect2[c-1],l,(0,0,255),1)

##################### Laranja #####################
	contours, hierarchy = cv2.findContours(maskOrange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	i = 0
	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)

		area = cv2.contourArea(cnt)
		
		if int(area) > 3000 :
			centro = center(x, y, w, h)

			# cv2.putText(frame, str(i), (x+5, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
			cv2.circle(frame, centro, 4, (255, 255, 255), -1)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,150,255),2)
			if len(detects3) <= i:
				detects3.append([])
			if centro[1]> posL-offset and centro[1] < posL+offset:
				detects3[i].append(centro)
			else:
				detects3[i].clear()
			i += 1

	if i == 0:
		detects3.clear()

	i = 0

	if len(contours) == 0:
		detects3.clear()

	else:

		for detect3 in detects3:
			for (c,l) in enumerate(detect3):


				if detect3[c-1][1] < posL and l[1] > posL :
					detect3.clear()
					laranja+=1
					cv2.line(frame,xy1,xy2,(0,255,0),5)
					continue

				if detect3[c-1][1] > posL and l[1] < posL:
					detect3.clear()
					# total+=1
					# cv2.line(frame,xy1,xy2,(0,0,255),5)
					continue

				if c > 0:
					cv2.line(frame,detect3[c-1],l,(0,0,255),1)

##################### Verde #####################
	contours, hierarchy = cv2.findContours(maskGreen,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	i = 0
	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)

		area = cv2.contourArea(cnt)
		
		if int(area) > 3000 :
			centro = center(x, y, w, h)

			# cv2.putText(frame, str(i), (x+5, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
			cv2.circle(frame, centro, 4, (255, 255, 255), -1)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
			if len(detects4) <= i:
				detects4.append([])
			if centro[1]> posL-offset and centro[1] < posL+offset:
				detects4[i].append(centro)
			else:
				detects4[i].clear()
			i += 1

	if i == 0:
		detects4.clear()

	i = 0

	if len(contours) == 0:
		detects4.clear()

	else:

		for detect4 in detects4:
			for (c,l) in enumerate(detect4):


				if detect4[c-1][1] < posL and l[1] > posL :
					detect4.clear()
					verde+=1
					cv2.line(frame,xy1,xy2,(0,255,0),5)
					continue

				if detect4[c-1][1] > posL and l[1] < posL:
					detect4.clear()
					# total+=1
					# cv2.line(frame,xy1,xy2,(0,0,255),5)
					continue

				if c > 0:
					cv2.line(frame,detect4[c-1],l,(0,0,255),1)

	cv2.putText(frame, "TOTAL: "+str(azul+vermelho+laranja+verde), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
	cv2.putText(frame, "Uva: "+str(azul), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 50, 100),2)
	cv2.putText(frame, "Morango: "+str(vermelho), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),2)
	cv2.putText(frame, "Laranja: "+str(laranja), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 255),2)
	cv2.putText(frame, "Limao: "+str(verde), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),2)

	cv2.imshow("frame", frame)

	if cv2.waitKey(30) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()