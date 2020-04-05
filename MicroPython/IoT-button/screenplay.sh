#!/bin/bash


##############################################
##
## Stream the screen of your PC to an 128x64 monocrome OLED 
##
## https://imagemagick.org/script/formats.php
##
##


# Default values
fn=""
ip="192.168.2.228"
p="21567"
ng="yes"
dl="3"

# Parse the input parameters
while [ $# -gt 0 ] ; do
  case $1 in
    --file)   fn="$2" ;;
    --host)   ip="$2" ;;
    --port)    p="$2" ;;
    --negate) ng="$2" ;;
    --delay)  dl="$2" ;;
  esac
  shift
done




# TODO combine the file and IP version
# Need either IP or filename

if [ -z "$ip" ]
then
	echo "Specify IP addr"
	exit
fi

if [ $ng = "yes" ]
then
	echo "Invert image"
	negate="-negate"
elif [ $ng = "no" ]
then
        echo "No invert"
        negate=""
fi


# We are doing screenshots so specify our own filename

fn="cap.png"
base=${fn%%.*}

echo "Working on file "$base".*"

output="small"$base

echo "$base     $output" 



while :
do

	# Take a fullscreen screenshot
	scrot $fn

	echo "Screenshot sending it to $ip:$p every $dl seconds"
	echo "Negate var ["$negate"]"

	convert $fn -resize 128x64^ -gravity Center -extent 128x64 $output".jpg"

	convert $output".jpg" -type bilevel -depth 1 $negate $output".pbm"

	convert $output".pbm" $output".pnm"

	# This does not work !
	#convert $output".pbm" $output".mono"

	# Just remove the two first lines of the .pnm image header
	python pnm2bin.py $output".pnm"

	cat $output".bin" | nc -u $ip $p -w 0

	sleep $dl
done
