import cv2
import os
import numpy as np
import faceRecognition as fr


#This module takes images  stored in disk and performs face recognition
test_img=cv2.imread('E:\ppts\deep learning\FaceRecognition-master\FaceRecognition-master\TestImages\p3.jpg')#test_img path
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)


#Comment below lines when running this program second time.Since it saves training.yml file in directory
faces,faceID=fr.labels_for_training_data('E:\ppts\deep learning\FaceRecognition-master\FaceRecognition-master\trainingImages')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.write('E:\ppts\deep learning\FaceRecognition-master\FaceRecognition-master\trainingData.yml')


#Uncomment below line for subsequent runs
#face_recognizer=cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('E:\ppts\deep learning\FaceRecognition-master\FaceRecognition-master\trainingData.yml')
#use this to #load training data for subsequent runs

name={0:"Priyanka",1:"Kangana",2:"Mahesh"}#creating dictionary containing names for each label

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+w]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>100):#If confidence more than 100 then don't print predicted face text on screen
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(900,800))
cv2.imshow("Predicted image",resized_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows()





