### OpenCV 

```
https://robodk.com/forum/Thread-Robotiq-Wrist-Camera

Hi Aaron,

Are you planning on driving the robot and processing images from RoboDK during production?
If not, RobotiQ have a few algorithms that can run natively on the UR. 
Take a look at their download page: https://robotiq.com/products/wrist-camera

You can also use RoboDK and OpenCV to do it yourself, for more flexibility and ease of development.
We're building up some code samples in our Python documentation that use OpenCV to process images.

Here are a few you might be interested in:
https://robodk.com/doc/en/PythonAPI/examples.html#qr-codes-and-barcodes
https://robodk.com/doc/en/PythonAPI/examples.html#object-detection

You will have to connect the wrist camera through USB on the host computer and verify that it is supported by using cv2.VideoCapture(0).

Let me know how it goes!
```
