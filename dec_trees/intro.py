import scipy.stats
import numpy as np
import pandas as pd

data = pd.read_csv('baloon.csv')

mapping_col = {'YELLOW': 0, 'PURPLE': 1}
mapping_size = {'SMALL': 0, 'LARGE': 1}
mapping_age = {'ADULT': 0, 'CHILD': 1}
mapping_act = {'STRETCH': 0, 'DIP': 1}
mapping_infl = {'F': 0, 'T': 1}

columns = []
for i in data:
    columns.append(i)
print(columns)

data.replace({'color': mapping_col, 'size': mapping_size, 'act': mapping_act, 'age': mapping_age, 'inflated': mapping_infl}, inplace=True)

#root branch decision via entropy and information gain
def prob(data):
    
    z = scipy.stats.entropy(data['color'])
    return z
    
    
print(prob(data))
        
