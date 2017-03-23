import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
import numpy as np
import random as rn
from sklearn.datasets.samples_generator import make_blobs

X,Y = make_blobs(n_samples = 500, centers=2, n_features=2, cluster_std=2)
xx = []
yy = []
for i,j in X:
    xx.append(i)
    yy.append(j)
    
data = pd.DataFrame({'x': xx, 'y': yy, 'class': Y})


#data = pd.DataFrame({'x': [1,2,3,4,5,6,7,8,9,10], 'y': [2,7,3,8,6,2,4,3,6,8], 'class': [1,1,1,1,1,2,2,2,2,2]})

xp = rn.randint(1,10)
yp = rn.randint(1,10)

def euclid(xp,yp,data_u):
    ll = []
    for index, row in data_u.iterrows():
        euc = sqrt((row['x'] - xp)**2 + (row['y'] - yp)**2)
        ll.append(euc)
    return ll    
    
def smallest_k(euclid, k):
    euclid = np.array(euclid)
    sorted_euclid = np.argsort(euclid)
    smallest_id = sorted_euclid[:k]
    return smallest_id

def decision(data, smallest_k):
    c1 = []
    c2 = []
    for index,row in data.iterrows():
        for n in smallest_k:
            if index == n:
                if row['class'] == 0:
                    c1.append(1)
                else:
                    c2.append(1)
    if len(c1) > len(c2):
        label = 0
    else:
        label = 1

    return label

def KNN(xp,yp,data=data,k=3): 
    euc = euclid(xp,yp,data)
    sm_k = smallest_k(euc,k)
    label = decision(data, sm_k)
    data.loc[len(data)] = [label,xp,yp]


KNN(xp,yp,k=9)

#data.to_csv('low_csv.csv')

x = data['x']
y = data['y']
label = data['class']

plt.scatter(x,y, c=label)
plt.text(xp,yp,[xp,yp])
plt.show()
