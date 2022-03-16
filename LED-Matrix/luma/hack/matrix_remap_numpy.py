# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:05:12 2022

@author: jareng
"""


# Download this file and the mappings to run this Python script
# 
# wget https://raw.githubusercontent.com/jarleven/Python/master/LED-Matrix/luma/hack/matrix_remap_numpy.py && wget https://raw.githubusercontent.com/jarleven/Python/master/LED-Matrix/luma/hack/matrix_mapping.py
#


layout = [
         [  "A", "A", "B", "B", "A"],
         [  "B", "B", "C", "A", "A"], 
         ]

from matrix_mapping import *

mapping = {
    "A" : MAPPING_2022,
    "B" : MAPPING_2020,
    "C" : MAPPING_2020_X,
    }


import numpy as np
from pprint import pprint



# Number of pixels in the Matrix
MH = MW = 8


W=len(layout[0])
H=len(layout)

np.set_printoptions(linewidth=300)
       

# https://stackoverflow.com/questions/7115437/how-to-embed-a-small-numpy-array-into-a-predefined-block-of-a-large-numpy-arra

def paste_slices(tup):
  pos, w, max_w = tup
  wall_min = max(pos, 0)
  wall_max = min(pos+w, max_w)
  block_min = -min(pos, 0)
  block_max = max_w-max(pos+w, max_w)
  block_max = block_max if block_max != 0 else None
  return slice(wall_min, wall_max), slice(block_min, block_max)

def paste(wall, block, loc):
  loc_zip = zip(loc, block.shape, wall.shape)
  wall_slices, block_slices = zip(*map(paste_slices, loc_zip))
  wall[wall_slices] = block[block_slices]


def checkMatrix(matrix, H, W):
    numbers = np.array(matrix)
    mUnique=len(np.unique(matrix))
    mMax=numbers.max()
    mMin=numbers.min()
    matrixpixels=MH*MW
    if (mUnique != matrixpixels*H*W or mMax !=  matrixpixels*H*W -1 or mMin != 0 ):
        print("Unique valuse: %2d, should be %d" % (mUnique, matrixpixels*H*W))
        print("Max value    : %2d, should be %d" % (mMax, matrixpixels*H*W -1))
        print("Min value    : %2d, should be  0" % mMin)
        print("")
        
        unique, counts = np.unique(matrix, return_counts=True)
        pprint(dict(zip(unique, counts)))
        #print(collections.Counter(numbers))
        print("")
        #pprint(matrix)
        
    else:
        print(" #   Matrix OK  min:%d / max:%d / unique:%d" % (mMin, mMax, mUnique)) 
        
        
        

# Create a matrix with 1:1 mapping of the pixels
base = np.arange(0,MH*MW*H*W).reshape(W*MW, H*MH)
base = np.flip(base, axis=0)
base = np.rot90(base, k=3, axes=(0, 1)) 

# Create a temporary matrix to paste the transformed 8x8 matrixes into
wall = np.zeros((H*MH, W*MW),dtype=int)

print("")
print(base)
print("")

print(wall)
print("")

print("W and H")
print("w=%d h=%d" % (W, H) ) 
print("---")


#
# Main part
#
# Go through each 8x8 matrix and move the transformed pixels to the "wall"
# The pixels on the "base" is transformed as described in each 8x8 mapping
for h in range(H):
    
    for w in range(W):
        
        SW=w*MW             #   Start based on size of matrix
        SH=h*MH             #   Start based on size of matrix
        
        c=SW                #   Start Vertical
        d=SW+MW             #   End (-1 )
        
        a=SH                #   Start Horisontal
        b=SH+MH             #   End -1
        
        a_slice = base[a:b, c:d]

        mMapping = layout[h][w]
        A = np.array(mapping[mMapping])
        
        aM = A.flatten()
        bM=a_slice.flatten()
        cM = bM[np.argsort(aM)]
        C = np.reshape(cM,(MH,MW))

 
        paste(wall, C, (a, c))
        
        """
        print("+++++++++++++++++++++")

        print("%d:%d, %d:%d    w=%d h=%d" % (a, b, c, d, w, h) ) 

        print ("Remap %s   " % mMapping, end="")
        print(aM)

        print(wall)
        print("+++++++++++++++++++++")
        """

print("Final WALL")
pprint(wall)

print("")
print("")


#
#  Print the list for copy/pasting into your Luma Python program
#
print("MY_LAYOUT = [")

for h in range(H*MH):
    
    print("          ", end="")
    for w in range(W*MW):

        print("%3d, " % (wall[h][w]), end=" ")
        if (w+1)%MW == 0:
            print("  ", end="")
    
    print("")
    if (h+1)%MH == 0:
        print("  ")
    

print("             ]")



       

# Check sanity of the new pixel mapping
#   Starts @ 0
#   Number of pixels 8x8 x number of matrixes
#   Same pixelID is not used two times (all are unique)
checkMatrix(wall, H, W)

print("")

print(" #")
print(" #   Matrix layout : ")
print(" #   Width = %d   Height = %d" % (W, H))

for h in range(H):
    print(" #       ", end="")
    for w in range(W):

        mMapping = layout[h][w]
        print ("%s " % mMapping, end="")
    print("")

print("")
print("device = ws2812(width=%d, height=%d, mapping=MY_MAPPING)" % ( MW*len(layout[0]), MH*len(layout) ) )
print("device = max7219(width=%d, height=%d, mapping=MY_MAPPING)" % ( MW*len(layout[0]), MH*len(layout) ) )


print("")   
print(" # Note that the /usr/local/bin/... decice.py must be patched with :")
print(" # https://github.com/jarleven/Python/blob/master/LED-Matrix/luma/hack/device.py")
