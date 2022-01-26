Hi Everybody,

The goal of this assignment is to replicate exactly the provided template.

Week3_Assignment_template.png 

(You can find the source file under Files/Resources/Assignments/Assignment_Week3)

To generate the figure, you have to parse the data in the BME163_Input_Data_2.txt text file provided in Files/Assignment_data

It is a tab separated text files with the log2(fold_change) in column 2 and p-values (which you still have to -log10 convert) in column 3.

Color points red if their fold-change (not log2(fold-change)) is larger than 10 (up or down) and their -log10(p-value) is above 8.

Label points with their gene names if their fold-change (not log2(fold-change)) is larger than 10 (only down) and their -log10(p-value) is greater than 30.

Submit a .png file with 600dpi and your code to generate the png file as a single python3 script (.py). You will be graded primarily on the image you submit.

File Name Format:

Code: LastName_FirstName_BME163_Assignment_Week3.py (should take input with "-i" and output figure to "-o")

Figure: LastName_FirstName_BME163_Assignment_Week3.png

Example command: python3 LastName_FirstName_BME163_Assignment_Week3.py -i BME163_Input_Data_2.txt -o LastName_FirstName_BME163_Assignment_Week3.png -s BME163

Use argparse and "-i" for input, "-o" for output, and "-s" for stylesheet.

For full points, I shouldn't be able to tell apart your image from mine. TAs will also attempt to run your code and possibly give you feedback on it. Unless your code doesn't run or could be significantly cleaned up or improved, it will not lose you points.

Remember to either use 'BME163' or 'BME163.mplstyle' as your style sheet. Do not use an absolute path.

Figure size: 3'' wide and 3'' high.

Main Panels: 2'' wide and 2'' high.

 

Happy plotting!

SCORE: 91/100

-5: Panel placement incorrect 

-2: Small non-systematic markersize difference 

-2: Incorrect point label placement"
