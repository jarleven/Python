```

		 VCC  GND
		 VCC  GND
		 VCC  GND
		LOAD  CLK
		 DIN  ---

        2x5 Connector on the LED matrix
  
 
 
 

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
     	CLK 23		GPIO11 (23) (24) GPIO8			24 Load/Enable/CS
			   GND (25) (26) GPIO7
			 GPIO0 (27) (28) GPIO1
			 GPIO5 (29) (30) GND
			 GPIO6 (31) (32) GPIO12
			GPIO13 (33) (34) GND
			GPIO19 (35) (36) GPIO16
			GPIO26 (37) (38) GPIO20
			   GND (39) (40) GPIO21



```

```
https://luma-led-matrix.readthedocs.io/_/downloads/en/stable/pdf/"
Note: The ws2812 driver uses the ws2812 PyPi package to interface to the daisychained LEDs. It uses DMA (direct"
memory access) via /dev/mem which means that it has to run in privileged mode (via sudo root access)."
```
