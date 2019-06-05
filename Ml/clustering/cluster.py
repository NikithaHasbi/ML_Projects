# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dat= pd.read_csv('cars.csv')
print(type(dat))
dat= dat.iloc[:,:-1]
#print(type(dat))

## convert objects to numeric variables ##
X=dat.convert_objects(convert_numeric=True)

#eliminate null values
for i in X.columns:
    print(X[i].isnull().sum())
    
for i in X.columns:
    X[i]=X[i].fillna(int(X[i].mean()))

print("after imptation")
for i in X.columns:
    print(X[i].isnull().sum())
    
from sklearn.cluster import KMeans


wcss=[]
for i in range(1,11):
    kmeans= KMeans(n_clusters=i,max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.xlabel('clsters')
plt.ylabel('cost')
plt.show()


kmeans=  KMeans(n_clusters=3,max_iter=300,n_init=10,random_state=0)
kmeans.fit(X)

ypred= kmeans.fit_predict(X)

X['cluster']=ypred
X.to_csv('cluster.csv',sep=',')



