import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

# ArgParse Implementation:
parser = argparse.ArgumentParser()

# ArgParse Options:
parser.add_argument('-i1', '--input_file1', default='BME163_Input_Data_5.psl')
parser.add_argument('-i2', '--input_file2', default='BME163_Input_Data_6.psl')
parser.add_argument('-g', '--gtf_file', default='gencode.vM12.annotation.gtf')
parser.add_argument('-o', '--output_file', default='Jones_Shweta_BME163_Assignment_Final.png')
args = parser.parse_args()

# Setting files
input3 = args.input_file1
input2 = args.input_file2
gtfFile = args.gtf_file
outputFile = args.output_file

# Figure dimensions
figureHeight = 5
figureWidth = 10
plt.figure(figsize=(figureWidth, figureHeight))

# Panel dimensions
panelWidth = 10
panelHeight = 1.25
relativePanelWidth = panelWidth/figureWidth
relativePanelHeight = panelHeight/figureHeight
bottomPanel = plt.axes([0, 0.05, relativePanelWidth, relativePanelHeight])
midPanel = plt.axes([0, 0.35, relativePanelWidth, relativePanelHeight])
topPanel = plt.axes([0, 0.65, relativePanelWidth, relativePanelHeight])

# removing ticks on panels
def panelEdit(panelType):
    panelType.tick_params(bottom=False, labelbottom=False,
                      left=False, labelleft=False,
                      right=False, labelright=False,
                      top=False, labeltop=False)
    panelType.axes.get_yaxis().set_ticks([])
    panelType.axes.get_xaxis().set_ticks([])
    panelType.set_xlim(45232945, 45240000)

panelEdit(topPanel)
panelEdit(bottomPanel)
panelEdit(midPanel)

# Sorting/Processing of psl file
# Referenced code given by Prof. Vollmers during section
def sortInput(inputFile):
    inputList = []
    openFile = open(inputFile, 'r')
    for line in openFile:
        a = line.strip().split('\t')
        read = [a[13], int(a[15]), int(a[16]), np.array(a[20].split(',')[:-1], dtype=int), np.array(a[18].split(',')[:-1], dtype=int), False]
        inputList.append(read)
    return (sorted(inputList, key=lambda x: x[2]))

# Sorts the input values and transforms the values within the input
readList3 = sortInput(input3)
readList2 = sortInput(input2)

# Middle Panel Display
# Referenced code provided by Prof. Vollmers
filteredReadList = []
for read in readList2:
    if read[0] == 'chr7':
        if 45232945 < read[1] < 45240000 or 45232945 < read[2] < 45240000:
            filteredReadList.append(read)

for val in range(1, len(filteredReadList)):
    lastest = 0
    for read in filteredReadList:
        if read[5] is False:
            final3 = val
            if read[1] > lastest:
                rectangle = mplpatches.Rectangle([read[1], val+0.18], read[2]-read[1], 0.1,
                                                 facecolor='black',
                                                 edgecolor='black',
                                                 linewidth=0)
                midPanel.add_patch(rectangle)
                for index in np.arange(0, len(read[3])):
                    blockstart = read[3][index]
                    blockwidth = read[4][index]
                    rectangle = mplpatches.Rectangle([blockstart, val], blockwidth, 0.5,
                                                     facecolor='black',
                                                     edgecolor='black',
                                                     linewidth=0)
                    midPanel.add_patch(rectangle)
                lastest = read[2]
                read[5] = True
final3 = final3 + (0.10*final3)
midPanel.set_ylim(0, final3)

#Bottom Panel Display
# Referenced code provided by Prof. Vollmers
filteredReadList = []
for read in readList3:
    if read[0] == 'chr7':
        if 45232945 < read[1] < 45240000 or 45232945 < read[2] < 45240000:
            filteredReadList.append(read)

for val in range(1, len(filteredReadList)):
    lastest = 0
    for read in filteredReadList:
        if read[5] is False:
            final3 = val
            if read[1] > lastest:
                rectangle = mplpatches.Rectangle([read[1], val+0.18], read[2]-read[1], 0.1,
                                                 facecolor='black',
                                                 edgecolor='black',
                                                 linewidth=0)
                bottomPanel.add_patch(rectangle)
                for index in np.arange(0, len(read[3])):
                    blockstart = read[3][index]
                    blockwidth = read[4][index]
                    rectangle = mplpatches.Rectangle([blockstart, val], blockwidth, 0.5,
                                                     facecolor='black',
                                                     edgecolor='black',
                                                     linewidth=0)
                    bottomPanel.add_patch(rectangle)
                lastest = read[2]
                read[5] = True
final3 = final3 + (0.10*final3)
bottomPanel.set_ylim(0, final3)

# Sorting/Processing of gtf file
# Referenced to code provided by Prof. Vollmers
transcriptList = []
gtfdict = {}
for line in open(gtfFile):
    if line[0] != '#':
        splitList = line.strip().split('\t')
        if splitList[2] == 'exon' or splitList[2] == 'CDS':
            transcript = splitList[8].split(' transcript_id "')[1].split('"')[0]
            if transcript not in gtfdict:
                gtfdict[transcript] = []
            gtfdict[transcript].append([splitList[0], int(splitList[3]), int(splitList[4]), splitList[2]])
for transcript, parts in gtfdict.items():
    starts = []
    ends = []
    blockstarts = []
    blockwidths = []
    types = []
    for part in parts:
        starts.append(part[1])
        ends.append(part[2])
        blockstarts.append(part[1])
        blockwidths.append(part[2] - part[1])
        types.append(part[3])
    transcriptList.append([part[0], min(starts), max(ends), blockstarts, blockwidths, False, types])
sorted_readList3 = sorted(transcriptList, key=lambda x: x[2])

# Top Panel display
# Referenced code provided by Prof. Vollmers
bottom = 1
filteredReadList = []
for read in sorted_readList3:
    if read[0] == 'chr7':
        if 45232945 < read[1] < 45240000 or 45232945 < read[2] < 45240000:
            filteredReadList.append(read)

for val in range(1, len(filteredReadList), 1):
    latest = 0
    for read in filteredReadList:
        if read[5] is False:
            finalY = val
            if read[1] > latest:
                rectangle = mplpatches.Rectangle([read[1], val+0.18], read[2]-read[1], 0.1,
                                                 facecolor='black',
                                                 edgecolor='black',
                                                 linewidth=0)
                topPanel.add_patch(rectangle)
                bottom += 1
                for index in np.arange(0, len(read[3]), 1):
                    if read[6][index] == 'exon':
                        rectangle = mplpatches.Rectangle([read[3][index], val+0.12], read[4][index], 0.25,
                                                         facecolor='black',
                                                         edgecolor='black',
                                                         linewidth=0)
                    else:
                        rectangle = mplpatches.Rectangle([read[3][index], val], read[4][index], 0.5,
                                                         facecolor='black',
                                                         edgecolor='black',
                                                         linewidth=0)
                    topPanel.add_patch(rectangle)
                latest = read[2]
                read[5] = True
topPanel.set_ylim(0, finalY+2.05)

plt.savefig(outputFile, dpi=1200)