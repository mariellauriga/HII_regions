import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0001/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0001/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z0001, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0001/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z0001 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.0001})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0002/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0002/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z0002, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0002/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z0002 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.0002})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0005/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0005/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z0002, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z0005/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z0005 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.0005})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z001/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z001/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z001, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z001/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z001 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.001})


stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z002/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z002/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z002, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z002/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z002 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.002})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z004/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z004/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z004, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z004/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z004 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.004})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z006/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z006/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z006, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z006/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z006 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.006})


stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z008/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z008/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z008, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z008/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z008 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.008})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z010/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z010/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z010, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z010/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z010 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.010})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z014/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z014/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z014, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z014/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z014 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.014})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z017/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z017/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z017, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z017/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z017 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.017})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z020/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z020/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z020, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z020/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z020 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.020})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z030/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z030/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z030, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z030/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z030 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.030})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z040/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z040/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z040, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z040/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z040 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.040})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z060/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z060/HIIlines.out', usecols=(2,3,4,5,6,7,8), unpack=True)
ngrid_k_100_z060, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/kroupa_Mup300_ssp/z060/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z060 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.060})

ratios_k100_ssp = pd.concat([ratios_k100_ssp_z0001,ratios_k100_ssp_z0002,ratios_k100_ssp_z0005,ratios_k100_ssp_z001,ratios_k100_ssp_z002,ratios_k100_ssp_z004,ratios_k100_ssp_z006,ratios_k100_ssp_z008,ratios_k100_ssp_z010,ratios_k100_ssp_z014,ratios_k100_ssp_z017,ratios_k100_ssp_z020,ratios_k100_ssp_z030,ratios_k100_ssp_z040,ratios_k100_ssp_z060])

Neon_rat = ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]
Oxyg_rat = ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]

ratios_k100_ssp['Neon_rat'] = np.log10(Neon_rat)
ratios_k100_ssp['Oxyg_rat'] = np.log10(Oxyg_rat)

#ratios_k100_ssp = ratios_k100_ssp.loc[(ratios_k100_ssp['age']>6.6) &(ratios_k100_ssp['age']<7)& (ratios_k100_ssp['u']>=-3)& (ratios_k100_ssp['ne']>=1)& (ratios_k100_ssp['z']>0.002)]


ratios_k100_ssp_neon = ratios_k100_ssp.loc[(ratios_k100_ssp['Neon_rat']<0) & (ratios_k100_ssp['Neon_rat']>-2)]
ratios_k100_ssp_oxyg = ratios_k100_ssp.loc[(ratios_k100_ssp['Oxyg_rat']<0) & (ratios_k100_ssp['Oxyg_rat']>-2.4)]


ratios_k100_ssp_neon=ratios_k100_ssp_neon.sort_values(by=["age","u","ne"])
ratios_k100_ssp_oxyg=ratios_k100_ssp_oxyg.sort_values(by=["age","u","ne"])
#ratios_k100_ssp_neon.to_excel('Neon_file.xlsx')
#ratios_k100_ssp_oxyg.to_excel('Oxyg_file.xlsx')

ratios_k100_ssp = ratios_k100_ssp.loc[(ratios_k100_ssp['Neon_rat']<2) & (ratios_k100_ssp['Neon_rat']>-2)]
ratios_k100_ssp = ratios_k100_ssp.loc[(ratios_k100_ssp['Oxyg_rat']<2) & (ratios_k100_ssp['Oxyg_rat']>-2.4)]

ratios_k100_ssp.to_excel('all_models.xlsx')

ratios_k100_ssp = ratios_k100_ssp.sort_values(by=["u", "ne","age"])
ratios_k100_ssp_subset = ratios_k100_ssp.sort_values(by=["u", "ne","age"])


plt.figure()
plt.subplot(221)
plt.plot(ratios_k100_ssp['Oxyg_rat'],ratios_k100_ssp['age'],'o', color='orange')
#plt.hist(ratios_k100_ssp_neon["age"], alpha=0.5,color='grey')
#plt.hist(ratios_k100_ssp_oxyg["age"],alpha=0.5,color='orange')
#plt.hist(ratios_k100_ssp["age"],alpha=0.5,color='green')

plt.xlabel("log10(Age) [yr]", fontsize=14)
plt.ylabel("Ratios", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)

