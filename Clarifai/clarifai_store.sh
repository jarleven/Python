#!/bin/bash

while IFS= read -r line; do
	test=`echo $line | head -n1 | awk '{print $1;}'`

	echo $test
	cp -f $test /home/tredea/clarifaifound/
done < helloworld.txt
