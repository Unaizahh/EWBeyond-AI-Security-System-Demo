import cv2

banana_cascade = cv2.CascadeClassifier('banana_info.xml')

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Flipping screen
    frame = cv2.flip(frame, 1)

    # Detection Tracking
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    banana = banana_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=38,minSize=(50, 100), maxSize=(500,1000), flags=cv2.CASCADE_SCALE_IMAGE)

    for(x,y,w,h) in banana:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),3)
        cv2.putText(frame,'danger',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))

    # Danger Sign
    if len(banana) > 0:
        cv2.putText(frame,'Danger Detected!',(200,100),cv2.FONT_HERSHEY_TRIPLEX,3,(0,0,255))
    else:
        cv2.putText(frame,'Safe...',(550,100),cv2.FONT_HERSHEY_TRIPLEX,3,(0,255,0))

    cv2.imshow('Detecting Dangerous Bananas',frame)

    # Exiting Frame
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()