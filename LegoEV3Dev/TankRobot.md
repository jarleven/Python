## A project to set up a tank
### 2x Ev3, Dualshock 4, Raspberry Pi and a camera




JOYSTICK
******************************************************************
sudo apt install python3
sudo apt install bluez
sudo apt install -y python3-pip
python3 -m pip install --upgrade --user pip 
python3 -m pip install --upgrade --force-reinstall --user ds4drv

sudo apt install python-pygame
sudo pip3 install ds4drv

sudo ds4drv



Thanks wiredtouch14
https://www.youtube.com/watch?v=1EYtZC2iVzc


export DISPLAY=:0

https://www.pygame.org/docs/ref/joystick.html


RPi
************************************************'





EV3 https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html
**********************************************

sudo apt update
sudo apt upgrade

sudo easy_install3 rpyc

echo "#!/bin/bash" > rpyc_server.sh
echo "python3 `which rpyc_classic.py`" >> rpyc_server.sh

chmod +x rpyc_server.sh




#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

sudo apt install -y python3

sudo apt install -y python3-pip
python3 -m pip install --upgrade --user pip
python3 -m pip install --user rpyc


