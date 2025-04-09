import os
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

script_directory = os.path.dirname(__file__)
penguin_data = os.path.join(script_directory, 'penguins_size.csv')

def csv_reader(filepath):
    
    try:
        data = pd.read_csv(filepath) 
        print(f'CSV file found, successfully loaded.')
        return data 
    
    except Exception as e:
        print(f'Error reading CSV: {e}')
        return None
    
def penguin_sorting_function(data):
    
    species_info = data.groupby('species')
    island_info = data.groupby('island')
    sex_info = data.groupby('sex')
    
    print(f'\nThere are {len(species_info)} species.')
    print('\nThis includes the following:')
    for species, group in species_info:
        print(f'Species: {species}')
    
    print(f'\nAdditionally, there are {len(island_info)} islands.')
    print(f'\nThis includes the following:')
    for island, group in island_info:
        print(f'Island: "{island}"')
    
    print('\nHow would you like to see the sorted data?')
    print('1: By species \n2: By Island \n3: By sex')
    info_wanted = input('Input here: ')
    if not info_wanted.isdigit():
        print('\nYour input must be an integer.')
        info_wanted = input('Please retry here: ')
        if not info_wanted.isdigit():
            print('Please attempt to restart the script after googling "Integer Number".')
            return    
    info_wanted = int(info_wanted)
    
    if info_wanted == 1:
        sort_type = 'species'
        data_set = species_info
    elif info_wanted == 2:
        sort_type = 'island'
        data_set = island_info
    elif info_wanted == 3:
        sort_type = 'sex'
        data_set = sex_info
    
    set_info = {}
    
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
        
    print('\nWould you like to see the noteworthy data?')
    y_n_check = input('Input "y" for yes and "n" for no: ')
    
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
    elif y_n_check == 'n':
        pass
    else:
        print('\nInvalid input; moving on.')
        pass
    
    return set_info, sort_type

def data_visualizer(data):
    
    data_cleaned = data.dropn(subset=['culmen_length_mm', 'culmen_depth_mm', 'species'])
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(
        data=data_cleaned,
        x='culmen_length_mm',
        y='culmen_depth_mm',
        hue='species',
        style='species',
        s=100
    )
    plt.title('Culmen Length vs. Culmen Depth by Species')
    plt.xlabel('Culmen Length (mm)')
    plt.ylabel('Culmen Depth (mm)')
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()
        
        

operate = csv_reader(penguin_data)
if operate is not None:
    set_info, sort_type = penguin_sorting_function(operate)
    if set_info:
        print('Would you like to visualize?')
        check = input('Type "y" for yes and "n" for no: ')
        if check == 'y':
            data_visualizer(set_info)
        elif check == 'n':
            pass
        else:
            print('Invalid input, you will need to rerun the script.')
                