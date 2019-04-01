Dependencies:
	Everything

Command:
	bash MasterChef.sh

---------------------------------------------------------------------------------------------------------

Outputs videos with hardcoded annotations. Requires XML file of annotations and MP4 file of the video.

A SPECIFIC DIRECTORY STRUCTURE IS REQUIRED, SUCH AS DESCRIBED BELOW. AUTOMATIC UNPACKER COMING SpOON.


[Parent Directory]
|
|--Txt_Format
|--MasterChef.sh
|--Dataset
	|--Slicer.sh
	|--[.mp4 files]
|
|--Vid_Format
	|--Painter.sh
	|--drawer.py
|
|--XMLS
      |--[.xml files]
      |--Editor.sh
      |--xmlparser.py
|
|--Output
	|--Fin
	|--Masher.sh

--------------------------------------------------------------------------------------------------------

Detailed Description:
	MasterChef coordinates the others (Painter, Slicer, Masher & Editor)
	Editor formats the XML files into Txt_Format (As requested by Franjo) and Vid_Format, suitable
	for generating .png files of frame-by-frame annotations, as done by Painter.
	Slicer slices videos into frame-by-frame .jpg files.
	Masher overlaps video frames and annotation frames, and then mashes them all into a final
	output - video with hardcoded person-tracking annotations
