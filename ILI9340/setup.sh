#!/bin/bash

#from PIL import Image
#print statements

cd ~

sudo apt update
sudo apt upgrade -y
sudo apt install -y vim git

sudo apt install -y build-essential libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5
sudo apt install -y python3 python3-pip python3-dev python3-smbus python3-pil python3-numpy

sudo apt install -y 2to3


python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

# Should work on Linux
#easy_install Pillow 

#Installing collected packages: pip
#  WARNING: The scripts pip, pip3 and pip3.9 are installed in '/home/pi/.local/bin' which is not on PATH.
#  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.



sudo raspi-config nonint do_spi 0
sudo usermod -a -G spi,gpio pi

git clone https://github.com/Funkrusha/Adafruit_Python_ILI9340.git

python3 -m pip install --upgrade Adafruit_ILI9341



cd Adafruit_Python_ILI9340/examples

# This example is Python2 so let us update it
2to3 -w image.py

python3 image.py

wget https://raw.githubusercontent.com/jarleven/Python/master/ILI9340/image.py

 wget https://images.hdqwalls.com/walls/thumb/pokemon-detective-pikachu-poster-5k-lc.jpg -O pikachu.jpg
 wget https://images.hdqwalls.com/walls/thumb/ninetales-one-more-pokemon-pu.jpg -O ninetales.jpg


# Connecting as instructed in this example : https://github.com/Funkrusha/Adafruit_Python_ILI9340/blob/master/examples/image.py
: '
```Bash

	           3V3  (1) (2)  5V		    VCC
	         GPIO2  (3) (4)  5V			  
	         GPIO3  (5) (6)  GND		  GND
	         GPIO4  (7) (8)  GPIO14
	           GND  (9) (10) GPIO15
	        GPIO17 (11) (12) GPIO18
	        GPIO27 (13) (14) GND
	        GPIO22 (15) (16) GPIO23		RESET
	           3V3 (17) (18) GPIO24
MOSI		GPIO10 (19) (20) GND
MISO		 GPIO9 (21) (22) GPIO25		D/C
SCK		GPIO11 (23) (24) GPIO8		LCD CS
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
