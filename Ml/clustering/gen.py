#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:14:01 2019

@author: nikitha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dat= pd.read_csv('gen.csv')
dat= dat.iloc[:,:1]

#X=dat.convert_objects(convert_numeric=True)


for i in X.columns:
    print(X[i].isnull().sum())
    
for i in X.columns:
    X[i]=X[i].fillna(int(X[i].mean()))

print("after imptation")
for i in X.columns:
    print(X[i].isnull().sum())
    