plt.subplot(222)

plt.hist(ratios_k100_ssp_neon["u"], alpha=0.5, color='grey')
#plt.hist(ratios_k100_ssp_oxyg["u"], alpha=0.5, color='orange')
plt.hist(ratios_k100_ssp["u"], alpha=0.5, color='green')
plt.xlabel("log10(U) ", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
#plt.ylim(-2,2)

plt.subplot(223)

plt.hist(ratios_k100_ssp_neon["z"], alpha=0.5, color='grey')
#plt.hist(ratios_k100_ssp_oxyg["z"], alpha=0.5, color='orange')
plt.hist(ratios_k100_ssp["z"], alpha=0.5, color='green')
plt.xlabel("Metallicity Z", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)


plt.subplot(224)

plt.hist(ratios_k100_ssp_neon["ne"], alpha=0.5, color='grey')
#plt.hist(ratios_k100_ssp_oxyg["ne"], alpha=0.5, color='orange')
plt.hist(ratios_k100_ssp["ne"], alpha=0.5, color='green')
plt.xlabel("log(ne)", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)



plt.figure()
#######MODELS%%%%%%%%%%%
plt.plot(np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]),np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]),'*',markersize=10,color='blue')
###%%%%%%%%%%%%%%Data in common
data_common = pd.read_excel("Ratios_common.xlsx", sheet_name='Sheet1')
data_common_s = data_common[data_common["ne_n"]==2]
plt.plot(data_common_s["Oxyg_rat_o"], data_common_s["Neon_rat_n"], '*',markersize=10,color='blue')
plt.plot(data_common_s["Oxyg_rat_o"], data_common_s["Neon_rat_n"], ':', markersize=10,color='black')
plt.text(data_common_s.iloc[0,23], data_common_s.iloc[0,11],'logU=-3.0', color='black')
plt.text(data_common_s.iloc[1,23], data_common_s.iloc[1,11],'logU=-1.5', color='black')
plt.text(-1.52, -0.19,'logAge=6.7', color='black')
plt.text(data_common_s.iloc[2,23], data_common_s.iloc[2,11],'logU=-1.5, logAge=6.8', color='black')
data_common_u = data_common[data_common["age_n"]==6.9]
plt.plot(data_common_u["Oxyg_rat_o"], data_common_u["Neon_rat_n"], '*',markersize=10,color='blue')
plt.text(-2.18,-0.32, 'logAge=6.9', color='black')
plt.text(-2.18,-0.44, 'logU=-2.5', color='black')
plt.text(-2.18,-0.55, 'log(ne)=-2.5', color='black')
plt.text(-2.18,-0.67, 'Z=0.060', color='black')
####
ratios_k100_ssp_md1 = ratios_k100_ssp.loc[(ratios_k100_ssp['age']==6.7) & (ratios_k100_ssp['ne']==2)& (ratios_k100_ssp['z']==0.017)]
#plt.plot(np.log10(ratios_k100_ssp_md1["O4"]/ratios_k100_ssp_md1["Ne3"]),np.log10(ratios_k100_ssp_md1["Ne3"]/ratios_k100_ssp_md1["Ne2"]),'o', color='black')
plt.plot(np.log10(ratios_k100_ssp_md1["O4"]/ratios_k100_ssp_md1["Ne3"]),np.log10(ratios_k100_ssp_md1["Ne3"]/ratios_k100_ssp_md1["Ne2"]),'--', color='orange')
plt.text(ratios_k100_ssp_md1.iloc[0,13], ratios_k100_ssp_md1.iloc[0,12],'logU=-3.0', color='black')
plt.text(ratios_k100_ssp_md1.iloc[3,13], ratios_k100_ssp_md1.iloc[3,12],'logU=-1.5', color='black')
#print(ratios_k100_ssp_md1.head())

