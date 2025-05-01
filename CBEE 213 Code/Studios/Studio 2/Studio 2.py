# SCRIPT IS BELOW
# I had some trouble getting jupyter to work so I just used VS
# I went through piece by piece doing the things. 
# I have no doubt you'll find this script is more than sufficient
# Answer to bonus, I would group by island, then groupby within the 
# island group and print the resulting species for each island

# PLEASE NOTE PRIOR TO ATTEMPTING TO RUN
# I use an os import for my filepathing
# you will need to figure that out on your own

# Here I import the libraries I used
import os
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# Here I get the file path
script_directory = os.path.dirname(__file__)
penguin_data = os.path.join(script_directory, 'penguins_size.csv')

# This just tries to read the CSV and tells me if it breaks 
def csv_reader(filepath):
    
    try:
        data = pd.read_csv(filepath) 
        print(f'CSV file found, successfully loaded.')
        return data 
    
    except Exception as e:
        print(f'Error reading CSV: {e}')
        return None


# This is a little more complex so I will annotate throughout
def penguin_sorting_function(data):
    
    
    # Here I create three unique data sets for each of the three sorting interests
    species_info = data.groupby('species')
    island_info = data.groupby('island')
    sex_info = data.groupby('sex')
    
    # This just gives basics about how many species and their names
    print(f'\nThere are {len(species_info)} species.')
    print('\nThis includes the following:')
    for species, group in species_info:
        print(f'Species: {species}')
    
    # This gives basics about how many islands and names
    print(f'\nAdditionally, there are {len(island_info)} islands.')
    print(f'\nThis includes the following:')
    for island, group in island_info:
        print(f'Island: "{island}"')
    
    # Here I add an option to choose which set you want to see
    # If a user is interested in species but not islands, they 
    # will see species and not islands
    print('\nHow would you like to see the sorted data?')
    print('1: By species \n2: By Island \n3: By sex')
    info_wanted = input('Input here: ')
    # Contingency for misinputs
    if not info_wanted.isdigit():
        print('\nYour input must be an integer.')
        info_wanted = input('Please retry here: ')
        if not info_wanted.isdigit():
            print('Please attempt to restart the script after googling "Integer Number".')
            return    
    info_wanted = int(info_wanted)
    
    # Determines which option was chosen
    if info_wanted == 1:
        sort_type = 'species'
        data_set = species_info
    elif info_wanted == 2:
        sort_type = 'island'
        data_set = island_info
    elif info_wanted == 3:
        sort_type = 'sex'
        data_set = sex_info
    
    # Create a dictionary to store data about the chosen set
    set_info = {}
    
    # This just runs through however many groups are in the set,
    # and grabs the noteworthy information about each one
    # It stores these as a nested dictionary
    for group_name, group in data_set:
        
        group_data = group.select_dtypes(include=[np.number])
        set_mean = group.mean(numeric_only=True)
        set_median = group.median(numeric_only=True)
        set_deviation = group.std(numeric_only=True)
        set_max = group.max(numeric_only=True)
        set_min = group.min(numeric_only=True)
        raw_values = group_data.to_dict(orient='list')
        
        set_info[group_name] = {
            'mean': set_mean,
            'median': set_median,
            'std_dev': set_deviation,
            'max': set_max,
            'min': set_min,
            'raw_values': raw_values,
            }
        
    # This adds a check to see if you want to view the data that has been processed
    print('\nWould you like to see the noteworthy data?')
    y_n_check = input('Input "y" for yes and "n" for no: ')
    #y_n_check = 'n'
    
    # If the check is passed, it will print data of interest and list which group it belongs to
    if y_n_check == 'y':
        print(f'\nWithin the {sort_type} group of data, noteable values are as follows:')
        for group_name, stats in set_info.items():
            print(f'\nGroup: {group_name}') 
            print(f'\nMean: {np.round(stats["mean"], 2)}')   
            print(f"\nMedian:\n{np.round(stats['median'], 2)}")
            print(f"\nStandard Deviation:\n{np.round(stats['std_dev'], 2)}")
            print(f"\nMax:\n{np.round(stats['max'], 2)}")
            print(f"\nMin:\n{np.round(stats['min'], 2)}")   
            print('\n- - - - - - - - - - - - - - ') 
            print('- - - - - - - - - - - - - -  ')
    # Contingency for not visualizing/misinputs
    elif y_n_check == 'n':
        pass
    else:
        print('\nInvalid input; moving on.')
        pass
    
    # This is a mystery tool that helps later
    return set_info, sort_type


# This is the function responsible for the plotting
def data_visualizer(data, sort_type):
    
    # data_cleaned cleans data
    # it drops missing values
    data_cleaned = data.dropna(subset=['culmen_length_mm', 'culmen_depth_mm', 'species'])
    
    # Here the scatter plot is built, it additionally will model whichever
    # sorting set was chosen, not just species
    plt.figure(figsize=(10,6))
    sns.scatterplot(
        data=data_cleaned,
        x='culmen_length_mm',
        y='culmen_depth_mm',
        hue=sort_type,
        style=sort_type,
        s=100
    )
    plt.title(f'Culmen Length vs. Culmen Depth by {sort_type.capitalize()}')
    plt.xlabel('Culmen Length (mm)')
    plt.ylabel('Culmen Depth (mm)')
    plt.legend(title=sort_type.capitalize())
    plt.tight_layout()
    plt.show()
    
    # Same as the scatter plot, but a box plot this time
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=data_cleaned,
        x=sort_type,
        y='culmen_length_mm',
        palette='Set2'
    )
    plt.title(f'Culmen Length Distribution by {sort_type.capitalize()}')
    plt.xlabel(sort_type.capitalize())
    plt.ylabel('Culmen Length (mm)')
    plt.tight_layout()
    plt.show()
        
        
# This is where the script is actually run
# It has a check for the data being read, and checks
# Where the user can specify what they want to see
# Additionally it has a contingency if someone cannot
# figure out how to pick y or n
try:
    operate = csv_reader(penguin_data)
    
    # Check for operate being defined
    if operate is not None:
       
       # I love the try function
       # I will throw it everywhere
       # God bless
       try: 
            set_info, sort_type = penguin_sorting_function(operate)
            
            # This adds the option to skip graphing
            if set_info:
                print('Would you like to visualize?')
                check = input('Type "y" for yes and "n" for no: ')
               
                if check == 'y':
                    try:
                        data_visualizer(operate, sort_type)
                    except Exception as e:
                        print(f'Encountered error {e}')
                elif check == 'n':
                    pass
                else:
                    print('Invalid input, you will need to rerun the script.')
       
       except Exception as e:
           print(f'Sorting function failed, error: {e}')

except Exception as e:
    print(f'There was an error in running the program, likely with file path. \nError is: {e}')
                