Command
    python drawer.py [file.txt]
        - file.txt is output from XML parser with --video-export option.

Dependencies:
    PIL:
        PIL Image
        PIL ImageDraw
-------------------------------------------
Description:
    Creates .png images containing Annotation boxes for each frame in PeopleDrawerOutput directory.

    Notice:
            Previously existing folder name PeopleDrawerOutput is deleted.