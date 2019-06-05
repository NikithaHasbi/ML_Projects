#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:19:26 2019

@author: nikitha
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dat= pd.read_csv('gen.csv')
dat= dat.drop('CUST_ID',axis=1)

X=dat.convert_objects(convert_numeric=True)


for i in X.columns:
    print(X[i].isnull().sum())
    
for i in X.columns:
    X[i]=X[i].fillna(int(X[i].mean()))

print("after imptation")
for i in X.columns:
    print(X[i].isnull().sum())
    
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,31):
    kmeans= KMeans(n_clusters=i,max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,31),wcss)
plt.xlabel('clusters')
plt.ylabel('cost')
plt.show()


kmeans=  KMeans(n_clusters=5,max_iter=300,n_init=10,random_state=0)
kmeans.fit(X)

ypred= kmeans.fit_predict(X)

X['general']=ypred
X.to_csv('general.csv',sep=',')



