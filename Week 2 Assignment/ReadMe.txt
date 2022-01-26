Hi Everybody,

The goal of this assignment is to replicate exactly the provided template.

Week2_Assignment_template.png 

(You can find the source file under Files/Assignment_templates)

To generate the figure, you have to parse the data in the BME163_Input_Data_1.txt text file provided in Files/Assignment_data.

It is a tab separated text files with the x_values in column 2 and y_values in column 3.

Note that before plotting the values (using .plot or .scatter) convert them [ log2(values+1)].

Same goes for the height of the histogram bars [ log2(height+1)]

The entire right side of the figure is optional and will earn you 20 (BME163) or 10 (BME263) extra points.

For this optional right side plot a heatmap instead of individual points. You'll have to figure out the appropriate color map and how to divide you plot and bin your points.

Submit a .png file with 600dpi and your code to generate the png file as a single python3 script (.py). You will be graded primarily on the image you submit.

File Name Format:

Code: LastName_FirstName_BME163_Assignment_Week2.py

Figure: LastName_FirstName_BME163_Assignment_Week2.png

Example command: python3 LastName_FirstName_BME163_Assignment_Week2.py -i BME163_Input_Data_1.txt -o LastName_FirstName_BME163_Assignment_Week2.png -s BME163

Use argparse and "-i" for input, "-o" for output, and "-s" for stylesheet. 

 

For full points, I shouldn't be able to tell apart your image from mine. The TAs will also attempt to run your code and possibly give you feedback on it. Unless your code doesn't run or could be significantly cleaned up or improved, it will not lose you points.

Remember to either use 'BME163' or 'BME163.mplstyle' as your style sheet. Do not use an absolute path.

Figure size: 5'' wide and 2'' high.

Main Panels: 1'' wide and 1'' high.

Side Panels: 0.25'' wide and 1'' hight

Top Panels: 1'' wide and 0.25'' hight

 

Important: No outside libraries and packages. Only use plot/scatter and rectangles. NO numpy histogram2d. Have to calculate your own 2D histogram...

 

Happy plotting!

SCORE: 85/100

-10: hard-coded filename 

-5: Panel placement incorrect