ratios_k100_ssp_md2 = ratios_k100_ssp.loc[(ratios_k100_ssp['age']==6.6) & (ratios_k100_ssp['ne']==2)& (ratios_k100_ssp['z']==0.017)]
#print(ratios_k100_ssp_md2.head())
#plt.plot(np.log10(ratios_k100_ssp_md2["O4"]/ratios_k100_ssp_md2["Ne3"]),np.log10(ratios_k100_ssp_md2["Ne3"]/ratios_k100_ssp_md2["Ne2"]),'o', color='orange')
plt.plot(np.log10(ratios_k100_ssp_md2["O4"]/ratios_k100_ssp_md2["Ne3"]),np.log10(ratios_k100_ssp_md2["Ne3"]/ratios_k100_ssp_md2["Ne2"]),'--', color='orange')
plt.text(ratios_k100_ssp_md2.iloc[0,13], ratios_k100_ssp_md2.iloc[0,12],'logU=-3.0', color='black')
plt.text(ratios_k100_ssp_md2.iloc[3,13], ratios_k100_ssp_md2.iloc[3,12],'logU=-1.5', color='black')

#$################OBSERVATIONS
#import BPT_data_mir as mir
import BPT_data_opt as opt
#LaMassa data
Ne2_S5, eNe2_S5, Ne3_S5, eNe3_S5 = np.loadtxt('/Users/mariela/Documents/projects/HII/data/files/LaMassa_mir_S5_sample.dat', usecols=(4,6,8,10), unpack=True)

Ne_rat = Ne3_S5/Ne2_S5

mean_Ne_rat = np.mean(Ne_rat)
std_Ne_rat = np.std(Ne_rat)

Ne2_SS, eNe2_SS, Ne3_SS, eNe3_SS = np.loadtxt('/Users/mariela/Documents/projects/HII/data/files/LaMassa_mir_SSGSS_sample.dat', usecols=(5,7,9,11), unpack=True)

Ne_rat_SS = Ne3_SS/Ne2_SS

mean_Ne_rat_SS = np.mean(Ne_rat_SS)
std_Ne_rat_SS = np.std(Ne_rat_SS)
########### MIR observations####################

plt.fill([-3,3,3,-3],[mean_Ne_rat-std_Ne_rat,mean_Ne_rat-std_Ne_rat,mean_Ne_rat+std_Ne_rat,mean_Ne_rat+std_Ne_rat], alpha=0.3,color='purple',fill=True, label='S5 sample')

plt.fill([-3,3,3,-3],[mean_Ne_rat_SS-std_Ne_rat_SS,mean_Ne_rat_SS-std_Ne_rat_SS,mean_Ne_rat_SS+std_Ne_rat_SS,mean_Ne_rat_SS+std_Ne_rat_SS], alpha=0.3,  color='brown',fill=True, label='SSGSS sample')
########%%DATOS SINGS%%###################

plt.plot(log10(opt.rat_xmir_sing[8]),log10(opt.rat_ymir_sing[8]), '*', markersize=10,color='purple', label='SINGS:SF/Starburst')
plt.errorbar(log10(opt.rat_xmir_sing[8]),log10(opt.rat_ymir_sing[8]), xerr = opt.erat_xmir_sing[8]/(log(10)*opt.rat_xmir_sing[8]), yerr = opt.erat_ymir_sing[8]/(log(10)*opt.rat_ymir_sing[8]), fmt='*', markersize=10, color='purple')###Ver que objeto es este: NGC 1705

plt.plot(log10(opt.rat_xmir_sing[11]),log10(opt.rat_ymir_sing[11]), '*', markersize=10, color='purple')
plt.errorbar(log10(opt.rat_xmir_sing[11]),log10(opt.rat_ymir_sing[11]), xerr = opt.erat_xmir_sing[11]/(log(10)*opt.rat_xmir_sing[11]), yerr = opt.erat_ymir_sing[11]/(log(10)*opt.rat_ymir_sing[11]), fmt='*', markersize=10, color='purple')

plt.plot(log10(opt.rat_xmir_sing[19]),log10(opt.rat_ymir_sing[19]), '*', markersize=10, color='purple')
plt.errorbar(log10(opt.rat_xmir_sing[19]),log10(opt.rat_ymir_sing[19]), xerr = opt.erat_xmir_sing[19]/(log(10)*opt.rat_xmir_sing[19]), yerr = opt.erat_ymir_sing[19]/(log(10)*opt.rat_ymir_sing[19]), fmt='*', markersize=10, color='purple')

