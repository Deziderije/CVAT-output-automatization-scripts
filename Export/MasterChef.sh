#! /bin /bash

cd XMLS
echo "Editor activated"
bash Editor.sh
echo "Files edited."
cd ../Dataset
echo "Slicer activated."
bash Slicer.sh
echo "Orders sliced."
cd ../Vid_Format
echo "Painter activated"
bash Painter.sh
echo "Masterpiece painted"
cd ../Output
echo "Masher activated"
bash Masher.sh
echo "All is done."

