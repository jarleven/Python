layout=MY_MAPPING


height=8
width=8

for element in range(height*width):
    
    #index_row = [layout.index(row) for row in layout if element in row]

    #index_column = [row.index(element) for row in layout if element in row]
    remappedpos = layout.index(element)
    pixelPosOut_h = int(remappedpos/height)
    pixelPosOut_w = remappedpos%width 
    
    pixelPosIn_h = int(element/height)
    pixelPosIn_w = element%width
    
    #imageIn = image
    #pixelval = imageIn.pixel(pixelPosIn_h, pixelPosIn_w)
    #image[pixelPosOut_h, pixelPosOut_w] = pixelval
    
    
    print("pixel %2d h/w  %2d/%2d   --  out pixel %2d h/w  %2d/%2d" % (element, pixelPosIn_h, pixelPosIn_w, remappedpos, pixelPosOut_h, pixelPosOut_w ))

    #print(layout)




MY_MAPPING = [
                 7,   6,   5,   4,   3,   2,   1,   0, 
                15,  14,  13,  12,  11,  10,   9,   8, 
                23,  22,  21,  20,  19,  18,  17,  16, 
                31,  30,  29,  28,  27,  26,  25,  24, 
                39,  38,  37,  36,  35,  34,  33,  32, 
                47,  46,  45,  44,  43,  42,  41,  40, 
                55,  54,  53,  52,  51,  50,  49,  48, 
                63,  62,  61,  60,  59,  58,  57,  56, 
            ]
