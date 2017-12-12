import face_recognition
import cv2
import string
from PIL import Image
import copy
def func(img):
    # imgNumpyArray = face_recognition.load_image_file(path)

    face_cascade = cv2.CascadeClassifier("/Users/ron/opencv" + "/data/haarcascades/haarcascade_frontalface_alt.xml")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # face_locations_1 = face_recognition.face_locations(img)
    face_locations = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.15,
                                          minNeighbors=5,
                                          minSize=(5, 5),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    # print face_locations
    if len(face_locations) != 0:
        # for face_local in face_locations:
            x, y, w, h = face_locations[0]

            start = (x - 50, y - 50)
            end = (x + 400 + 50, y + 400 + 50)

            color = (55, 255, 155)
            thickness = 3
            # (x, y), (x + w, y + h)
            cv2.rectangle(img, start, end, color, thickness)
            crop = img[y:y + 400,x:x + 400]
            # print w,h
            return crop
    else:
        return img
def dec(img):

    face_cascade = cv2.CascadeClassifier("/Users/ron/opencv" + "/data/lbpcascades/lbpcascade_frontalface.xml")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # face_locations_1 = face_recognition.face_locations(img)
    face_locations = face_cascade.detectMultiScale(gray,
                                                   scaleFactor=1.15,
                                                   minNeighbors=5,
                                                   minSize=(5, 5),
                                                   flags=cv2.CASCADE_SCALE_IMAGE)
    # print face_locations
    if len(face_locations) != 0:
        # for face_local in face_locations:
        x, y, w, h = face_locations[0]
        start = (x, y)
        end = (x + 400, y + 400)
        cpImage = copy.deepcopy(img)
        color = (55, 255, 155)
        thickness = 3
        # (x, y), (x + w, y + h)
        crop = cpImage[y:y + 400, x:x + 400]
        cv2.rectangle(img, start, end, color, thickness)
        # print w,h
    else:
        crop = None


    return crop,img