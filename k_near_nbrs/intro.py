import numpy as np
from sklearn import model_selection, preprocessing, neighbors
import pandas as pd

df = pd.read_csv('~/Documents/python/csv/breast-cancer-wisconsin.data.csv')
df.replace('?',-99999, inplace=True)
df.drop(['id'], 1, inplace=True)

x = np.array(df.drop('class',1))
y = np.array(df['class'])

x_train, ...
