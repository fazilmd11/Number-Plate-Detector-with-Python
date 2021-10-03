import cv2

frameWidth = 480
frameHeight = 640
minArea = 500
color=(255,0,255)

#url = "http://192.168.0.100:8080/video"
cap=cv2.VideoCapture(0)       # 0 for webcam, 1 for secondary webcam, url for IP webcam
cap.set(3,frameHeight)
cap.set(4,frameWidth)
cap.set(10,130)
count=0
NumberPlateCascade = cv2.CascadeClassifier("Resourses/haarcascade_russian_plate_number.xml")
while True:
    success, img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = NumberPlateCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
            imgROI = img[y:y+h,x:x+w]
            cv2.imshow("roi",imgROI)


    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("Resourses/NPlate_"+str(count)+".jpg",imgROI)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        count +=1
