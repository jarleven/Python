# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:13:10 2022

@author: jareng
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:42:47 2022

@author: jareng
"""

debugline=False

layout = [
         [  0, 1, 2 ],
         [  3, 4, 5 ] 
         ]

"""
layout = [
         [  0 ],
         ]

layout = [
         [  0, 1 ]
         ]





layout = [
         [  0 ],
         [  1 ]
         ]
"""

# The UNICORN_HAT snake layout
base =  [
        [  7,   6,   5,   4,   3,   2,   1,   0 ],
        [ 15,  14,  13,  12,  11,  10,   9,   8 ], 
        [ 23,  22,  21,  20,  19,  18,  17,  16 ], 
        [ 31,  30,  29,  28,  27,  26,  25,  24 ], 
        [ 39,  38,  37,  36,  35,  34,  33,  32 ], 
        [ 47,  46,  45,  44,  43,  42,  41,  40 ], 
        [ 55,  54,  53,  52,  51,  50,  49,  48 ], 
        [ 63,  62,  61,  60,  59,  58,  57,  56 ]
        ]

print("")
print("")
print("")
print("#  Neopixel matrix layout ")
print("#")


for i in layout:
    print("#     ", end="" )
    for x in range(len(i)):
        print(i[x]," ", end="" )
    print("")

print("#")
print("")

print("#    :param mapping: An (optional) array of integer values that translate the")
print("#            pixel to physical offsets. If supplied, should be the same size as")
print("#            ``width * height``")

print("")
print("MY_MAPPING = [")



def transformRow(row, matrix):
    
    offset=64*matrix
    offset_list = [element + offset for element in base[row]]
    
    for d in offset_list:
        print("%3d, " % d, end="")

    if debugline:
        print("- ", end="") # Debug line



for i in layout:

    for row in range(8):
        print("               ", end="")

        for x in range(len(i)):
            transformRow(row, i[x])
        print("")

    if debugline:
        print("")   # Debug line

print("            ]")
    

#print(len(layout[0]))
#print(len(layout))
      
width=8*len(layout[0])
height=8*len(layout)

print("")
print("device = ws2812(width=%d, height=%d, mapping=MY_MAPPING)" % (width, height))


# 

