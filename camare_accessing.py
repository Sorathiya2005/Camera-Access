import cv2 as chr
str = chr.VideoCapture(0)

while(True):
	ret, frame = str.read()
	chr.imshow('frame', frame)
	if chr.waitKey(1) & 0xFF == ord('q'):
		break
str.release()
chr.destroyAllWindows()
