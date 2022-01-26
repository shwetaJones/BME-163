Hi Everybody,

The goal of this assignment is to replicate the provided template exactly.

Week6_Assignment_template.png 

(You can find the source file under Files/Assignment_templates)

Figure Dimensions: Width 5, Height 3
Panel (each): Width 0.75(left) and 2.5 (right) , Height 2.5

 

To generate the figure, you have to parse the data in the text file provided in BME163_Input_Data_4.txt.

It is a tab separated text file. Each row contains expression value and other data on a single gene. The first row contains column labels. Data for the heatmap is in columns labeled FPKM_CT*. Read these values in and normalize like we did in class:

normalized_y_data=((random_list-min(random_list))/(max(random_list)-min(random_list)))*100

The normalized list can then be used for the heatmap. Make sure to sort the lists based on the Peak_phase(CT) column and use only the rectangle function.

Only BME263 has to do the right panel (10 points extra credit for BME163):

For the right panel, make a circular histogram of the Peak_phase(CT) column using 2 hour long bins (0-2,2-4,4-6, etc...).

USE ONLY .plot() and .text() functions. Use of any other function will lead to your submission not being graded.

 

File Name Format:

Code: LastName_FirstName_BME163_Assignment_Week6.py using (-i, -s, and -o)

Figure: LastName_FirstName_BME163_Assignment_Week6.png

Example command: python3 LastName_FirstName_BME163_Assignment_Week6.py -i BME163_Input_Data_4.txt -o LastName_FirstName_BME163_Assignment_Week6.png -s BME163

 

Happy plotting!

SCORE: 100/100

Nice!
