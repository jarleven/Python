import urx
import time

rob = urx.Robot("192.168.1.114")

Movements are in centimeters as we divide by 100 in the movel commands 

# Pen down
z=-0.48
rob.movel((0, 0, z/100, 0, 0, 0), 0.01, 0.05, relative=True)  # move relative to current pose
    
# The X/Y dimmentions of the rectangle we will draw
x=[-10,  0, 10, 0]
y=[ 0,  -3, 0,  3] 

# Draw the rectangle in the X,Y plane
for i in range(0,4):
    rob.movel((x[i]/100, y[i]/100, 0, 0, 0, 0), 0.01, 0.05, relative=True, wait=True)  # move relative to current pose

# Pen up
z=.48
rob.movel((0, 0, z/100, 0, 0, 0), 0.01, 0.05, relative=True)  # move relative to current pose
        
