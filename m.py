# _*_ coding: UTF-8 _*_
import cv2
import os
import gg

# 第一个摄像头
cap = cv2.VideoCapture(0)
# 规定fourcc的配置
fourcc = cv2.VideoWriter_fourcc(*'XVID')
i = 1
key = 'y'
path = "./face"
# 输出文件名，fourcc格式，
out = cv2.VideoWriter(path + "/test.avi", fourcc, 20.0, (640, 480))
if not (os.path.exists(path)):
    os.mkdir(path)
    pass

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # frame =cv2.flip(frame,0)#cv2.flip(翻转帧) 0->x轴，1->y轴,负数代表沿两个坐标轴同时翻转

        frame = gg.func(frame)
        dirFile = "face/10_" + str(i)
        dirFile = dirFile + '.bmp'
        cv2.imwrite(dirFile, frame)
        cv2.imshow('sahuibi', frame)
        i+=1
            # if cv2.waitKey(38) & 0xff == ord('c'):
            #
            #     continue



        # out.write(frame)


        key = cv2.waitKey(35) & 0xff
        if key == ord('q'):  # 35是延时35ms
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
