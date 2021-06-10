import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

# argparse information
parser = argparse.ArgumentParser(description='Week 5 Assignment Options:', usage='python3 LastName_FirstName_Assignment_Week5.py -i Splice_Sequences.fasta -p /path/to/bases/pngs -s bme163.mplstyle -o LastName_FirstName_Assignment_Week5.png')
parser.add_argument('-s', '--style_sheet', default="BME163")
parser.add_argument('-i', '--input_file', default="BME163_Input_Data_4.txt")
parser.add_argument('-o', '--output_file', default="Jones_Shweta_BME163_Assignment_Week6.png") #"Jones_Shweta_Assignment_Week6.png")
args = parser.parse_args()
plt.style.use(args.style_sheet)

# figure design
figureHeight = 3
figureWidth = 5
plt.figure(figsize=(figureWidth, figureHeight))

# right panel design
rightWidth = 0.75
rightHeight = 2.5
rightPanelWidth = rightWidth / figureWidth
rightPanelHeight = rightHeight / figureHeight
rightPanel = plt.axes([0.1,0.1,rightPanelWidth,rightPanelHeight])
rightPanel.set_xlim(0, 16)
rightPanel.set_ylim(0, 1262)
rightPanel.set_xticks([1, 3, 5, 7, 9, 11, 13, 15])
rightPanel.set_xticklabels(['0', '', '6', '', '12', '','18', ''])
rightPanel.set_xlabel('CT')
rightPanel.set_ylabel('Number of genes')

# Reads in the file and places into a list
valList = []
openFile = open(args.input_file, "r")
next(openFile)
for line in openFile:
    splitLine = line.strip().split('\t')
    CT0 = int(splitLine[4])
    CT3 = int(splitLine[5])
    CT6 = int(splitLine[6])
    CT9 = int(splitLine[7])
    CT12 = int(splitLine[8])
    CT15 = int(splitLine[9])
    CT18 = int(splitLine[10])
    CT21 = int(splitLine[11])
    CT = float(splitLine[13])
    valList.append([CT, CT0, CT3, CT6, CT9, CT12, CT15, CT18, CT21])

# Sorts the list based on the first index, of CT value
valList.sort(reverse=True, key=lambda x: x[0])

# Places colored rectangles into figure based on value from list we created earlier
y = 0
for val in valList:
    processedData = (((np.array([val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8]]))-min(np.array([val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8]])))/(max(np.array([val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8]]))-min(np.array([val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8]])))) * 100
    x = 0
    for processed in processedData:
        rectangle = mplpatches.Rectangle([x, y], 3, 1, facecolor=(np.linspace(255/255, 56/255, 101)[int(processed)], np.linspace(225/255, 66/255, 101)[int(processed)], np.linspace(40/255, 157/255, 101)[int(processed)]),linewidth=0)
        rightPanel.add_patch(rectangle)
        x+=2
    y+=1

plt.savefig(args.output_file, dpi=600)