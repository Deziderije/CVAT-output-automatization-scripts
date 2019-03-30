#! /bin /bash

touch files.txt
ls | egrep '.*[mp4|avi]$' > files.txt
exec < files.txt
touch results.txt
while read filename; do
resolution="$(mediainfo --Inform="Video;%Width%" $filename)x$(mediainfo --Inform="Video;%Height%" $filename)"
FPS="$(mediainfo $filename | grep FPS | cut -f2 -d: | cut -f2 -d' ' | cut -f1 -d.)"
Frames="$(mediainfo --fullscan $filename | grep count -m 1 | cut -f2 -d: | cut -f2 -d' ')"
echo "$filename $resolution $FPS $Frames"
echo "$filename $resolution $FPS $Frames" >> results.txt
done
rm files.txt
