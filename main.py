import cv2
import numpy as np
import face_recognition
import os
from operations import *
from add_face import *
passwordCount = 0
def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def take_attendance():
    count = 0
    path = 'images'
    images = []
    personNames = []
    attendanceList = []
    myList = os.listdir(path)
    if len(myList) == 0:
        print ('\nNo images found in the directory\n')
        input ('Press any key to continue...')
        os.system('cls')
        return
    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    encodeListKnown = faceEncodings(images)
    # for i in range(len(personNames)):
    #     print('Encoding of ' + personNames[i] + ' is:\n' + str(encodeListKnown[i]))
    print('All Encodings Complete!!!')
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
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
                count = write_attendance_in_xl(name, get_dict(), count)
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
        print("Attendance was marked for",count, "student(s) out of", len(attendanceList), "student(s) whose faces were detected")
    else:
        print("No student was detected")
    input('Press any key to continue...')
    return

try:
    os.makedirs('images')
except:
    pass
choice = 0
while choice != "4":
    os.system('cls')
    print('Press 1 to take attendance')
    print('Press 2 to fetch attendance')
    print('Press 3 to add new face')
    print('Press 4 to exit')
    choice = input('Enter your choice: ')
    if choice == "1":
        take_attendance()
    elif choice == "2":
        fetch_attendance(get_dict())
    elif choice == "3":
        while passwordCount < 3:
            password = input('Enter password or enter -1 to exit: ')
            if password == 'group1_dse':
                add_the_face()
                break
            elif password == '-1':
                break
            else:
                passwordCount += 1
                print('Wrong password')
        if passwordCount == 3:
            print('You have entered a wrong password 3 times, you will not be allowed to add new face')
            override = input('Press any key to continue...')
            if override == 'admin@override':
                passwordCount = 0
    elif choice == "4":
        pass
    else:
        print('Invalid choice')
        input('Press any key to continue...')