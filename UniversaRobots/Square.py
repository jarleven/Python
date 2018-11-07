import urx

rob = urx.Robot("192.168.1.114")

#Movements are in centimeters as we divide by 100 in the movel commands 

# movel((x,y,z,rx,ry,rz, acceleration, velocity, relative=True, wait=True)

# Pen down
z=-0.7
zmove=z/100
rob.movel((0, 0, zmove, 0, 0, 0), 0.01, 0.05, relative=True, wait=True))  # move relative to current pose
    
# The X/Y dimmentions of the rectangle we will draw
x=[-10,  0, 10, 0]
y=[ 0,  -3, 0,  3] 

# Draw the rectangle in the X,Y plane
for i in range(0,4):
    xmove=x[i]/100
    ymove=y[i]/100
    rob.movel((xmove, ymove, 0, 0, 0, 0), 0.01, 0.05, relative=True, wait=True)  # move relative to current pose

# Pen up
z=.7
zmove=z/100
rob.movel((0, 0, zmove, 0, 0, 0), 0.01, 0.05, relative=True, wait=True))  # move relative to current pose
        
