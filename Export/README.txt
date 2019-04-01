Dependencies:
	Everything

Command:
	bash MasterChef.sh

-----------------------------------------------------------------------------------------------

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
