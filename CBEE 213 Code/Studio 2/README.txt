- - - - - EXPLANATION OF FILE - - - - - 
The 'studio 2.py' file uses your os to determine where 
to get your csv filepath. That all just means that the 
penguin_data.csv file, and the studio 2.py file, need 
to be in the same folder in your computer. 

When running the script itself, the markups and annotations
should explain each component, if they are unclear, reach out
in the CBEE 213 server, someone can explain it. Furthermore, 
I have inbuilt contingencies for misinputs, and error reporting, 
the script should be able to minimally trouble shoot for you. 

- - - - - COMMON ISSUES - - - - - 
Since I already explained the filepath issue we will skip it

The other issue that may arise is from the libraries not being
installed within an environment your IDE can recognize. If this
is the case, you can either manually install them, or run the 
command 'pip install -r studio_2_requirements.txt' in your cmd 
window. 
If you get a message saying 'file not found'. Use the 'cd "PATH"' 
command in your terminal to navigate to the correct directory. 

Note that 'PATH' is not the input, it should be something like
"c:\Users\username\Documents\Python\Studio 2"
Your input may vary, just copy the file path out of your file explorer.
