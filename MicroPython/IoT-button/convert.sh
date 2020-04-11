#!/bin/bash


# sudo apt install imagemagick


fn=""
ip=""
ng=""


while [ $# -gt 0 ] ; do
  case $1 in
    --file) fn="$2" ;;
    --host) ip="$2" ;;
    --negate) ng="$2" ;;
  esac
  shift
done


if [ -z "$ip" ]
then
	echo "Specify IP addr"
	exit
fi

if [ -z "$fn" ]
then
        echo "Specify file"
        exit
fi


if [ -z "$ng" ]
then
        echo "No invert"
        negate=""
else
	echo "Invert image"
	negate="-negate"
fi

echo "Negate var ["$negate"]"



echo "LCD prepare $fn and sending it to $ip"

base=${fn%%.*}
output="small"$base

echo "$base     $output" 


convert $fn -resize 128x64^ -gravity Center -extent 128x64 $output".jpg"

convert $output".jpg" -type bilevel -depth 1 -negate $output".pbm"

convert $output".pbm" $output".pnm"

# This does not work !
convert $output".pbm" $output".mono"

python3 pnm2bin.py $output".pnm"

#cat "small"$base".mono" | nc -u 192.168.2.228 21567 -w 0
#sleep 10

cat $output".bin" | nc -u $ip 21567 -w 0