plt.plot(log10(opt.rat_xmir_sing[22]),log10(opt.rat_ymir_sing[22]), '*', markersize=10, color='purple')
plt.errorbar(log10(opt.rat_xmir_sing[22]),log10(opt.rat_ymir_sing[22]), xerr = opt.erat_xmir_sing[22]/(log(10)*opt.rat_xmir_sing[22]), yerr = opt.erat_ymir_sing[22]/(log(10)*opt.rat_ymir_sing[22]), fmt='*', markersize=10, color='purple')##Ver errores de este objeto: NGC 3773

plt.plot(log10(opt.rat_xmir_sing[20]),log10(opt.rat_ymir_sing[20]), 's', markersize=10, color='green')
plt.errorbar(log10(opt.rat_xmir_sing[20]),log10(opt.rat_ymir_sing[20]), xerr = opt.erat_xmir_sing[20]/(log(10)*opt.rat_xmir_sing[20]), yerr = opt.erat_ymir_sing[20]/(log(10)*opt.rat_ymir_sing[20]), fmt='s', markersize=10, color='green')

plt.plot(log10(opt.rat_xmir_sing[23]),log10(opt.rat_ymir_sing[23]), 's', markersize=10, color='green')
plt.errorbar(log10(opt.rat_xmir_sing[23]),log10(opt.rat_ymir_sing[23]), xerr = opt.erat_xmir_sing[23]/(log(10)*opt.rat_xmir_sing[23]), yerr = opt.erat_ymir_sing[23]/(log(10)*opt.rat_ymir_sing[23]), fmt='s', markersize=10, color='green')


plt.plot(log10(opt.rat_xmir_sing[4]),log10(opt.rat_ymir_sing[4]), 'o', markersize=10, color='black', label='SINGS:AGNs')
plt.errorbar(log10(opt.rat_xmir_sing[4]),log10(opt.rat_ymir_sing[4]), xerr = opt.erat_xmir_sing[4]/(log(10)*opt.rat_xmir_sing[4]), yerr = opt.erat_ymir_sing[4]/(log(10)*opt.rat_ymir_sing[4]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[5]),log10(opt.rat_ymir_sing[5]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[5]),log10(opt.rat_ymir_sing[5]), xerr = opt.erat_xmir_sing[5]/(log(10)*opt.rat_xmir_sing[5]), yerr = opt.erat_ymir_sing[5]/(log(10)*opt.rat_ymir_sing[5]), fmt='o', markersize=10, color='black')

plt.plot(log10(opt.rat_xmir_sing[7]),log10(opt.rat_ymir_sing[7]), 'o', markersize=10, color='black')#NGC 1566
plt.errorbar(log10(opt.rat_xmir_sing[7]),log10(opt.rat_ymir_sing[7]), xerr = opt.erat_xmir_sing[7]/(log(10)*opt.rat_xmir_sing[7]), yerr =
             opt.erat_ymir_sing[7]/(log(10)*opt.rat_ymir_sing[7]), fmt='o', markersize=10, color='black')

