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
 
import os
import glob
import time
 
 
import argparse
import datetime
import time
import cv2
import numpy as np
import imutils
#import winsound
 
 
homedir = os.getenv("HOME")
print(homedir)
 
path = homedir+"/workdir/bright/"
#path = homedir+"/Dropbox/"
 
savepath = homedir+"/motion/"
 
print(path)
print(savepath)
 
extension = "*.jpg"
 
countoursize = 200
 
 
if os.path.exists(savepath):
        os.system("rm -rf "+savepath+"/*")
 
 
subfolders = [f.path for f in os.scandir(path) if f.is_dir() ] 
print(subfolders)
 
 
     
 
for folder in sorted(subfolders):
 
    print("Processing folder [%s]" % folder)
 
    print("\a")
 
 
 
    directory = os.path.join(folder, extension)
    files = glob.glob(directory)
 
    for file in sorted(files):
        frame = cv2.imread(file, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        avg1 = np.float32(frame)
        avg2 = np.float32(frame)
 
        break
 
    # Variables for detection
    occupied_new = True
    pict = 0
 
    processed = 0
    # loop over the frames of the video
    for file in sorted(files):
        #print(file)
 
        processed += 1
        frame = cv2.imread(file, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
 
        text = "Unoccupied"
 
        cv2.accumulateWeighted(frame,avg1,0.1)
        cv2.accumulateWeighted(frame,avg2,0.01)
 
        res1 = cv2.convertScaleAbs(avg1)
        #res2 = cv2.convertScaleAbs(avg2)
 
 
        # if the frame could not be grabbed, then we have reached the end
        # of the video
 
        #    if not grabbed:
        #        break
 
        # resize the frame, convert it to grayscale, and blur it
        #frame = imutils.resize(frame, width=500)
        Current = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Current = cv2.GaussianBlur(Current, (21, 21), 0)
 
        Background = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
        #Background = cv2.GaussianBlur(Background, (21, 21), 0)
 
 
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
            if cv2.contourArea(c) < countoursize:
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
            print("Found movement in : " + file)
            if occupied_new:
                #winsound.PlaySound("SystemExit", winsound.SND_ASYNC) 
 
                filephead, filetail = os.path.split(file)
                #pict = filetail
                #pictfile = "%stest%s.jpg" % (savepath,pict)
                pictfile = "%s%s" % (savepath,filetail)
                cv2.imwrite(pictfile, frame)
                pict=pict+1
                print(pictfile)
 
 
                occupied_new = False
                print("\a")
 
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
 
        #cv2.imshow('avg1',res1)
        #cv2.imshow('avg2',res2)
        cv2.imshow("Security Feed", frame)
 
        key = cv2.waitKey(1) & 0xFF
 
        # if the `q` key is pressed, break from the lop
        if key == ord("q"):
            break
 
    print("Processed %d files  saved %d files" % (processed,pict))
 
# cleanup the camera and close any open windows
 
cv2.destroyAllWindows()
