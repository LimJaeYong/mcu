import numpy as np
import cv2

# Cascades 디렉토리의 haarcascade_frontalface_default.xml 파일을 Classifier로 사용
cascade = 'opencv/data/haarcascades/'
faceCascade = cv2.CascadeClassifier(
    cascade + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(
    cascade + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # 상하반전
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #얼굴인식
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #눈 인식
        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=10, 
            minSize=(5, 5)
        )
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        
    cv2.imshow('video', img)  # video라는 이름으로 출력
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit # ESC를 누르면 종료
        break
cap.release()
cv2.destroyAllWindows()
