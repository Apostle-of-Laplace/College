- - - - - READ ME - - - - - 
Before anything else, make sure all the files you downloaded from 
my GitHub page are in the same directory (folder). If they are not 
together the references in the script will not work. More detailed 
explanation will be below the common issues section. 

In the file, each component should be explained by the annotations
and markups. If they are unclear, reach out to someone in the CBEE 
server. The file also has minimal contingencies against misinputs.
This means that the script can do some troubleshooting for you, but
not a lot. You can ignore the 'try' and 'except' statements, they 
are just the script's way of troubleshooting and do not need to be
included in your script.


- - - - - COMMON ISSUES - - - - - 
If you are in Visual studio, you can open the CMD terminal
with 'ctrl + ~'. If you are in a different IDE, or cannot 
access the terminal, importing libraries will be up to you. 


- - - - - 'Filepath not found' - - - - -
If you receive an error report saying filepath not found,
you have likely input the file name incorrectly, or do not have
the files within the same directory. Check that all the files 
involved with the script are in the same parent directory.
If you receive this report while attempting to install something 
with the CMD terminal, see the pip install section below. 


- - - - - 'Module not found' - - - - -
This error report will generally happen when the library you are 
importing is not installed, or is in a different file. If this happens,
run the command 'pip install -r homework_1_requirements.txt' in 
your CMD terminal. 

The terminal may return a 'file not found' type report when you try to 
run install the requirements. If this happens, check to make sure your 
terminal is in the correct directory. You can do this by trying to match 
the filepath listed in the terminal with the filepath of your script's 
directory. 

Example file path; 
"C:\Users\username\OneDrive\Current Project\CBEE Homework" 

If your directories do not match, run the command 'cd (Filepath)' in your 
terminal. (Filepath) should be the path that leads to the directory your 
script is currently in. You can find this path in your File Explorer.
 After the cd command is run, your paths should match. 

You can then retry installing from the requirements file. 

- - - - - Other Issues - - - - -
If you run into a problem that cannot be solved with a quick google search. 
Consult the CBEE discord, or DM me and I can try to help you resolve it. 


- - - - - Detailed Explanation - - - - - 
This script completes the homework 1 assignment by dividing it into four 
main parts. 
Part 1: Importing the data
Part 2: Reading the Data
Part 3: Processing the coinflip data
Part 4: Processing the Mice data

Part 1: The script is built with the assumption that you will have your
.py file and the .csv files in the same directory. It then imports your 
operating system and uses that to find out where it is in the computer. 
After the script knows where it is, it joins the path to its parent 
directory with the other file, completing its file path. (Basically address)

Part 2: Here the script takes the filepaths found in part one, and inputs them
to the 'read_csv_file' function. This function just uses pandas to define a 'data'
variable as the contents of the csv, and then spits that variable out the other side.

Part 3: Here the script processes the data from the 'coinflip' csv. It works by first
getting only the second column of the data set, and then choosing ten random numbers 
between 0 and 489. These are the ten random rows. The script then finds information
about these rows, mean, median, etc, and prints them to the terminal. Again feel free 
to ignore the repetitions based if statements, and the try/except parts. That is simply 
to troubleshoot user error.

Part 4: Finally the script parses the sleep data, and notes import values. This section will
also be subdivided for simplicity.

Part 4a. Here the script sorts the sleep data into different groups based on the 'animal ID'. 
It then creates three different variable types to append data to. The variables with {} are 
dictionaries, they hold both a value and the 'Key' to that value. Ex ["AAL": 2, "AAR": 4, etc]
The [] variables are lists, and the variables defined as None only hold the one value.

Part 4b. Finding average amplitude. The first for loop parses through the data sets and gets 
relevant data. Specifically, it finds out how much time was measured, the standard deviation of
that mouse's amplitude, and then runs a check to see if the STDDEV possessed by the current mouse
is higher than the previous choices. The highest value will be appended to our highest_avg_amp_value
variable, as will the mouse it comes from. 

Part 4c. The script separatees the data into another set based on sleep state. The second for loop 
then iterates over these different states and finds the stddev of the avg frequency and does a check
similar to the last for loop, but this time to find the lowest value.

Part 4d. Here the script prints out results for each mouse. To avoid having like 20 print statements, 
for loops are used. 

Part 4e. This is where the script graphs data. I will not be explaining it. Good luck. 