# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:36:28 2023

@author: jareng
"""


#
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   |   | █   █ |   |   |   |   0x18
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   |   | █   █ |   |   |   |   0x18
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   | █ | █   █ |   |   |   |   0x38
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   |   | █   █ |   |   |   |   0x18
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   |   | █   █ |   |   |   |   0x18
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   |   | █   █ |   |   |   |   0x18
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   | █ | █ | █   █ | █ | █ |   |   0x7E
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#     |   |   |   |   |   |   |   |   |
#     |   |   |   |       |   |   |   |   0x00
#     |   |   |   |   |   |   |   |   |
#     ---------------------------------
#
#
#

#    THE INTERESTING WRITING TO THE SPI BUS / MAX7219 IS DONE BELOW
#    https://www.instructables.com/Raspberry-Pi-Pico-MAX7219-8x8-Dot-Matrix-Scrolling/
#
#    def show(self):
#        for y in range(8):
#            self.cs(0)
#            for m in range(self.num):
#                self.spi.write(bytearray([_DIGIT0 + y, self.buffer[(y * self.num) + m]]))
#            self.cs(1)


#   self.spi.write(bytearray[line,value]) is responsible for writing data to the MAX7291 chip
#
#    def show(self):
#        for y in range(8):
#            self.cs(0)
#            for m in range(self.num):
#
#                line = _DIGIT0 + y
#                value = self.buffer[(y * self.num) + m]
#                print("linje %d  verdi 0x%02x  " % (line, value))
#                self.spi.write(bytearray([line, value]))
#            self.cs(1)





input = [0x18, 0x3c, 0x3c, 0x06, 0x18, 0x66, 0x66, 0x0e, 0x38, 0x06, 0x06, 0x1e, 0x18, 0x0c, 0x1c, 0x66, 0x18, 0x30, 0x06, 0x7f, 0x18, 0x60, 0x66, 0x06, 0x7e, 0x7e, 0x3c, 0x06, 0x00, 0x00, 0x00, 0x00]
num_matrixes = int(len(input)/8)



print("")
print("")

# Print input buffer as ASCII art
for m in range(num_matrixes):
    for i in range(8):
        
        a=input[i*num_matrixes + m]    
    
        for x in range(8):
            if(a & (1 << (7-x))):
                print("█", end="")
            else:
                print("-", end="")
        print(" 0x%02x" % a)
    
    
    print("")



for y in range(8): # Loop through each line
    
    for m in range(num_matrixes):  # Cascade of matrixes

        out = 0
        for z in range(8):
            
            fbindex = (z * num_matrixes) + m
            value = input[fbindex]
   
            if(value & 0x01 << y):          # Test if bit is set
                out = out | (0x80 >> z)     # Create a new byte from each bit
                print("█", end="")
            else:
                print("|", end="")
        print(" 0x%02x " % out, end=(""))
                
    print("")
print("")






"""

    def show(self):
      
        for y in range(8): # Linje num
            
            self.cs(0)
            for m in range(self.num):  # Matrise num

#                for z in range(8): # Linje num
#                    
#                    fbindex = (z * self.num) + m
#                    value = self.buffer[fbindex]
#                    print("matrix  0x%02x %s" % (value, '{:08b}'.format(value)))
#                print("")
#                print("Bit number %d" % y)
  
                # Read out the 8xbytes intended for ONE matrix
                # y is the line being written to the Matrix
                # m is the matrix being written
                # z is for reading one matrix and we use the y/line variable to get the transposed byte for this matrix
      
                out = 0
                for z in range(8): # Linje num
                    
                    fbindex = (z * self.num) + m
                    value = self.buffer[fbindex]
       
                    if(value & 0x80 >> y):
                        out = out | (0x80 >> z)
#                        print("1", end="")
#                    else:
#                       print("0", end="")


#                print(" transposed 0x%02x" % out)
#                print("FBid %02d FBval 0x%02x " % (fbindex, value ), end="")
                self.spi.write(bytearray([_DIGIT0 + y, out]))
#            print("")
            self.cs(1)


"""
