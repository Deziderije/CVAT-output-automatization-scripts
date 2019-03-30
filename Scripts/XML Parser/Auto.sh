#! /bin /bash

touch xmls.txt
ls | grep .xml$ > xmls.txt
exec < xmls.txt

while read line; do
	python xmlparser.py $line
done
mkdir Txt_Format
rm xmls.txt
mv *.txt Txt_Format
