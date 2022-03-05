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
