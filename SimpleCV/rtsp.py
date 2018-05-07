"""
    Simple example of a connection to 

    IPC (720P) Motorized Zoom & Auto Focal LEN 1/3" Aptina AR0130 CMOS Hi3518C CCTV IP camera
    Default IP 192.168.1.10

    Sony IMX module
    Default IP 192.168.1.88

"""

import cv2

#camera = cv2.VideoCapture("rtsp://192.168.1.10:554/user=admin&password=&channel=1&stream=0.sdp")
#camera = cv2.VideoCapture("rtsp://192.168.1.88:554/user=admin&password=&channel=1&stream=0.sdp")
#camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture('capture-000.mp4')


while(1):
    ret, frame = camera.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
    
    key = cv2.waitKey(1) & 0xFF
    
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()