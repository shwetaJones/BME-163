#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

# Argparse code, from argparse_example.py code
parser = argparse.ArgumentParser(description='Week 1 Assignment Options:', usage='python3 LastName_FirstName_BME163_Assignment_Week1.py -s /path/to/stylesheet.mplstyle -o /path/to/output.png')
parser.add_argument('-s', '--style_sheet', default="BME163")
parser.add_argument('-i', '--input_file', default="BME163_Input_Data_1.txt")
parser.add_argument('-o', '--output_file')
args = parser.parse_args()
plt.style.use(args.style_sheet)

# Reads the input file to make get values for the histogram:
xList = []
yList = []
openFile = open(args.input_file,'r')
for line in openFile:
        x = int(line.split()[1])
        y = int(line.split()[2])
        xList.append(x)
        yList.append(y)
xVals = np.log2([i+1 for i in np.array(xList)])
yVals = np.log2([j+1 for j in np.array(yList)])

# Sets the figure size, from Lecture 2
figureHeight = 2
figureWidth = 5
plt.figure(figsize=(figureWidth, figureHeight))

# Sets the main panel size and axis's
mpanelWidth = 1
mpanelHeight = 1
mrelativePanelWidth = mpanelWidth/figureWidth
mrelativePanelHeight = mpanelHeight/figureHeight
mainPanel = plt.axes([0.165, 0.2, mrelativePanelWidth, mrelativePanelHeight])
mainPanel.axes.yaxis.set_visible(False)
mainPanel.set_xlim(0,15)
mainPanel.set_ylim(0,15)

# Constructs the scatter plot within the main panel
mainPanel.scatter(xVals,yVals,\
                  marker='o',\
                  linewidth=0,\
                  s=2,\
                  c='black',\
                  alpha=0.1)

# Sets the side panel
spanelWidth = 0.25
spanelHeight = 1
srelativePanelWidth = spanelWidth/figureWidth
srelativePanelHeight = spanelHeight/figureHeight
sidePanel = plt.axes([0.1, 0.2, srelativePanelWidth, srelativePanelHeight])
sidePanel.set_xlim(20,0)
sidePanel.set_ylim(0,15)

# Sets the top panel
tpanelWidth = 1
tpanelHeight = 0.25
trelativePanelWidth = tpanelWidth/figureWidth
trelativePanelHeight = tpanelHeight/figureHeight
topPanel = plt.axes([0.165, 0.735, trelativePanelWidth, trelativePanelHeight])
topPanel.axes.xaxis.set_visible(False)
topPanel.set_xlim(0,15)
topPanel.set_ylim(0,20)

# Constructs the histogram within the top and side panel
xHisto, xBins = np.histogram(xVals, np.arange(0, 15, 0.5))
yHisto, yBins = np.histogram(yVals, np.arange(0, 15, 0.5))
for i in range (0, len(yHisto), 1):
    # Side Panel Histogram
    sBottom = 0
    sLeft = np.arange(0, 15, 0.5)[i]
    sWidth = np.arange(0, 15, 0.5)[i + 1] - sLeft
    sHeight = np.log2(yHisto[i] + 1)
    sideRectangle = mplpatches.Rectangle([sBottom, sLeft],sHeight, sWidth,
                                     facecolor = 'grey',
                                     edgecolor = 'black',
                                     linewidth = 0.1)
    sidePanel.add_patch(sideRectangle)

    # Top Panel Histogram
    tBottom = 0
    tLeft = np.arange(0, 15, 0.5)[i]
    tWidth = np.arange(0, 15, 0.5)[i + 1] - tLeft
    tHeight = np.log2(xHisto[i] + 1)
    topRectangle = mplpatches.Rectangle([tLeft, tBottom], tWidth, tHeight,
                                         facecolor='grey',
                                         edgecolor='black',
                                         linewidth=0.1)
    topPanel.add_patch(topRectangle)

plt.savefig(args.output_file, dpi=600)
