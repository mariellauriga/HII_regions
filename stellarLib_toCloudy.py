#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:51:41 2022

@author: mariela
"""

import numpy as np
#import pandas as pd

import datetime
today = datetime.date.today()
    
#The file 'ages.txt' was created from the files 
#bc2019_z017_kroup_MU300_hr_xmilesi_ssp.all and 
#cb2019_z017_kroup_MU300_hr_xmilesi_ssp.all. Therefore it lists the same ages.
 
Age_val  = np.loadtxt('ages.txt')   

#####Alternative code if the age isnt listed like a column but a raw, and want to 
#####create a key for each age
#Using a dictionary to dynamically create the key names and associated values.    
#ages = {}
#k = 0
#while k < 221:
    ### dynamically create key
#    key = 'Age'+str(k+1)
    ### calculate value
#    value = Age_val[k]
#    ages[key] = value 
#    k += 1
    
#Create a dataframe for the age data
#df_age = pd.DataFrame(ages, index=[0])
#print(df_age.head())

#df_age = df_age.T
#print(df_age.head())
#print(df_age.iloc[220,0])

#Read the data
data = np.loadtxt('cb2019_z017_kroup_MU300_hr_xmilesi_ssp.all')
#print('lambda')
#print(data[-1,0]) # inspecting the data
#print(len(data))

#####IMPORTANT TO READ#####
#If the model is SSP (instantaneous star formation)
# it is necesary multiply the model by a factor fc=1E06. 
#With this correction the fluxes of the SSP models will be of the 
#same order of the SFR (continuous star formation)
#####################

#If the model is SSP
flux_ssp = []
flux_ssp = data[:,1:] # Lo/A -> It is normalized to solar luminosity
#############
#If the model is SFR
#flux_sfr = []
#flux_sfr = data[:,1:] # Lo/A -> It is normalized to solar luminosity
#############
Lsolar = 3.826E+33 #erg sec-1/Lo
#############
#print('flux')
#print(flux[-1,0]) # inspecting the data
fc = 1E6
flux = fc*flux_ssp  # If the model is SSP
#flux = flux_sfr    # If the model is SFR
#######################
flux = Lsolar*flux #erg sec-1 A-1

lambd = data[:,0] # in Angstroms
#print(data[-1,0]) 

#We requiere a wavelength > 107.3 A. Below it the flux is too small.


#Create the file that will be compiled in Cloudy. The two collumns are used 
#when the nebular emission is considere. Here we arent taking this emission 
#into account (we are simimulating star forming regions). However, these 
#columns are include to mimic the format from Starburst99 SEDs.


min_lambd = np.where(lambd==108.20)
print(min_lambd)
lmin = 114 #A, Para excluir los flujos nulos o negativos

#f = open('bc2019_z017_kroup_MU300_hr_xmilesi_ssp.stb99','w+')
f = open('cb2019_z017_kroup_MU300_hr_xmilesi_ssp.stb99','w+')

print(' MODEL DESIGNATION: GB1', file=f)
print(today.strftime(' MODEL GENERATED: %d %b %H:%M:%S %Y'), file=f)
print('                                            ', file=f)
print('              COMPUTED SYNTHETIC SPECTRUM', file=f)
print('                                            ', file=f)
print(' TIME [YR]    WAVELENGTH [A]   LOG TOTAL  LOG STELLAR  LOG NEBULAR  [ERG/SEC/A]',file=f)

for i in range(1,206): # range ages
   for j in range(lmin,len(lambd)): #range wavelengths
       if flux[j,i] > 0:
           print(' ',"{:.4E}".format(Age_val[i]), '      ',"{0:.2f}".format(lambd[j]), ' ',"{0:.4f}".format(np.log10(flux[j,i])), ' ',"{0:.4f}".format(np.log10(flux[j,i])), ' ','-15.00000', file=f)
         #print(' ',"{:.4E}".format(df_age.iloc[i,0]), '      ',"{0:.2f}".format(lambd[j]), ' ',"{0:.4f}".format(np.log10(flux[j,i])), ' ',"{0:.4f}".format(np.log10(flux[j,i])), ' ','-15.00000', file=f)
         
f.close()
