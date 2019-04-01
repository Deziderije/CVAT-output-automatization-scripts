#! /bin /bash

ls | grep txt | cut -f1 -d'>' > temp.txt
while read line; do
	echo "Converting $line annotations to .PNG"
	python drawer.py "$line>VideoFormat.txt"
	mv PeopleDrawerOutput/* ../Output/$line
	echo "Conversion over"
done < temp.txt
rm temp.txt
