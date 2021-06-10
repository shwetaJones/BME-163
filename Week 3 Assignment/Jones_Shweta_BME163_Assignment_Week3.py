#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import argparse

# Argparse code, from argparse_example.py code
parser = argparse.ArgumentParser(description='Week 3 Assignment Options:', usage='python3 LastName_FirstName_BME163_Assignment_Week1.py -s /path/to/stylesheet.mplstyle -o /path/to/output.png')
parser.add_argument('-s', '--style_sheet', default="BME163")
parser.add_argument('-i', '--input_file')
parser.add_argument('-o', '--output_file')
args = parser.parse_args()
plt.style.use(args.style_sheet)

xRed = []
yRed = []
xLabel = []
yLabel = []
xBlack = []
yBlack = []
geneList = []
openFile = open(args.input_file, "r")
for line in openFile.readlines():
    try:
        yCol = float(line.split()[2])
        y = -1*np.log10(yCol)
        x = float(line.split()[1])
        foldChange = 2**abs(x)
        if (foldChange > 10 and y > 30 and x < 0):
            xLabel.append(x)
            yLabel.append(y)
            geneList.append(line.split()[0])
        elif (foldChange > 10 and y > 8):
            xRed.append(x)
            yRed.append(y)
        else:
            xBlack.append(x)
            yBlack.append(y)
    except ValueError:
        continue

# Set dimensions of figure given requirements
figureHeight=3
figureWidth=3
plt.figure(figsize=(figureWidth, figureHeight))

# Set dimensions of panel given requirements
mainWidth = 2
mainHeight = 2
panelWidth = mainWidth / figureWidth
panelHeight = mainHeight / figureHeight
panel = plt.axes([0.1665,0.1665,panelWidth,panelHeight])
panel.set_xlim(-12.01,12.01)
panel.set_ylim(0,60)
panel.set_xlabel('log' + r'$_2$' + '(fold change)', fontsize=8)
# panel.set_ylabel('-log' + r'$_{10}$' + '(p-value)', fontsize=8)

# plt.xlabel(r'$log_{2}$'"(fold change)")
plt.ylabel('-' + r'$log_{10}$' + '(p-value)')
panel.tick_params(labelsize=8)
panel.plot(xLabel,yLabel,\
                  marker='o', \
                  linewidth=0,\
                  markeredgecolor='red',\
                  markerfacecolor='red',\
                  markeredgewidth=0, \
                  markersize=1.455)

panel.plot(xRed,yRed,\
                  marker='o', \
                  linewidth=0,\
                  markeredgecolor='red',\
                  markerfacecolor='red',\
                  markeredgewidth=0,\
                  markersize=1.455)

panel.plot(xBlack,yBlack,\
                  marker='o', \
                  linewidth=0,\
                  markeredgecolor='black',\
                  markerfacecolor='black',\
                  markeredgewidth=0, \
                  markersize=1.455)

for i in range(len(geneList)):
    panel.annotate(geneList[i],(xLabel[i], yLabel[i]), xytext=(xLabel[i] - 0.255, yLabel[i]),\
                      fontsize=6,verticalalignment='center',horizontalalignment='right')
plt.savefig(args.output_file,dpi=600)
