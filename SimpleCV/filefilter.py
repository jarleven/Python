# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 01:43:11 2018
 
@author: jareng
"""

# Loop jpg in all subfolders

import os
import glob

from matplotlib import pyplot as plt
import cv2
import shutil

extension = "*.jpg"

homedir = os.getenv("HOME")
print(homedir)

#path = homedir+"/Dropbox"

path = homedir+"/GrabberArchive"
outpath = homedir+"/workdir"

# Measure points in the histogram
histrange = 256

# Delete dark/bright folders if they exist
dirbright = path+ "/bright"
dirdark = path+ "/dark"


if os.path.exists(outpath):
    os.system("rm -rf "+outpath)

subfolders = [f.path for f in os.scandir(path) if f.is_dir() ] 
print(subfolders)

for folder in sorted(subfolders):

    # Make the directory for processing bright and dark images
    phead, ptail = os.path.split(folder)

    darkpath = outpath+"/dark/"+ptail

    print(darkpath)
    os.makedirs(darkpath)

    brightpath = outpath+"/bright/"+ptail

    print(brightpath)
    os.makedirs(brightpath)

    directory = os.path.join(folder, extension)
    files = glob.glob(directory)

    for file in sorted(files):

        print(file)
        __, filename = os.path.split(file)

        image = cv2.imread(file)

        # convert the image to grayscale and create a histogram
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Make a histogram
    hist = cv2.calcHist([gray], [0], None, [histrange], [0, histrange])
    #    
    # Do some math on the histogram
    # Compare bright side to the right with dark side on the left
    brightpixels = 0
    darkpixels = 0

    i = 0
    while i < len(hist):
        if (i < (histrange/2)):
            darkpixels = darkpixels + hist[i]
        else:
            brightpixels = brightpixels + hist[i]
            i = i + 1

        print("Dark %d vs light %d" % (darkpixels, brightpixels))

        if (brightpixels > darkpixels):
            fdest = brightpath+"/"+filename
            shutil.copyfile(file, fdest)
            #print(fdest)    

        else:
            fdest = darkpath+"/"+filename
            #print(fdest)
            shutil.copyfile(file, fdest)

    #__, filename = os.path.split(file)
    #print(filename)

