#! /bin /bash

touch xmls.txt
ls | grep .xml$ > xmls.txt
exec < xmls.txt

while read line; do
	python xmlparser.py --text-export $line
	python xmlparser.py --video-export $line
done
rm xmls.txt
mv *VideoFormat* ../Vid_Format
mv *TxtFormat* ../Txt_Format
