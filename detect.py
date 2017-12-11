import face_recognition
import cv2
import string
from PIL import Image

def func():
    imgNumpyArray = face_recognition.load_image_file("siliconvalley.jpg")
    face_locations = face_recognition.face_locations(imgNumpyArray)
    print face_locations

    img = cv2.imread("siliconvalley.jpg")
    imgOpen = Image.open("siliconvalley.jpg")

    cv2.namedWindow("original")
    cv2.imshow("original", img)

    faceNum = len(face_locations)
    arrIMG = []

    for i in range(0, faceNum):
        top = face_locations[i][0]
        right = face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]

        start = (left, top)
        end = (right, bottom)

        box = (left, top, right, bottom)
        # arrIMG.append(imgOpen.crop(box))
        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)

    print arrIMG
    cv2.namedWindow("recognize")
    cv2.imshow("recognize", img)

    # print faceNum
    # for i in range(0,faceNum-1):
    #     strI = '%d' %i
    #     arrIMG[i].save('/Users/ron/Desktop/test'+strI+'.jpg')

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return face_locations
