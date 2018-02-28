# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:38:47 2018

@author: jareng
"""

"""
    Kilder for blob extraction og running average :
        https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
        http://opencvpython.blogspot.no/2012/07/background-extraction-using-running.html

"""

# import the necessary packages
import argparse
import datetime
import time
import cv2
import numpy as np
#import winsound



# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())




# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
    #camera = cv2.VideoCapture(0)
    
    camera = cv2.VideoCapture("rtsp://192.168.1.10:554/user=admin&password=&channel=1&stream=0.sdp")
    time.sleep(3)
    
    time.sleep(0.25)
 
    _,frame = camera.read()


    avg1 = np.float32(frame)
    avg2 = np.float32(frame)




# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])


occupied_new = True

# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
    (grabbed, frame) = camera.read()
    text = "Unoccupied"


   
    cv2.accumulateWeighted(frame,avg1,0.1)
    cv2.accumulateWeighted(frame,avg2,0.01)
     
    res1 = cv2.convertScaleAbs(avg1)
    res2 = cv2.convertScaleAbs(avg2)
    #res1 = frame
    #res2 = frame



	# if the frame could not be grabbed, then we have reached the end
	# of the video
    if not grabbed:
        break

    # resize the frame, convert it to grayscale, and blur it
    #frame = imutils.resize(frame, width=500)
    Current = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Current = cv2.GaussianBlur(Current, (21, 21), 0)

    Background = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
    Background = cv2.GaussianBlur(Background, (21, 21), 0)



    # compute the absolute difference between the current frame and
    # first frame
    frameDelta = cv2.absdiff(Background, Current)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
         cv2.CHAIN_APPROX_SIMPLE)


    occupied = False
  
    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < args["min_area"]:
            continue

        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
        
        occupied = True
 
        # Write the coordinates at the center of the blob       
        xc = x + int(w/2)
        yc = y + int(h/2)

        cv2.putText(frame, "%d %d" % (xc, yc), (xc, yc),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
  
        
    if occupied:
        if occupied_new:
            #winsound.PlaySound("SystemExit", winsound.SND_ASYNC) 
            print("\a")
        occupied_new = False
 
    else:
        occupied_new = True


    # draw the text and timestamp on the frame
    cv2.putText(frame, "Press 'q' to quit. Room Status: {}".format(text), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # show the frame and record if the user presses a key
    
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    
    cv2.imshow('avg1',res1)
    cv2.imshow('avg2',res2)
    cv2.imshow("Security Feed", frame)

#   Modified to play with rtsp
#    key = cv2.waitKey(1) & 0xFF
    key = cv2.waitKey(1) & 0xFF


    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
