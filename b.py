# _*_ coding: UTF-8 _*_
import numpy as np
import cv2
# 0表示第一台摄像设备cap被赋予从cv2的VideoCap
cap = cv2.VideoCapture(0)			

while (True):
	# cap.read成功返回true否则返回false，
	ret, frame = cap.read()
		#ret, frame = cap.read()
		#这里的 read() 函数有两个返回值？
		#要搞清楚这个问题我们必须先了解 VideoCapture 下面的另外两个函数 VideoCapture.grab() 以及 VideoCapture.retrieve()。
		#VideoCapture.grab() 方法抓取视频文件或摄像头的下一帧，如果抓取成功就返回 true。
		#VideoCapture.retrieve() 方法解码抓取到的视频帧并返回。而
		#VideoCapture.read() 函数就是将以上两个函数结合到一起同时返回两个返回值。
		#第一个返回值是一个标志位， true 代表视频帧抓取成功，第二个返回值就是我们得到的视频帧。


	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		#cv2.cvtColor() 函数
		#这个函数用来转换颜色空间。
		#它接收两个参数，第一个参数是要转换的图片，第二个参数是一个枚举值代表如何转换。
		#比如上面的 cv2.COLOR_BGR2GRAY 就代表要将BGR（OpenCV 读取彩色图像的方式）转换为灰度模式，
		#然后返回转换后的图像

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xff == ord('q'):
		cv2.imwrite('12345.png',gray)
		break
		#cv2.waitKey(1) & 0xFF == ord('q') ，这行代码有三个作用：
		#在 cv2.imshow() 函数之后必须有 cv2.waitKey() 函数否则 cv2.imshow() 函数将不起作用。
		#这行代码还起到当我们按下 q 键的时候，退出循环。
		#这段代码还控制视频的播放速度。
			#现在主要讨论一下第三个作用，
			#如果我们直接运行上面的代码，会发现视频播放速度比它原来的速度快很多，几乎是好几倍的播放速度。
			#原因是我们是用一个 while 循环读取视频帧的
			#而 cv2.waitKey(value) 在这里的作用是等待 value 毫秒然后执行下一个循环，
			#换句话说就是每个循环展示一副画面 value 毫秒。
			#注意，这个 value 跟视频的 fps 不是一回事，fps是一秒钟播放多少帧画面，
			#而 value 是展示一幅图 value 毫秒，大致可以理解为 fps = 1000/value。
			#我们可以用 cap.get(5) 获取视频原本的 fps，
			#视频的 fps 为 24，所以我的 value 大概取 1000/24 = 42，
			#这样视频的播放速度就大致与它原本的播放速度一致了。
cap.release()
cv2.destroyAllWindows()