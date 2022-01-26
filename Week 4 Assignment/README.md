Hi Everybody,

The goal of this assignment is to replicate the provided template - in this case, it doesn't have to be exact, you just have to capture the distribution of the data with your swarm plot. I do however expect the figures, panel, and labels to be the right size and in the right position.

Week4_Assignment_template_black.png

(You can find the source file under Files/Assignments)

To generate the figure, you have to parse the data in the text file provided in Files/Resources/Assignment_data (It's file number 3).

It is a tab separated text files read names in the first column and identity (%) in the second column.

Subread coverage can be found in the first column, which is the read name. See the red number in the first name in the file.

0f3e2e30-cb87-44be-8113-dffcd743de7b_12.45_1885_3_565_191|Nextera_A-A8-TSO6|ISPCR_S_E

You have to collect identity (%) for separately for reads with a specific subread coverage (see categories in the figure template: 1,2,3,...,10,>11)

Then you have to plot these identities as a swarm plot for each subread coverage.

 

You are not allowed to use a premade swarm plot function. You have to write a swarm plot function yourself, which has to place the points while taking into account their distance in "paper space"! Also, don't plot all the points in the file, but subsample them to 1000 points for each swarm plot. Also, test your function with less points because plotting 1000 points will take a while.

 

File Name Format:

Code: LastName_FirstName_BME163_Assignment_Week4.py using (-i, -s, and -o)

Figure: LastName_FirstName_BME163_Assignment_Week4.png

Example command: python3 LastName_FirstName_BME163_Assignment_Week4.py -i BME163_Input_Data_3.txt -o LastName_FirstName_BME163_Assignment_Week4.png -s BME163

TAs will also attempt to run your code and possibly give you feedback on it. Unless your code doesn't run or could be significantly cleaned up or improved, it will not be lose you points.

Remember to either use 'BME163' as your style sheet. Do not use an absolute path.

Figure size: 7'' wide and 3'' high.

Panel size: 5'' wide and 2'' high.

 

Happy plotting!

 

Extra credit (Total of 115pt graduates, 130pt undergraduates)

Color the individual points according to their quality score as seen here

Week4_Assignment_template_color.png 

Quality score can be found here:

0f3e2e30-cb87-44be-8113-dffcd743de7b_12.45_1885_3_565_191|Nextera_A-A8-TSO6|ISPCR_S_E

 

Fallback template (70pts graduates and undergraduates)

If you can't figure out a reasonable Swarmplot function, you can use the boxplot function we wrote in class instead. The outcome should look like this. (Note that I omitted outliers)

Week4_Assignment_template_box.png

SCORE: 85.5/100

-5: Assymetrical 

-2: Small non-systematic markersize difference 

-5: incorrect jitter 

-2.5: Scaling Factor Incorrect
