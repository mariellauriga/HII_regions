import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z0002/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563, O3_88p3, PAH3p3, PAH6p2, PAH7p9, PAH11p3, PAH11p8, PAH13p3 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z0002/HIIlines.out', usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)
ngrid_k_100_z0002, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z0002/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z0002 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "O3_88":O3_88p3, "PAH3p3":PAH3p3, "PAH6p2":PAH6p2, "PAH7p9":PAH7p9, "PAH11p3":PAH11p3, "PAH11p8":PAH11p8, "PAH13p3":PAH13p3, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.0002})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z002/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563, O3_88p3, PAH3p3, PAH6p2, PAH7p9, PAH11p3, PAH11p8, PAH13p3 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z002/HIIlines.out', usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)
ngrid_k_100_z002, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z002/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z002 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "O3_88":O3_88p3, "PAH3p3":PAH3p3, "PAH6p2":PAH6p2, "PAH7p9":PAH7p9, "PAH11p3":PAH11p3, "PAH11p8":PAH11p8, "PAH13p3":PAH13p3, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.002})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z008/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563, O3_88p3, PAH3p3, PAH6p2, PAH7p9, PAH11p3, PAH11p8, PAH13p3 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z008/HIIlines.out', usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)
ngrid_k_100_z008, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z008/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z008 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "O3_88":O3_88p3, "PAH3p3":PAH3p3, "PAH6p2":PAH6p2, "PAH7p9":PAH7p9, "PAH11p3":PAH11p3, "PAH11p8":PAH11p8, "PAH13p3":PAH13p3, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.008})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z017/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563, O3_88p3, PAH3p3, PAH6p2, PAH7p9, PAH11p3, PAH11p8, PAH13p3 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z017/HIIlines.out', usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)
ngrid_k_100_z017, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z017/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z017 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "O3_88":O3_88p3, "PAH3p3":PAH3p3, "PAH6p2":PAH6p2, "PAH7p9":PAH7p9, "PAH11p3":PAH11p3, "PAH11p8":PAH11p8, "PAH13p3":PAH13p3, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.017})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z030/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563, O3_88p3, PAH3p3, PAH6p2, PAH7p9, PAH11p3, PAH11p8, PAH13p3 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z030/HIIlines.out', usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)
ngrid_k_100_z030, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z030/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z030 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "O3_88":O3_88p3, "PAH3p3":PAH3p3, "PAH6p2":PAH6p2, "PAH7p9":PAH7p9, "PAH11p3":PAH11p3, "PAH11p8":PAH11p8, "PAH13p3":PAH13p3, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.030})

stop = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z060/sttoping_criterium.txt', unpack=True)
O4, Ne3, Ne2, O3_5007, H1_4861, N2_6584, H1_6563, O3_88p3, PAH3p3, PAH6p2, PAH7p9, PAH11p3, PAH11p8, PAH13p3 = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z060/HIIlines.out', usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)
ngrid_k_100_z060, age, ion, ne = np.loadtxt('/Volumes/Samsung_T5/lines_nH21/sfr_ssp/x030_Mup100_ssp/z060/HIIlines_grid.grd', usecols=(0,6,7,8),unpack=True)
#Make the data frame
ratios_k100_ssp_z060 = pd.DataFrame({"O4":O4, "Ne3":Ne3, "Ne2":Ne2, "O3_5007l":O3_5007, "Hbeta":H1_4861, "N2":N2_6584, "Halpha":H1_6563, "O3_88":O3_88p3, "PAH3p3":PAH3p3, "PAH6p2":PAH6p2, "PAH7p9":PAH7p9, "PAH11p3":PAH11p3, "PAH11p8":PAH11p8, "PAH13p3":PAH13p3, "age":age, "u":ion, "ne":ne, "stopC":stop, "z":0.060})


ratios_k100_ssp = pd.concat([ratios_k100_ssp_z0002,ratios_k100_ssp_z002,ratios_k100_ssp_z008,ratios_k100_ssp_z017,ratios_k100_ssp_z030,ratios_k100_ssp_z060])


plt.figure('param_ratios_x100_ssp.png')
#ratios_k100_ssp_z0002=ratios_k100_ssp_z0002.sort_values(by=["u","ne", "age"])
#ratios_k100_ssp = ratios_k100_ssp.groupby(by=["ne"])
ratios_k100_ssp = ratios_k100_ssp.sort_values(by=["u", "ne","age"])

plt.subplot(221)
#plt.plot(ratios_k100_ssp_z0002["age"], np.log10(ratios_k100_ssp_z0002["Ne3"]/ratios_k100_ssp_z0002["Ne2"]), 'o',color='navy')
plt.plot(ratios_k100_ssp["age"], np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]), 'o',color='navy')
plt.plot(ratios_k100_ssp["age"], np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]), '*',color='orange')
plt.xlabel("log10(Age) [yr]", fontsize=14)
plt.ylabel("Ratios", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.ylim(-2,2)

plt.subplot(222)
plt.plot(ratios_k100_ssp["u"], np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]),'o',color='navy')
plt.plot(ratios_k100_ssp["u"], np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]),'o',color='orange')
plt.xlabel("log10(U) ", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.ylim(-2,2)

plt.subplot(223)
plt.plot(ratios_k100_ssp["z"], np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]),'o',color='navy')
plt.plot(ratios_k100_ssp["z"], np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]),'o',color='orange')
plt.xlabel("Metallicity Z", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.ylabel("Ratios", fontsize=14)
plt.ylim(-2,2)

plt.subplot(224)
plt.plot(ratios_k100_ssp["ne"], np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]),'o',color='navy')
plt.plot(ratios_k100_ssp["ne"], np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]),'o',color='orange')
plt.xlabel("ne", fontsize=14)
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.ylim(-2,2)

plt.figure()

plt.plot(np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]), np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]),'*', color='blue')
plt.text(0.02,0.02,'BAT-AGNs', fontsize=16)
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
plt.savefig('figures/BPT_ssp_x030_Mup100')


plt.figure()

plt.plot(np.log10(ratios_k100_ssp["O4"]/ratios_k100_ssp["Ne3"]), np.log10(ratios_k100_ssp["Ne3"]/ratios_k100_ssp["Ne2"]),'*', color='blue')
plt.text(0.02,0.02,'BAT-AGNs', fontsize=16)
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
plt.savefig('figures/BPT_ssp_x030_Mup100')


plt.show()
