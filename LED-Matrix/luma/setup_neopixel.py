#!/bin/bash


: '
wget https://raw.githubusercontent.com/jarleven/flaskapp/main/luma/setup_neopixel.sh && chmod +x setup_neopixel.sh && ./setup_neopixel.sh
'
# 
# https://downloads.raspberrypi.org/raspios_oldstable_lite_armhf/images/raspios_oldstable_lite_armhf-2022-01-28/2022-01-28-raspios-buster-armhf-lite.zip
# This is atleast working on Buster !

cd ~

sudo apt update
sudo apt upgrade -y
sudo apt install -y vim git


sudo apt install -y build-essential libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5
sudo apt install -y python3 python3-pip python3-dev

sudo raspi-config nonint do_spi 0
sudo usermod -a -G spi,gpio pi

git clone https://github.com/rm-hull/luma.led_matrix.git

sudo pip3 install luma.led-matrix
cd luma.led_matrix/

sudo python3 examples/neopixel_demo.py

#
# In the examples/matrix_demo.py include the ws2812 and setup the device as a ws2812 for scrolling text examples
#
# from luma.led_matrix.device import ws2812, UNICORN_HAT
# device = ws2812(width=8, height=8, mapping=UNICORN_HAT)
#
# In show message use fill="green" for green text
#

: '
```Bash

			   3V3  (1) (2)  5V			2 VCC
			 GPIO2  (3) (4)  5V			  
			 GPIO3  (5) (6)  GND			6 GND
			 GPIO4  (7) (8)  GPIO14
			   GND  (9) (10) GPIO15
			GPIO17 (11) (12) GPIO18			(12 Neopixel DI)
			GPIO27 (13) (14) GND
			GPIO22 (15) (16) GPIO23
			   3V3 (17) (18) GPIO24
   	DIN 19		GPIO10 (19) (20) GND
			 GPIO9 (21) (22) GPIO25
     	CLK 23		GPIO11 (23) (24) GPIO8			24 Enable/CS
			   GND (25) (26) GPIO7
			 GPIO0 (27) (28) GPIO1
			 GPIO5 (29) (30) GND
			 GPIO6 (31) (32) GPIO12
			GPIO13 (33) (34) GND
			GPIO19 (35) (36) GPIO16
			GPIO26 (37) (38) GPIO20
			   GND (39) (40) GPIO21

```
'

echo ""
echo "https://luma-led-matrix.readthedocs.io/_/downloads/en/stable/pdf/"
echo "Note: The ws2812 driver uses the ws2812 PyPi package to interface to the daisychained LEDs. It uses DMA (direct"
echo "memory access) via /dev/mem which means that it has to run in privileged mode (via sudo root access)."

