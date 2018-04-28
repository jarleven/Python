# Internet Radio on the Lego EV3

## Update the system

sudo apt-get update

sudo apt-get upgrade 

## Install an MP3 player


sudo apt-get install mpg123

## Listen to the radio

	mpg123 http://stream-sd1.radioparadise.com:80/mp3-32

	mpg123 -2 -m http://lyd.nrk.no/nrk_radio_p3_mp3_l

	mpg123 -2 -m http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_l
	
	mpg123 -2 -0   or  mpg123 -2 -m   Downmix frequency and one channel only or mono  (TODO! fix this explanation)


