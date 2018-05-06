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
import platform

import glob
import time
import datetime
import cv2
import numpy as np
from PIL import Image, ImageStat


# TODO SHOWTAGS and SAVETAGS / SAVEBOTH ?
# TODO BEEP

save = True
textboxOn = True
showframe = True
sleepTime = 0.5
folderDepth = 1

OSSystem = platform.system()

if OSSystem == "Windows":
    path     = os.path.join('C:\\','git','bilder')
    savepath = os.path.join('C:\\','git','motion')
else:
    path     = "/home/tredea/GrabberArchive"
    savepath = "/home/tredea/motion"

print(path)
print(savepath)
print(OSSystem)


countoursize = 700      # 600 uten blur
TRESH_MIN = 20        # Var 25   40 uten blur
TRESH_MAX = 255
BLUR = False
extension = "*.jpg"


if save:
    if OSSystem == "Windows":
        os.system("rmdir /Q /S "+savepath)
        os.mkdir(savepath)
    else:
        os.system("rm -rf "+savepath+"/*")
    


subfolders = [f.path for f in os.scandir(path) if f.is_dir() ] 
print(subfolders)
    

def is_grayscale(path):

    im = Image.open(path).convert("RGB")
    stat = ImageStat.Stat(im)

    if sum(stat.sum)/3 == stat.sum[0]:
        return True
    else:
        return False

folderIdx = 0
for folder in sorted(subfolders, reverse=True):

    folderIdx = folderIdx + 1
    if folderIdx > folderDepth:
        print("Done processing reached user defined depth of %d folders" % folderDepth)
        break

    print("Processing folder [%s]" % folder)

    
    directory = os.path.join(folder, extension)
    files = sorted(glob.glob(directory))


    for file in files:
        frame = cv2.imread(file, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        avg1 = np.float32(frame)
        avg2 = np.float32(frame)

        avg3 = np.float32(frame)
     
        break
    
    avgstart = 0    
    for file in files:
        frame = cv2.imread(file, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        cv2.accumulateWeighted(frame,avg2,0.1)   
        avgstart = avgstart + 1
        res2 = cv2.convertScaleAbs(avg2)
        Background = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)


        if avgstart > 100:
            break

    res3 = res2
    # Variables for detection
    pict = 0
    processed = 0

    
    # loop over the frames of the video
    #for file in files:
    for i in range(0, len(files)):

        #print(file)
        file=files[i]

        processed += 1
        frame = cv2.imread(file, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

        text = "Unoccupied"
        
        if is_grayscale(file):
              text = "GRAYSCALE"
              grayscale = True
        else:
              text = "COLOR"
              grayscale = False
        

        #cv2.accumulateWeighted(frame,avg1,0.1)
        cv2.accumulateWeighted(frame,avg2,0.05)     #0.1 and 0.01

        #res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)


        # if the frame could not be grabbed, then we have reached the end
        # of the video

        #    if not grabbed:
        #        break

        # resize the frame, convert it to grayscale, and blur it
        #frame = imutils.resize(frame, width=500)
        if processed > 30:
            frame = cv2.imread(files[i-30], cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
            
        Current = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if BLUR:
            Current = cv2.GaussianBlur(Current, (21, 21), 0)

        Background = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
        if BLUR:        
            Background = cv2.GaussianBlur(Background, (21, 21), 0)


        # compute the absolute difference between the current frame and the background
        frameDelta = cv2.absdiff(Background, Current)
        thresh = cv2.threshold(frameDelta, TRESH_MIN, TRESH_MAX, cv2.THRESH_BINARY)[1]

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

            occupied = True

            if textboxOn:
                # compute the bounding box for the contour, draw it on the frame,
                # and update the text
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                #text = "Occupied"
    
                # Write the coordinates at the center of the blob       
                xc = x + int(w/2)
                yc = y + int(h/2)

                if x > 350:
                    xc = x - w - 50
                else: 
                    xc = x + w + 50
                
                if y > 250:
                    yc = y -h - 50
                else:
                    yc = y + h + 50
  
    
                #cv2.putText(frame, "%d %d" % (xc, yc), (xc, yc), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, "Contour size %d" % (cv2.contourArea(c)), (xc, yc), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

  
        if textboxOn:
            # draw the text and timestamp on the frame
            cv2.putText(frame, "Press 'q' to quit. Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)


        
        if occupied and grayscale == False:
            print("Found movement in : " + file)
            pict=pict+1
  
            if save:
                filephead, filetail = os.path.split(file)
                pictfile=os.path.join(savepath,filetail)
                cv2.imwrite(pictfile, frame)
  


        # show the frame
        if showframe == True:
            cv2.imshow("Thresh", thresh)
            cv2.imshow("Frame Delta",  frameDelta)
            #cv2.imshow("Frame Delta2", frameDelta2)
            cv2.imshow("Frame Delta2", res3)


            #cv2.imshow('avg1',res1)
            cv2.imshow('Background',res2)
            cv2.imshow("Processing", frame)

            key = cv2.waitKey(1) & 0xFF

            # if the `q` key is pressed, break from the lop
            if key == ord("q"):
                break
            if occupied == True and grayscale == False:
                if sleepTime:
                    time.sleep(sleepTime)

    print("Processed %d files saved %d files" % (processed,pict))
    # End of folder, process next folder in line


# cleanup the camera and close any open windows
cv2.destroyAllWindows()
