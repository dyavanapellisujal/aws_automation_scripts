#!/bin/bash

files=$( ls ./ )

for file in $files;
do
	echo $file
	if [ -f $file  ];then
		chmod +x $file
	fi
	
done
#or use

#chmod +x $1

