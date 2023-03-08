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
#
#    https://www.instructables.com/Raspberry-Pi-Pico-MAX7219-8x8-Dot-Matrix-Scrolling/
#
#   self.spi.write(bytearray[line,value]) is responsible for writing data to the MAX7291 chip


#
#    def show(self):
#        for y in range(8):
#            self.cs(0)
#            for m in range(self.num):
#                self.spi.write(bytearray([_DIGIT0 + y, self.buffer[(y * self.num) + m]]))
#            self.cs(1)


#
#    def show(self):
#        for y in range(8):
#            self.cs(0)
#            for m in range(self.num):
#
#                line = _DIGIT0 + y
#                value = self.buffer[(y * self.num) + m]
#                print("line %d  value 0x%02x  " % (line, value))
#                self.spi.write(bytearray([line, value]))
#            self.cs(1)



#
#    def show(self):
#        for y in range(8): # Line number
#            self.cs(0)
#            for m in range(self.num):  # Matrix number
#
#                # Read all data in one matrix 64 LEDs, and modify one line to be written 8 LEDs  
#                out = 0
#                for z in range(8): # Linje num
#                    
#                    fbindex = (z * self.num) + m
#                    value = self.buffer[fbindex]
#       
#                    if(value & 0x80 >> y):
#                        out = out | (0x80 >> z)
#
#                self.spi.write(bytearray([_DIGIT0 + y, out]))
#            self.cs(1)




buffer = [0x18, 0x3c, 0x3c, 0x06, 0x18, 0x66, 0x66, 0x0e, 0x38, 0x06, 0x06, 0x1e, 0x18, 0x0c, 0x1c, 0x66, 0x18, 0x30, 0x06, 0x7f, 0x18, 0x60, 0x66, 0x06, 0x7e, 0x7e, 0x3c, 0x06, 0x00, 0x00, 0x00, 0x00]

buffer = [0xff, 0x80, 0x80, 0x01,   0x00, 0x80, 0x40, 0x02,   0x00, 0x80, 0x20, 0x04,   0x00, 0x80, 0x10, 0x08,   0x00, 0x80, 0x08, 0x10,   0x00, 0x80, 0x04, 0x20,   0x00, 0x80, 0x02, 0x40,   0x00, 0x80, 0x01, 0x80]

num = int(len(buffer)/8)


###
# Print one byte as ASCII-art bitmap
#
# ---██--- 0x18
# ---██--- 0x18
# --███--- 0x38
# ---██--- 0x18
# ---██--- 0x18
# ---██--- 0x18
# -██████- 0x7e
# -------- 0x00
# 
def write_byte(value):
    
    for i in range(8):
   
        if(value & 0x80 >> i):          # Test if bit is set
            print("█", end="")
        else:
            print("-", end="")

    print(" 0x%02x " % value, end=(""))


print("")
print("")


###
# Print Matrix original orientation
#
for y in range(8): # Loop through each line
    
    for m in range(num):  # Cascade of matrixes

        value=buffer[(y*num) + m]    

        write_byte(value)
    print("")
print("")




###
# Print Matrix rotated clockwise
#
for y in range(8): # Loop through each line
    
    for m in range(num):  # Cascade of matrixes

        # Loop through one matrix 8 byte (64 bit)
        # Return one byte in the "out" variable. "out" represents one line created from one column 
        out = 0
        for z in range(8):

            value=buffer[z*num + m]    
   
            if(value & 0x01 << y):          # Test if bit is set
                out = out | (0x80 >> z)     # Create a new byte from each bit in the column
        write_byte(out)
                
    print("")
print("")




luty = [0,1,2,3,4,5,7,6] # Row 
lutz = [1,0,2,3,4,5,6,7] # Column

###
# Print Matrix rotated counter-clockwise
#
for y in range(8): # Loop through each line
    
    for m in range(num):  # Cascade of matrixes

        # Loop through one matrix 8 byte (64 bit)
        # Return one byte in the "out" variable. "out" represents one line created from one column 
        out = 0
        for z in range(8):

            value=buffer[z*num + m]    
   
            yy = luty[y]
            if(value & 0x01 << yy):          # Test if bit is set
                zz = lutz[z]
                out = out | (0x80 >> zz)     # Create a new byte from each bit in the column
        write_byte(out)
                
    print("")
print("")



