Command:
    python xmlparser.py [--option] [file1.xml file2.xml ...]
    python xmlparser.py [--option] [*.xml...]  
Dependencies:
    xml (standard python library)
    trebalo bi raditi jednako na windowsima (os nije koristen)
------------------------------------------
OPTIONS:
    --video-export - 
                    Outputs format used by PeopleDrawer.
    --text-export -
                    Outputs standard text format.

------------------------------------------
Uglavnom pretvara CVAT-ov output xml u oblik koji je zadan, a to je
(broj frameova) (broj osoba u vs) | (broj tekuceg framea) (broj osoba u tekucem frameu) | (ID osobe) (Xtl) (Ytl) (Xbr) (Xbr)
...ispisuje se odijeljeno samo razmacima
------------------------------------------
EDIT by Niksa:

Descr:
    Script added that converts all .xml files in current directory to given .txt format and dumps them into Txt_Format folder

ToRun:
    bash Auto.sh
