from PIL import Image, ImageDraw
import sys
import os

colors = [(255, 0, 0),(255, 51, 204),(102, 0, 255),(51, 204, 255),(255, 153, 0),(179, 0, 179),(153, 204, 0),(102, 255, 204),(204, 102, 255),(204, 51, 153),(102, 255, 102),(51, 204, 51),(0, 255, 255),(230, 230, 0),(0, 119, 179),(255, 26, 255),(0, 51, 153),(117, 117, 163),(0, 136, 204),(153, 102, 51)]
linewidth = 3
def createEmptyFrames(TotalFrame,CurrentFrame,output):
    howMany = int(TotalFrame) - int(CurrentFrame)
    for i in range(howMany+1):
        savename = ''
        im = Image.new('RGBA', (1920, 1080), (255,255,255,0))
        draw = ImageDraw.Draw(im)
        savename = output + str(int(CurrentFrame)+i) + '.png'
        im.save(savename,'PNG')
        im.close()

def drawRectangle(Xtl,Ytl,Xbr,Ybr,color):
    draw.line((Xtl,Ytl, Xtl, Ybr), fill=color, width=linewidth)
    draw.line((Xtl,Ytl, Xbr, Ytl), fill=color, width=linewidth)
    draw.line((Xbr,Ytl, Xbr, Ybr), fill=color, width=linewidth)
    draw.line((Xtl,Ybr, Xbr, Ybr), fill=color, width=linewidth)

os.system('rm -rf PeopleDrawerOutput')
os.system('mkdir PeopleDrawerOutput')
curdir = str(os.getcwd())
outputdir = curdir + '/PeopleDrawerOutput/'

with open(str(sys.argv[1])) as infofile:
    content = infofile.readlines()
    totalFrames = int(content[0].split()[0])
    status = 0
    for line in content:
        lineInList = line.split()
        if 'frameid' in lineInList:
            print lineInList
            if status == 1:
                output = outputdir + str(int(frameNo)+1) + '.png'
                im.save(output,'PNG')
                del draw
                im.close()
                status = 0
            if status == 0:
                frameNo = lineInList[1] 
                status = 1
                im = Image.new('RGBA', (1920, 1080), (255,255,255,0))
                draw = ImageDraw.Draw(im)
            
        elif status==1:
            colorID = int(lineInList[1])-1   #-1 jer je lista boja od 0 a osobe od 1
            if colorID >= 20:
                colorID = colorID % 20
            xtl = float(lineInList[3])
            ytl = float(lineInList[4])
            xbr = float(lineInList[5])
            ybr = float(lineInList[6])
            drawRectangle(xtl,ytl,xbr,ybr,colors[colorID])


output = outputdir + str(frameNo) + '.png'
im.save(output,'PNG')
del draw
im.close()
print 'Creating additional frames'
createEmptyFrames(totalFrames,frameNo,outputdir)
print 'Completed'
