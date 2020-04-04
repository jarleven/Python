#!/bin/bash

fn=""
ip=""

while [ $# -gt 0 ] ; do
  case $1 in
    --file) fn="$2" ;;
    --host) ip="$2" ;;
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


echo "LCD prepare $fn and sending it to $ip"

base=${fn%%.*}

echo $base



convert $fn -resize 128x64^ -gravity Center -extent 128x64 "small"$base".jpg"

convert "small"$base".jpg" -size 128x64 -type bilevel -depth 1 -negate "small"$base".pbm"

convert "small"$base".pbm" "small"$base".pnm"

# This does not work !
convert "small"$base".pbm" "small"$base".mono"

python pnm2bin.py "small"$base".pnm"

#cat "small"$base".mono" | nc -u 192.168.2.228 21567 -w 0
#sleep 10

cat "small"$base".bin" | nc -u $ip 21567 -w 0

