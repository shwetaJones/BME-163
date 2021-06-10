import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse

# argparse information
parser = argparse.ArgumentParser(description='Week 5 Assignment Options:', usage='python3 LastName_FirstName_Assignment_Week5.py -i Splice_Sequences.fasta -p /path/to/bases/pngs -s bme163.mplstyle -o LastName_FirstName_Assignment_Week5.png')
parser.add_argument('-s', '--style_sheet', default="BME163")
parser.add_argument('-i', '--input_file', default="Splice_Sequences.fasta")
parser.add_argument('-o', '--output_file', default="Jones_Shweta_Assignment_Week5.png")
parser.add_argument('-p', '--pngs')
args = parser.parse_args()
plt.style.use(args.style_sheet)

# figure design
figureHeight = 3
figureWidth = 6
plt.figure(figsize=(figureWidth, figureHeight))

# left panel design
leftWidth = 2.4
leftHeight = 1
leftPanelWidth = leftWidth / figureWidth
leftPanelHeight = leftHeight / figureHeight
leftPanel = plt.axes([0.1,0.3,leftPanelWidth,leftPanelHeight])
leftPanel.set_xlim(0, 20)
leftPanel.set_ylim(0, 2.0)
leftPanel.set_xticklabels(np.arange(-10, 11, 5))
leftPanel.plot([10, 10], [0, 2], lw=1/2, color='black')
leftPanel.set_ylabel('Bits')
leftPanel.set_title('5\'SS')
leftPanel.set_xlabel('Distance to\nSplice Site')

# right panel design
rightWidth = 2.4
rightHeight = 1
rightPanelWidth = rightWidth / figureWidth
rightPanelHeight = rightHeight / figureHeight
rightPanel = plt.axes([0.55,0.3,rightPanelWidth,rightPanelHeight])
rightPanel.set_xlim(0, 20)
rightPanel.set_ylim(0, 2.0)
rightPanel.set_xticklabels(np.arange(-10, 11, 5))
rightPanel.axes.yaxis.set_visible(False)
rightPanel.plot([10, 10], [0, 2], lw=1/2, color='black')
rightPanel.set_title('3\'SS')
rightPanel.set_xlabel('Distance to\nSplice Site')

# creation of up and down stream lists
upList = []
downList = []
for i in range(0, 20):
    upList.append({'A': 0, 'T': 0, 'C': 0, 'G': 0})
    downList.append({'A': 0, 'T': 0, 'C': 0, 'G': 0})

up = False
upstream = 0
downstream = 0
openFile = open(args.input_file, "r")
for line in openFile.readlines():
    if line[0] == ">":
        if line[1] == "3":
            up = False
            downstream += 1
        else:
            up = True
            upstream += 1
    else:
        for i in range(0, 20):
            if up == True:
                uplistPos = upList[i]
                uplistPos[line[i]] += 1
            else:
                downlistPos = downList[i]
                downlistPos[line[i]] += 1

# Creates a list of heights based on the upstream values
upHeights = []
for dict in upList:
    frequency = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for key in dict:
        frequency[key] = (dict[key] / upstream)
    total = 0
    for freq in frequency:
        total += frequency[freq] * np.log2(frequency[freq])
    height = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for freq in frequency:
        height[freq] = (frequency[freq] * (2 - ((-total) + ((4 - 1) / (np.log(2) * (2*upstream))))))
    upHeights.append(height)

# Creates a list of heights based on the downstream values
downHeights = []
for dict in downList:
    frequency = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for key in dict:
        frequency[key] = (dict[key] / downstream)
    total = 0
    for freq in frequency:
        total += frequency[freq] * np.log2(frequency[freq])
    height = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for freq in frequency:
        height[freq] = (frequency[freq] * (2 - ((-total) + ((4 - 1) / (np.log(2) * (2 * downstream))))))
    downHeights.append(height)

def logo_print (extent1, extent2, extent3, extent4, panel):
    A = mpimg.imread(args.pngs + "/A_small.png")
    G = mpimg.imread(args.pngs + "/G_small.png")
    C = mpimg.imread(args.pngs + "/C_small.png")
    T = mpimg.imread(args.pngs + "/T_small.png")
    if key == 'A':
        panel.imshow(A, aspect='auto', extent=[extent1, extent2, extent3, extent4])
    elif key == 'G':
        panel.imshow(G, aspect='auto', extent=[extent1, extent2, extent3, extent4])
    elif key == 'C':
        panel.imshow(C, aspect='auto', extent=[extent1, extent2, extent3, extent4])
    elif key == 'T':
        panel.imshow(T, aspect='auto', extent=[extent1, extent2, extent3, extent4])

for heightDict in range(0, 20):
    newupheights = upHeights[heightDict]
    upsortedHeights = sorted(newupheights.keys(), key=lambda k: newupheights[k])
    upTop = 0
    for key in upsortedHeights:
        upbottom = upTop
        upuptop = upbottom + newupheights[key]
        upTop = upuptop
        logo_print(heightDict, heightDict + 1, upbottom, upuptop, leftPanel)

    newdowheights = downHeights[heightDict]
    downsortedHeights = sorted(newdowheights.keys(), key=lambda k: newdowheights[k])
    doupTop = 0
    for key in downsortedHeights:
        downbottom = doupTop
        downtop = downbottom + newdowheights[key]
        doupTop = downtop
        logo_print(heightDict, heightDict+1, downbottom, downtop, rightPanel)

plt.savefig(args.output_file,dpi=600)