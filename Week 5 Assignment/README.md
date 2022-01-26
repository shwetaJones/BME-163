Reproduce the following figure:

Week5 _Assignment_template.png 

Figure Dimensions: Width 6, Height 3
Panel (each): Width 2.4, Height 1


BME263
-Make a Function the returns the reverse complement of a sequence
-Read in genome sequence from fasta file (ftp://ftp.ensembl.org/pub/release-87/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz)
=>convert chromosome names (1->chr1, MT -> chrM)
-Read in Splice coordinates from bed file.
=>First column is chromosome (already right format), second column is position, first position of 4th column is the Type is splice junction
-Collect the sequence from 10bp before to 10bp after each splice junction
-Divide Splice Juntions in 5' and 3'. Reverse complement all 3' sequences
-For 5' (left panel) and 3' (right panel) splice juntions:
-For each position from 0 to 20 bp calculate the relative base frequency and Information content to determine Stack height and Base Height (Everything you need is on Wikipedia)
-Plot stack for each position. (Reminder, bases are sorted top -> bottom with the most frequent on top)

-Arguments: (-g, --genome), ('-b', '--bed'), ('-p', '--pngs'), ('-s', '--style_sheet'), ('-o', '--output_file')

 

python3 LastName_FirstName_Assignment_Week5.py -g mus_musculus.fasta -b Splice_Locations.bed -p /path/to/bases/pngs -s bme163.mplstyle -o LastName_FirstName_Assignment_Week5.png

 

BME163

-Read in sequences from fasta file
-Divide Splice Juntions in 5' and 3' (First position of read name)
-For 5' (left panel) and 3' right panel) splice juntions:
-For each position from 0 to 20 bp calculate the relative base frequency and Information content to determine Stack height and Base Height (Everything you need is on Wikipedia)
-Plot stack for each position. (Reminder, bases are sorted top -> bottom with the most frequent on top)

-Arguments: ('-i', '--input_file'), ('-p', '--pngs'), ('-s', '--style_sheet'), ('-o', '--output_file')

python3 LastName_FirstName_Assignment_Week5.py -i Splice_Sequences.fasta -p /path/to/bases/pngs -s bme163.mplstyle -o LastName_FirstName_Assignment_Week5.png

 

The path to bases pngs argument should be the directory where you put A_small.png etc.

Example directory tree:

assignment_5/
├── a5_163.py
├── a5_263.py
├── a5_template.png
├── bases/
│   ├── A_small.png
│   ├── C_small.png
│   ├── G_small.png
│   └── T_small.png
├── mus_musculus.fasta
├── Splice_Locations.bed
└── Splice_Sequences.fasta

If I had this directory tree, my command to run the program as a grad student would be:

python3 a5_263.py -g mus_musculus.fasta -b Splice_Locations.bed -p bases/ -s BME163 -o a5_template.png
As an undergrad:

python3 a5_163.py -i Splice_Sequences.fasta -p bases/ -s BME163 -o a5_template.png
 

Students in BME 163 can submit the BME 263 version of the assignment for 10 extra credit points. Students in BME 263 can submit the BME 163 version of the assignment for a maximum of 85 points

SCORE: 95/100

-5: Panel placement incorrect because we give out these answers in OH
