import os
import face_recognition
import cv2
image = 'images/31-Bipin.png'
image = cv2.imread(image)
facesCurrentFrame = face_recognition.face_locations(image)
print(len(facesCurrentFrame))