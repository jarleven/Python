# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from PIL import Image
import time

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

PITFT_2_8 = 18
PITFT_2_2 = 25

CURRENT_PITFT = PITFT_2_2

# Raspberry Pi configuration.
DC = CURRENT_PITFT
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0

# BeagleBone Black configuration.
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()

#
# Draw a green screen with a red line on it
# https://stackoverflow.com/questions/13053443/drawing-a-line-on-an-image-with-pil
from PIL import Image, ImageDraw
im = Image.new('RGBA', (240, 320), (0, 255, 0, 0)) 
draw = ImageDraw.Draw(im) 
draw.line((100,200, 150,300), fill=128)
disp.display(im)
time.sleep(5)


# Load an image.
print('Loading image...')
#image = Image.open('cat.jpg')
image1 = Image.open('pikachu.jpg')

# Resize the image and rotate it so it's 240x320 pixels.
image1 = image1.rotate(0).resize((240, 320))

print('Loading image...')
image2 = Image.open('ninetales.jpg')
# Resize the image and rotate it so it's 240x320 pixels.
image2 = image2.rotate(0).resize((240, 320))


while True:

    # Draw images on the display.

    print('Drawing image')
    disp.display(image1)
    time.sleep(5)

    print('Drawing image')
    disp.display(image2)
    time.sleep(5)

