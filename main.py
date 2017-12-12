import face_recognition
import gg

face_locations = gg.func()
# thomas_image = face_recognition.load_image_file("Thomas.jpg")
# TJ_image = face_recognition.load_image_file("TJ.jpg")
# unknown_image = face_recognition.load_image_file("siliconvalley.jpg")
# # unknown_image = []
# # for i in range(0,gg.faceNum):
# #     strI = '%d' % i
# #     unknown_image.append(face_recognition.load_image_file('/Users/ron/Desktop/test'+strI+'.jpg'))
#
# tj_encoding = face_recognition.face_encodings(TJ_image)[0]
# thomas_encoding = face_recognition.face_encodings(thomas_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image,face_locations)
# print unknown_encoding
# label = ['Thomas','TJ']
# faceNum = len(face_locations)
# for i in range(0,faceNum):
#     results = face_recognition.compare_faces([thomas_encoding, tj_encoding], unknown_encoding[i])
#     for j in range(0, len(results)):
#         if results[j] == True:
#             print('The person is:'+label[j])

# labels = ['jobs', 'obama']
# label = ['Thomas','William']
# print('results:'+str(results))
#
# for i in range(0, len(results)):
#     if results[i] == True:
#         print('The person is:'+label[i])