plt.plot(log10(opt.rat_xmir_sing[10]),log10(opt.rat_ymir_sing[10]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[10]),log10(opt.rat_ymir_sing[10]), xerr = opt.erat_xmir_sing[10]/(log(10)*opt.rat_xmir_sing[10]), yerr = opt.erat_ymir_sing[10]/(log(10)*opt.rat_ymir_sing[10]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[14]),log10(opt.rat_ymir_sing[14]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[14]),log10(opt.rat_ymir_sing[14]), xerr = opt.erat_xmir_sing[14]/(log(10)*opt.rat_xmir_sing[14]), yerr = opt.erat_ymir_sing[14]/(log(10)*opt.rat_ymir_sing[14]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[21]),log10(opt.rat_ymir_sing[21]), 'o', markersize=10, color='black')#NGC 3621
plt.errorbar(log10(opt.rat_xmir_sing[21]),log10(opt.rat_ymir_sing[21]), xerr = opt.erat_xmir_sing[21]/(log(10)*opt.rat_xmir_sing[21]), yerr = opt.erat_ymir_sing[21]/(log(10)*opt.rat_ymir_sing[21]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[25]),log10(opt.rat_ymir_sing[25]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[25]),log10(opt.rat_ymir_sing[25]), xerr = opt.erat_xmir_sing[25]/(log(10)*opt.rat_xmir_sing[25]), yerr = opt.erat_ymir_sing[25]/(log(10)*opt.rat_ymir_sing[25]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[29]),log10(opt.rat_ymir_sing[29]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[29]),log10(opt.rat_ymir_sing[29]), xerr = opt.erat_xmir_sing[29]/(log(10)*opt.rat_xmir_sing[29]), yerr = opt.erat_ymir_sing[29]/(log(10)*opt.rat_ymir_sing[29]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[30]),log10(opt.rat_ymir_sing[30]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[30]),log10(opt.rat_ymir_sing[30]), xerr = opt.erat_xmir_sing[30]/(log(10)*opt.rat_xmir_sing[30]), yerr = opt.erat_ymir_sing[30]/(log(10)*opt.rat_ymir_sing[30]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[31]),log10(opt.rat_ymir_sing[31]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[31]),log10(opt.rat_ymir_sing[31]), xerr = opt.erat_xmir_sing[31]/(log(10)*opt.rat_xmir_sing[31]), yerr = opt.erat_ymir_sing[31]/(log(10)*opt.rat_ymir_sing[31]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[32]),log10(opt.rat_ymir_sing[32]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[32]),log10(opt.rat_ymir_sing[32]), xerr = opt.erat_xmir_sing[32]/(log(10)*opt.rat_xmir_sing[32]), yerr = opt.erat_ymir_sing[32]/(log(10)*opt.rat_ymir_sing[32]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[33]),log10(opt.rat_ymir_sing[33]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[33]),log10(opt.rat_ymir_sing[33]), xerr = opt.erat_xmir_sing[33]/(log(10)*opt.rat_xmir_sing[33]), yerr = opt.erat_ymir_sing[33]/(log(10)*opt.rat_ymir_sing[33]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[34]),log10(opt.rat_ymir_sing[34]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[34]),log10(opt.rat_ymir_sing[34]), xerr = opt.erat_xmir_sing[34]/(log(10)*opt.rat_xmir_sing[34]), yerr = opt.erat_ymir_sing[34]/(log(10)*opt.rat_ymir_sing[34]), fmt='o', markersize=10, color='black')
plt.plot(log10(opt.rat_xmir_sing[36]),log10(opt.rat_ymir_sing[36]), 'o', markersize=10, color='black')
plt.errorbar(log10(opt.rat_xmir_sing[36]),log10(opt.rat_ymir_sing[36]), xerr = opt.erat_xmir_sing[36]/(log(10)*opt.rat_xmir_sing[36]), yerr = opt.erat_ymir_sing[36]/(log(10)*opt.rat_ymir_sing[36]), fmt='o', markersize=10, color='black')


plt.plot(log10(opt.rat_xmir_sing[28]),log10(opt.rat_ymir_sing[28]), 's', markersize=10, color='green', label='SINGS:SF/AGN')
plt.errorbar(log10(opt.rat_xmir_sing[28]),log10(opt.rat_ymir_sing[28]), xerr = opt.erat_xmir_sing[28]/(log(10)*opt.rat_xmir_sing[28]), yerr = opt.erat_ymir_sing[28]/(log(10)*opt.rat_ymir_sing[28]), fmt='s', markersize=10, color='green')

plt.plot(log10(opt.rat_xmir_sing[35]),log10(opt.rat_ymir_sing[35]), 's', markersize=10, color='green')
plt.errorbar(log10(opt.rat_xmir_sing[35]),log10(opt.rat_ymir_sing[35]), xerr = opt.erat_xmir_sing[35]/(log(10)*opt.rat_xmir_sing[35]), yerr = opt.erat_ymir_sing[35]/(log(10)*opt.rat_ymir_sing[35]), fmt='s', markersize=10, color='green')



plt.legend(loc = 'lower right', numpoints=1, prop={'size':16})
text(0.02,0.02,'BAT-AGNs', fontsize=16)
x0=(0,0)
y0=(0,0)
y1=(-2.5,2.2)
x1=(-2.5,2.2)
plt.plot(x0,y1,'k:', color='grey')
plt.plot(x1,y0,'k:', color='grey')

plt.xlabel("log10([OIV]/[Ne III])", fontsize=14)
plt.ylabel("log10([Ne III]/[Ne II])", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.xlim(-2.5,0.8)
plt.ylim(-2,2.2)

plt.show()











