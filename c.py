# _*_ coding: UTF-8 _*_
import numpy as np
import cv2


#第一个摄像头
cap = cv2.VideoCapture(0)
#规定fourcc的配置
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#输出文件名，fourcc格式，
out = cv2.VideoWriter('ctca.avi',fourcc,20.0,(640,480))

while (cap.isOpened()):
	ret,frame = cap.read()
	if ret == True:
		#frame =cv2.flip(frame,0)#cv2.flip(翻转帧) 0->x轴，1->y轴,负数代表沿两个坐标轴同时翻转

		out.write(frame)

		cv2.imshow('sahuibi',frame)
		if cv2.waitKey(38) & 0xff == ord('q'): #35是延时35ms
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()