#! /bin /bash

touch temp.txt
ls | grep mp4 | cut -f1 -d. > temp.txt
while read line; do
	echo "Slicing $line.mp4 to frames."
	mkdir $line
	mv $line.mp4 $line
	cd $line
	ffmpeg -loglevel quiet -nostdin -i $line.mp4 %d.jpg
	mv $line.mp4 ..
	cd ..
	mv $line ../Output
	echo "$line sliced."
done < temp.txt
rm temp.txt
