import xml.etree.ElementTree as ET 
import sys

def NumberofFrames(PersonFrames): #getting number of frames with people in it; aka important frames
    MaxFrames = 0
    for person in PersonFrames:
        for frameNo in person:
            if int(frameNo) >= MaxFrames:
                MaxFrames = int(frameNo)
    return MaxFrames

def NumberofPeopleinVS(PersonID): #number of people in video sequence
    return len(PersonID)

def NumberofPeopleinCurrentFrame(PersonFrames,PersonOcclusionStatus,currentFrame): #number of people in the current frame
    counter=0
    personNo=0
    for person in PersonFrames:
        if str(currentFrame) in person:
            counter +=1
        personNo+=1

    return counter 

def isInFrame(PersonID,PersonFrames,PersonOcclusionStatus,currentFrame, currentID): #check if person referred to by its ID (currentID) is in the current frame (currentFrame)
    currentID = PersonID.index(str(currentID))
    person = PersonFrames[currentID]    
    
    if str(currentFrame) in person:
        return True
    return False

def onePersonForAFrameOutput(PersonID,PersonFrames,PersonOcclusionStatus,currentFrame,currentID,PersonBoxes): #returns a annotation box variables referred to by currentFrame and currentID (person's ID)
    if isInFrame(PersonID,PersonFrames,PersonOcclusionStatus,currentFrame, currentID)==True:
        listID = PersonID.index(str(currentID))
        currentFrameID = PersonFrames[listID].index(str(currentFrame))
        xtl=PersonBoxes[listID][currentFrameID][0]
        ytl=PersonBoxes[listID][currentFrameID][1]
        xbr=PersonBoxes[listID][currentFrameID][2]
        ybr=PersonBoxes[listID][currentFrameID][3]
        return [xtl,ytl,xbr,ybr]

def CompleteOutput(metaframes,PersonID,PersonFrames,PersonOcclusionStatus,PersonBoxes): #return whole output in a list as ['string','string']
    output = []
    output.append(str(metaframes))
    output.append(str(NumberofPeopleinVS(PersonID)))
    noofframes = NumberofFrames(PersonFrames)
    perPersonoutput = []


    for i in range(0,noofframes):
        output.append(str(i))
        output.append(str(NumberofPeopleinCurrentFrame(PersonFrames,PersonOcclusionStatus,i)))
        for person in PersonID:
            if isInFrame(PersonID,PersonFrames,PersonOcclusionStatus,i,person)==True:
                output.append(str(person))
                perPersonoutput = onePersonForAFrameOutput(PersonID,PersonFrames,PersonOcclusionStatus,i,person,PersonBoxes)
                for data in perPersonoutput:
                    output.append(str(data))
    return output

xmlFile = str(sys.argv[1])  
tree = ET.parse(xmlFile)
root = tree.getroot()       #
meta = root.find("meta")    #xml getting root and positioning
task = meta.find("task")    #
metaframes = task.find("size").text

PersonID = [] #Contains all video sequence person IDs [Person1id,Person2id,...]
PersonFrames = [] #Contains all frames a certain person is in [[Person1 frames],[Person2 frames],...]
PersonBoxes = [] #Contains all boxes a certain person is in [[Person 1 boxes], [Person2 boxes],...] where [Person box] --> [[Box in a frame],[Box in a frame]] where [Box in a frame] --> [xtl,ytl,xbr,ybr] 
PersonOcclusionStatus = [] #ContainsOcclusion status, 0 if visible, 1 if occluded; not used

for track in root.findall('track'):
    PersonID.append(track.attrib['id'])
    Frames = [] 
    boxesByFrame = []                                                           # Gets values from .xml  
    box, Xtl, Ytl, Xbr, Ybr = ([] for i in range(5))                            # assigns them to lists declared in previous chunk
    occlusionstatus = []                                                        # all in order of personID appearance in .xml
    for box in track.findall('box'):
        Frames.append(box.attrib['frame'])
        occlusionstatus.append(box.attrib['occluded'])
        Xtl=(box.attrib['xtl'])
        Ytl=(box.attrib['ytl'])
        Xbr=(box.attrib['xbr'])
        Ybr=(box.attrib['ybr'])
        boxesByFrame.append([Xtl,Ytl,Xbr,Ybr])
    PersonFrames.append(Frames)
    PersonBoxes.append(boxesByFrame) 
    PersonOcclusionStatus.append(occlusionstatus)

#### formats output for .txt file ####
outputname = xmlFile[0:-4] 
outputname += '_formattedOutput.txt'
f = open(outputname,"w")
outputlist = CompleteOutput(metaframes, PersonID,PersonFrames,PersonOcclusionStatus,PersonBoxes)
outputString = ' '.join(outputlist)    
print 'XML parsed to',outputname
f.write(outputString)
