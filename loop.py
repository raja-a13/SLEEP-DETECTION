from img import *
import os

for i in range(1,6):
	name = './dataset/' + str(i)
	print("")
	print("---------------------------------------------")
	print(f"IMAGE NO : {i}")
	print("for eyes open & mouth open")
	frame = cv2.imread(name + '_emo.jpg')
	eye_sleep(frame)
	
	print("")
	print("for eyes close & mouth open")
	frame = cv2.imread(name + '_emc.jpg')
	eye_sleep(frame)
	
	print("")
	print("for eyes open & mouth closed")
	frame = cv2.imread(name + '_eo.jpg')
	eye_sleep(frame)
	
	print("")
	print("for eyes close & mouth closed")
	frame = cv2.imread(name + '_ec.jpg')
	eye_sleep(frame)
	print("---------------------------------------------")
	print("")
	


