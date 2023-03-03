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




input = [0x18, 0x18, 0x38, 0x18,  0x18, 0x18, 0x7E, 0x00]
input = [0x3c, 0x66, 0x06, 0x0c,  0x30, 0x60, 0x7e, 0x00 ]

input = [0x18,0x3c,  0x18,0x66,  0x38,0x06,  0x18,0x0c,  0x18,0x30,  0x18,0x60, 0x7e,0x7e,  0x00,0x00 ]


print("")


# Print contents of input buffer in HEX format
for i in range(8):
        print("  0x%02x" % input[i])    
    

print("")

# Print input buffer as ASCII art
for i in range(8):

    for num in range(2):
    
        a=input[i*2 + num]    
    
        for x in range(8):
            if(a & (1 << (7-x))):
                print("█", end="")
            else:
                print("-", end="")
    print("")


print("")


output = [0x00, 0x00, 0x00, 0x00,  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  0x00, 0x00, 0x00, 0x00]    




line = [0x01, 0x08]


# Print input buffer as ASCII art
for i in range(8):

    a=line[0]
    b=line[1]    
    for x in range(8):
        if(a & (1 << (7-x))):
            print("█", end="")
        else:
                print("|", end="")

        if(b & (1 << (7-x))):
            print("█", end="")
        else:
                print("|", end="")


    print("")


print("")


input = [0x18, 0x18, 0x38, 0x18,  0x18, 0x18, 0x7E, 0x00]
input = [0x18,0x3c,  0x18,0x66,  0x38,0x06,  0x18,0x0c,  0x18,0x30,  0x18,0x60, 0x7e,0x7e,  0x00,0x00 ]


# id is the matrix we read
def rotate_array(array, numarray, line, id):
    
    print("Return first bit from every byte in the matrix")

    out = 0
    for i in range (8):
    
        a=array[i*numarray + id]
        print("  0x%02x  " % a, end="") 

        if(a & 0x80 >> line):
            print("1", end="")
            out = out | 0x80 >> i
        else:
           print("0", end="")

        print("")
        print("0x%02x" % out)
    
    for w in range (8):

        
        if(line & 0x80 >> w):
        #if(line & 0x01 << w):

            
            print("1", end="")
        
            #output[w] = output[w] | (0x80 >> z)
            output[w] = output[w] | (0x01 << z)

        else:
            print("0", end="")
            
    print("")


print("")



rotate_array(input, 1, 3, 1)



exit()



# Rotate the input buffer and put the rotated bitfields in the output buffer
for z in range(8):

    line = input[z]
    
    
    # Set each bit in output from line
    
    # z : Input byte index  / Bit number for output
    # w : Bit number for input / output buffer byte index

    for w in range (8):

        
        if(line & 0x80 >> w):
        #if(line & 0x01 << w):

            
            print("1", end="")
        
            #output[w] = output[w] | (0x80 >> z)
            output[w] = output[w] | (0x01 << z)

        else:
            print("0", end="")
            
    print("")


print("")


# Print output buffer as ASCII art
for i in range(8):
    
    a=output[i]    

    for x in range(8):
        if(a & (1 << (7-x))):
            print("█", end="")
        else:
            print("|", end="")
    print("")


print("")

# Print contents of the output buffer in HEX format
for i in range(8):
        print("  0x%02x" % output[i])   

