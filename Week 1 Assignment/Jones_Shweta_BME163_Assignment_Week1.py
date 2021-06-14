import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

# Argparse code, from argparse_example.py
parser = argparse.ArgumentParser(description='Week 1 Assignment Options:', usage='python3 LastName_FirstName_BME163_Assignment_Week1.py -s /path/to/stylesheet.mplstyle -o /path/to/output.png')
parser.add_argument('-s', '--style_sheet', default="BME163")
parser.add_argument('-o', '--output_file')
args = parser.parse_args()
plt.style.use(args.style_sheet)

# Sets the figure size, from Lecture 2
figureHeight = 2
figureWidth = 3.42
plt.figure(figsize=(figureWidth, figureHeight))

# Sets the panel size, from Lecture 2
panelWidth = 1
panelHeight = 1
relativePanelWidth = panelWidth/figureWidth
relativePanelHeight = panelHeight/figureHeight

# Sets the location of the panels onto the figure, from Lecture 2
panel1 = plt.axes([0.1, 0.2, relativePanelWidth, relativePanelHeight])
panel2 = plt.axes([0.55, 0.2, relativePanelWidth, relativePanelHeight])

# Removes the axes of the panels
panel1.axes.xaxis.set_visible(False)
panel1.axes.yaxis.set_visible(False)
panel2.axes.xaxis.set_visible(False)
panel2.axes.yaxis.set_visible(False)

# generates panel 1, lecture 3
for i in np.arange(0, 1.57,0.06):
    panel1.plot(np.cos(i),np.sin(i),\
                marker='o', \
                markerfacecolor=(np.cos(i), np.cos(i), np.cos(i)), \
                markeredgecolor = 'black', \
                markersize=2, \
                markeredgewidth=0,\
                linewidth=0)

# generates panel 2, lecture 3
for i in np.arange(0,1,0.1):
    for j in np.arange(0,1,0.1):
            rectangle = mplpatches.Rectangle((i,j),0.1,0.1,\
                                    facecolor=(i,j,1),\
                                    edgecolor='black',\
                                    linewidth=1)
            panel2.add_patch(rectangle)
            
plt.savefig(args.output_file, dpi=600)
