# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:42:12 2018

@author: Jarl Even Englund
"""

import matplotlib.pyplot as plt


torange = 5
fromrange = 1
picture = 0

graphpoints = 100
increments = [1,2,4,10, 400]


def f(x):
   return(x)
 

for increment in increments:


    # The datasets
    xlist=[]
    ylist=[]

    xlinear=[]
    ylinear=[]
    
    
    # Loop the linear range
    for x in range(fromrange,(torange*graphpoints)+1):
        
        
        y = f(x/graphpoints)
        ylinear.append(y)
        xlinear.append(x/graphpoints)
    
    
    
    
    steps = torange*increment
    section = 1/increment
    
    areal = 0.0

    
    # Make the bars and sum up the area of these
    for step in range(fromrange,steps+1):
        
        x = step/increment
        xlist.append(x)
    
        y = f(x)
        ylist.append(y)

        # The area of the bars. This bar and the total area added up
        yareal = y * section
        areal = areal + yareal
    
        #print("X  %f  Y %f  Areal er %f" %  (x, y, areal))
        
   
    #print(round(areal, 3))
    
    # Mark the area you would like to frame in.
    plt.plot(xlinear,ylinear, color="blue", linewidth=2)
    plt.plot([0,torange],[0,0], color="blue", linewidth=2)
    plt.plot([torange,torange],[0,f(torange)], color="blue", linewidth=2)
    plt.plot([0,0],[0,f(0)], color="blue", linewidth=2)


    
    # Set the canvas size
    plt.xlim([-1,torange+1 ] )
    plt.ylim([-1,f(torange) + (int(f(torange) / torange) )]) 

    # Don't frame the rectangles if they are to dense !   
    if increment < 50:
        plt.bar(xlist, ylist, align='edge', width=-section, edgecolor='black', facecolor='r', alpha=.3)
    else:
        plt.bar(xlist, ylist, align='edge', width=-section, facecolor='r', alpha=.3)

    plt.ylabel('Areal = %.5f' % areal  )
    plt.title("%d rektangel" % (increment*torange))

    # Save and print the picture
    picture = picture + 1
    plt.savefig('foo%d.png' % picture)
    plt.show()
 
