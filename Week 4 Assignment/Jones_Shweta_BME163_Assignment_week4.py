import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse
import random

# Followed Prof. Asgn 4 Pseudocode
def swarmplot(yList, xCenter, pointSize, xrange, yrange, panelwidth, panelheight, ):
    placedPoints = []
    minDistance = pointSize / 72
    count = 0
    for yPos in yList:
        xPos = xCenter
        placedLength = len(placedPoints)
        if placedLength > 0:
            for point in placedPoints:
                xVal = (xPos-point[0])/xrange
                yVal = (yPos-point[1])/yrange
                xDist = (xVal*panelwidth)**2
                yDist = (yVal*panelheight)**2
                distance = np.sqrt(xDist + yDist)
                if distance <= minDistance:
                    if (count%2 == 0):
                        xPos += (minDistance * 2.5)
                    else:
                        xPos -= (minDistance * 2.5)
                count += 1
        placedPoints.append((xPos, yPos))
    return [i for i in placedPoints]

# Argparse code, from argparse_example.py code
parser = argparse.ArgumentParser(description='Week 3 Assignment Options:', usage='python3 LastName_FirstName_BME163_Assignment_Week1.py -s /path/to/stylesheet.mplstyle -o /path/to/output.png')
parser.add_argument('-s', '--style_sheet', default="BME163")
parser.add_argument('-i', '--input_file', default="BME163_Input_Data_3.txt")
parser.add_argument('-o', '--output_file', default="1out")
args = parser.parse_args()
plt.style.use(args.style_sheet)

# figure design
figureHeight = 3
figureWidth = 7
plt.figure(figsize=(figureWidth, figureHeight))

# main panel design
mainWidth = 5
mainHeight = 2
mainpanelWidth = mainWidth / figureWidth
mainpanelHeight = mainHeight / figureHeight
mainPanel = plt.axes([0.1,0.2,mainpanelWidth,mainpanelHeight])
# sets limits of x and y
mainPanel.set_xlim(0.25,11.75)
mainPanel.set_ylim(75,100)
# sets x ticks
mainPanel.set_xticks(np.arange(1,12))
ticks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '>10']
mainPanel.set_xticklabels(ticks)
# sets labels of the graph
mainPanel.set_ylabel('Identity %')
mainPanel.set_xlabel('Subread Coverage', fontsize = 8)
# set dash line in main panel
mainPanel.plot([0,12],[95,95], linewidth=0.5, linestyle=(0, (2, 2, 1, 2)), color='black', markersize=2)

# side panel
sideWidth = 0.2
sideHeight = 2
secondPanelHeight = sideHeight / figureHeight
secondPanelWidth = sideWidth / figureWidth
secondPanel = plt.axes([0.9, 0.2, secondPanelWidth, secondPanelHeight])
# side panel axis information
secondPanel.set_ylim(7,15)
secondPanel.axes.xaxis.set_visible(False)
secondPanel.set_ylabel('Read quality (Q)')
# side panel gradient
colorRange = np.linspace(0,0.9,16)
colors = [(1-i, 1-i, i) for i in colorRange]
for color in colors:
    patch = mplpatches.Rectangle((0, (colors.index(color)+7)/1.55), 1, 1, facecolor=color)
    secondPanel.add_patch(patch)

openFile = open(args.input_file, "r")
# openFile = open("BME163_Input_Data_3.txt", "r")
subreadDict = {}
medianDictInfo = {}
for i in range(1,12):
    subreadDict[i]=[]
for line in openFile.readlines():
    lineList = line.split()
    subRead = int(lineList[0].split("_")[3])
    identity = float(lineList[1])
    # For Swarm
    if subRead <= 10:
        subRead = subRead
    else:
        subRead = 11
    subreadDict[subRead].append(identity)
    # For Median
    quality = float(lineList[0].split("_")[1])
    try:
        medianDictInfo[subRead].append((identity, quality))
    except KeyError:
        medianDictInfo[subRead] = [(identity, quality)]

# Swarm Plot Display
for key,subread in subreadDict.items():
    point = swarmplot((random.sample(subread, 1000)),key, 0.9, 11.5, 25, 5, 2)
    for p in point:
        mainPanel.plot(p[0], p[1],
                    marker='o',
                    markerfacecolor='black',
                    markeredgecolor='black',
                    markersize=0.85,
                    markeredgewidth=0,
                    linewidth=0)

# Median Line Display
readDict = {}
qualityScoresDict = {}
for key in medianDictInfo:
    identity, quality = zip(*(np.array(medianDictInfo[key])[np.random.choice(len(medianDictInfo[key]),1000)]))
    readDict[key] = np.array(identity)
    qualityScoresDict[key] = np.array(quality)
medians = {key : np.median(readDict[key]) for key in readDict}
for key in medians:
    mainPanel.plot([int(key)-0.35,int(key)+0.35],[medians[key],medians[key]],lw=1, color='red',zorder=1)

# plt.savefig("1out",dpi=600)
plt.savefig(args.output_file,dpi=600)