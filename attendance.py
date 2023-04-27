import cv2
import numpy as np
import face_recognition
import os
from operations import *
passwordCount = 0
def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def takeattendance():
    count = 0
    path = 'images'
    images = []
    personNames = []
    attendanceList = []
    myList = os.listdir(path)
    if len(myList) == 0:
        print ('\nNo images found in the directory\n')
        os.system('cls')
        return
    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    encodeListKnown = faceEncodings(images)
    print('All Encodings Complete!!!')
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        while not ret:
            ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.4)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = personNames[matchIndex]
                if name not in attendanceList:
                    attendanceList.append(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                count = write_attendance_in_xl(name, count)
        cv2.imshow('Taking attendance', frame)
        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()
    if (len(attendanceList) == count and count != 0):
        print('Attendance for following students has been taken successfully')
        for name in attendanceList:
            print(name)
    elif (len(attendanceList) != count):
        print("Attendance was marked for",count,"student(s) out of", len(attendanceList), "student(s) whose faces were detected")
    else:
        print("No student was detected")