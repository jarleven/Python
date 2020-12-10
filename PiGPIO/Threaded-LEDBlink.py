# Make some blinking LEDs from this example

#https://stackoverflow.com/questions/43892334/python-raspberry-pi-call-a-task-avery-10-milliseconds-precisely

import threading

def work (): 
  threading.Timer(0.25, work).start ()
  print(time.time())
  print "stackoverflow"

work ()
