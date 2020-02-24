# Credits to :
#   https://www.twobitarcade.net/article/displaying-images-oled-displays/
#   https://github.com/robert-hh/SH1106
#   https://gist.github.com/projetsdiy/f4330be62589ab9b3da1a4eacc6b6b1c

# MicroPython SH1106 OLED driver
#
# Pin Map I2C
#   - 3v - xxxxxx   - Vcc
#   - G  - xxxxxx   - Gnd
#   - D2 - GPIO 5   - SCK / SCL
#   - D1 - GPIO 4   - DIN / SDA
#   - D0 - GPIO 16  - Res (required, unless a Hardware reset circuit is connected)
#   - G  - xxxxxx     CS
#   - G  - xxxxxx     D/C
#
# Pin's for I2C can be set almost arbitrary
#
#from machine import Pin, I2C
import sh1106
import time

import machine
import framebuf

time.sleep(3)

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))


print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))


#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, machine.Pin(16), 0x3c)
display.sleep(False)
display.fill(0)
display.text('Testing 2', 0, 0, 1)
display.show()

time.sleep(3)


with open('scatman.pbm', 'rb') as f:
    f.readline() # Magic number
    f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

display.invert(1)
display.blit(fbuf, 0, 0)
display.show()

