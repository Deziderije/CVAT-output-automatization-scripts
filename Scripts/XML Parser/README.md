# XML Parser

## Synopsis
### Command:
    python xmlparser.py [--option] [file1.xml file2.xml ...]
    python xmlparser.py [--option] [*.xml...]  
### Dependencies:
    1* xml (standard python library)
    _trebalo bi raditi jednako na windowsima (os nije koristen)_
### Options:
    `--video-export -` 
                    Outputs format used by PeopleDrawer.
    `--text-export -`
                    Outputs standard text format.

### Description
Uglavnom pretvara CVAT-ov output xml u oblik koji je zadan, a to je
(broj frameova) (broj osoba u vs) | (broj tekuceg framea) (broj osoba u tekucem frameu) | (ID osobe) (Xtl) (Ytl) (Xbr) (Xbr)
_Ispis je odijeljen samo razmacima, bez `(,|,)`_

## Auto.sh
### Description
Script added that converts all .xml files in current directory to given .txt format and dumps them into Txt_Format folder
_niksa_
### run with
`bash Auto.sh`
