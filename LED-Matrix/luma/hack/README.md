### A few hacks


```Python
# Layout from 2020 followed by layout from 2022
# Two cascaded matrixes with individual different LED/pixel layout

MY_MAPPING = [
        63,  62,  61,  60,  59,  58,  57,  56,  64,  72,  80,  88,  96, 104, 112, 120, 
        55,  54,  53,  52,  51,  50,  49,  48,  65,  73,  81,  89,  97, 105, 113, 121, 
        47,  46,  45,  44,  43,  42,  41,  40,  66,  74,  82,  90,  98, 106, 114, 122, 
        39,  38,  37,  36,  35,  34,  33,  32,  67,  75,  83,  91,  99, 107, 115, 123, 
        31,  30,  29,  28,  27,  26,  25,  24,  68,  76,  84,  92, 100, 108, 116, 124, 
        23,  22,  21,  20,  19,  18,  17,  16,  69,  77,  85,  93, 101, 109, 117, 125, 
        15,  14,  13,  12,  11,  10,   9,   8,  70,  78,  86,  94, 102, 110, 118, 126, 
         7,   6,   5,   4,   3,   2,   1,   0,  71,  79,  87,  95, 103, 111, 119, 127, 
    ]


device = max7219(serial, width=16, height=8, mapping=MY_MAPPING)




```


```Python

MAPPING_2020 = [
        [ 63, 62, 61, 60, 59, 58, 57, 56 ], 
        [ 55, 54, 53, 52, 51, 50, 49, 48 ], 
        [ 47, 46, 45, 44, 43, 42, 41, 40 ], 
        [ 39, 38, 37, 36, 35, 34, 33, 32 ], 
        [ 31, 30, 29, 28, 27, 26, 25, 24 ], 
        [ 23, 22, 21, 20, 19, 18, 17, 16 ], 
        [ 15, 14, 13, 12, 11, 10,  9,  8 ], 
        [  7,  6,  5,  4,  3,  2,  1,  0 ], 
    ]

MAPPING_2022 = [
        [ 0,  8, 16, 24, 32, 40, 48, 56 ], 
        [ 1,  9, 17, 25, 33, 41, 49, 57 ], 
        [ 2, 10, 18, 26, 34, 42, 50, 58 ], 
        [ 3, 11, 19, 27, 35, 43, 51, 59 ], 
        [ 4, 12, 20, 28, 36, 44, 52, 60 ], 
        [ 5, 13, 21, 29, 37, 45, 53, 61 ], 
        [ 6, 14, 22, 30, 38, 46, 54, 62 ], 
        [ 7, 15, 23, 31, 39, 47, 55, 63 ],    
    ]     

# The UNICORN_HAT snake layout
UNICORN =  [
        [  0,  1,  2,  3,  4,  5,  6,  7 ],
        [ 15, 14, 13, 12, 11, 10,  9,  8 ], 
        [ 23, 22, 21, 20, 19, 18, 17, 16 ], 
        [ 31, 30, 29, 28, 27, 26, 25, 24 ], 
        [ 39, 38, 37, 36, 35, 34, 33, 32 ], 
        [ 47, 46, 45, 44, 43, 42, 41, 40 ], 
        [ 55, 54, 53, 52, 51, 50, 49, 48 ], 
        [ 63, 62, 61, 60, 59, 58, 57, 56 ]
    ]

```

```Python

    def preprocess(self, image):
        """
        The pixels are remapped according to the layout of the cascaded matrix.
        """
        image = super(max7219, self).preprocess(image)
        
        
        if self._mapping is not None:
            layout=self._mapping
      
            new_image = image.copy()
          
            width  = new_image.width
            height = new_image.height
            pixelId=0
            
            for x in range(width):
                for y in range(height):
                    pixelval = image.getpixel((x,y))

                    mappedpos = layout.index(pixelId)
                    Oy = int(mappedpos/width)
                    Ox = mappedpos%width 

                    new_image.putpixel((Ox, Oy), (pixelval))
                    pixelId = pixelId+1
            return new_image
```
