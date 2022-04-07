#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:20:54 2022

@author: mariela
"""

###This code compare the elements into two files

import numpy as np

f1 = np.loadtxt("ages.txt")
f2 = np.loadtxt("edades.log.txt", usecols=1)
  

for i in range(len(f1)):
    if f1[i]==f2[i]:
        print("{:.4E}".format(f1[i]))
    else:
            print(i,'',"{:.4E}".format(f1[i]),'is different from',"{:.4E}".format(f2[i]))
