#! /bin /bash

touch temp.txt
ls | grep UMN > temp.txt
while read line; do
	cd $line
	touch tmp.txt
	ls | grep png | cut -f1 -d. > tmp.txt
	echo "Mashing $line frames with annotation frames..."
	while read newline; do
		ffmpeg -i $newline.jpg -i $newline.png -nostdin -loglevel quiet -filter_complex "[1]scale=iw/1:-1[b];[0:v][b] overlay" "out_$newline.jpg"
	done < tmp.txt
	rm tmp.txt
	echo "Potatoes are mashed."
	echo "Making a video..."
	ffmpeg -framerate 25 -i out_%d.jpg -c:v libx264 -profile:v high -crf 20 -nostdin -loglevel quiet -pix_fmt yuv420p "$line-Annoted.mp4"
	echo "$line is served."
	mv *mp4 ../Fin
	cd ..
	rm -rf $line
	echo "Dinner is ready."
done < temp.txt
rm temp.txt
