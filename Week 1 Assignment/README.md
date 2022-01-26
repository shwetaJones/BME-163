Hi Everybody,

The goal of this assignment is to replicate exactly the provided template.

Week1_Assignment_template.png

Submit a .png file with 600dpi and your code to generate the png file as a single python3 script (.py). You will be graded primarily on the image you submit. For full points, I shouldn't be able to tell apart your image from mine. TAs will also attempt to run your code and possibly give you feedback on it. 

Unlike previous years, we will be requiring argparse for this assignment. The required arguments are --style_sheet (-s) and --output_file (-o). An example of argparse usage can be found in the class files (lecture code).

Your program will be run as such:

python3 LastName_FirstName_BME163_Assignment_Week1.py -s /path/to/stylesheet.mplstyle -o /path/to/output.png

 

Figure size: 3.42'' wide and 2'' high.

Panels: 1'' wide and 1'' high.

Hint1: You can use x or y coordinates directly in RGB tuples.

Hint2: numpy has cosine and sine functions that will be useful for the panel on the left.

Happy plotting!

SCORE: 93/100
-5: Incorrect spacing on points in panel 1 (using arange with a right bound of pi/2 doesn't have an endpoint of pi/2) 

-2: Point jitter in panel 1 from inaccurate pi value
