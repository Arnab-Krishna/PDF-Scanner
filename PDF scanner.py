import cv2 as cv
import os 
url = 'http://192.168.0.101:8080/video'

cap = cv.VideoCapture(url)
ret = True
f = 0
i = 0

while ret:
    if f == 0:
        print("Press 's' to Scan the Document")
        print("Press 'q' to Quit")
        f = f + 1
        
    ret,frame = cap.read()
    cv.imshow("Camera",frame)

    k = cv.waitKey(1)

    if k == ord('s'):
        cv.destroyWindow("Camera")
        cv.imshow("Scanned Photo",frame)
        print ("Press 'u' If it's Unreadable")
        print("Press 'b' to Convert it to B&W")
        k1= cv.waitKey(0)

        if k1 == ord ('u'):
            cv.destroyWindow("Scanned Photo")
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,155,1)
            cv.imwrite(f"D:/scan/image_thresold{i}.jpg", threshold)
            i = i + 1
            print("Press 's' to Scan More Document")
            print("Press 'q' to Quit")
            continue
        
        elif k1 == ord ('b'):
            cv.destroyWindow("Scanned Photo")
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imwrite(f"D:/scan/image{i}.jpg", gray)
            i = i + 1
            print("Press 's' to Scan More Document")
            print("Press 'q' to Quit")
            continue

    elif k == ord('q'):
        ret = False
        break

cv.destroyAllWindows()
