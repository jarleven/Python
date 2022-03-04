#!/bin/bash


: '
wget https://raw.githubusercontent.com/jarleven/Python/master/LED-Matrix/luma/setup_neopixel.sh && chmod +x setup_neopixel.sh && ./setup_neopixel.sh
'
# 
#  Tested both on Buster and Bullseye!
#

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

echo "Starting Neopixel Demo"
sudo python3 examples/neopixel_demo.py

echo "Starting MAX7219 Matrix Demo"
python3 examples/matrix_demo.py


#
# In the examples/matrix_demo.py include the ws2812 and setup the device as a ws2812 for scrolling text examples
#
# from luma.led_matrix.device import ws2812, UNICORN_HAT
# device = ws2812(width=8, height=8, mapping=UNICORN_HAT)
#
# In show message use fill="green" for green text
#
