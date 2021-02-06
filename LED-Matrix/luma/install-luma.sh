#!/bin/bash



sudo apt install -y python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential
sudo apt install -y libsdl-dev libportmidi-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libsdl-image1.2-dev
sudo apt install -y python3-testresources
sudo apt install -y python3-dev python3-pip build-essential

sudo -H pip3 install --upgrade --ignore-installed pip setuptools


cd ~
git clone https://github.com/rm-hull/luma.examples.git
git clone https://github.com/rm-hull/luma.core.git
git clone https://github.com/rm-hull/luma.emulator.git


cd ~/luma.core
sudo -H pip3 install -e .

cd ~/luma.examples
sudo -H pip3 install -e .

cd ~/luma.emulator
sudo -H pip3 install -e .


cd ~/luma.examples
# python3 examples/clock.py --display capture
# python3 examples/clock.py --display pygame
python3 examples/matrix.py --display pygame --transform=led_matrix --width 40 --height 16


# Further reading:
# https://tutorial.cytron.io/2018/11/22/displaying-max7219-dot-matrix-using-raspberry-pi/
