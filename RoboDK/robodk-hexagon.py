# Draw a hexagon around Target 1
from robolink import *    # RoboDK's API
# Copy of the example from RoboDB found @ https://robodk.com/offline-programming

from robodk import *      # Math toolbox for robots

 
# Start the RoboDK API:
RDK = Robolink()
 
# Get the robot (first robot found):
robot = RDK.Item('', ITEM_TYPE_ROBOT)
 
# Get the reference target by name:
target = RDK.Item('Target 1')
target_pose = target.Pose()
xyz_ref = target_pose.Pos()
 
# Move the robot to the reference point:
robot.MoveJ(target)
 
# Draw a hexagon around the reference target:
for i in range(7):
    ang = i*2*pi/6 # Angle = 0,60,120,...,360
    R = 200        # Polygon radius
    
    # Calculate the new position:
    x = xyz_ref[0] + R*cos(ang) # new X coordinate
    y = xyz_ref[1] + R*sin(ang) # new Y coordinate
    z = xyz_ref[2]              # new Z coordinate
    target_pose.setPos([x,y,z])
    
    # Move to the new target:
    robot.MoveL(target_pose)
 
# Trigger a program call at the end of the movement
robot.RunInstruction('Program_Done')
 
# Move back to the reference target:
robot.MoveL(target)
