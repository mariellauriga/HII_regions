import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plot_ratios_param_kroupa_sfr_Mup100 as k_sfr_100
import plot_ratios_param_kroupa_sfr_Mup300 as k_sfr_300
import plot_ratios_param_kroupa_ssp_Mup100 as k_ssp_100
import plot_ratios_param_kroupa_ssp_Mup300 as k_ssp_300
import plot_ratios_param_salpeter_sfr_Mup100 as s_sfr_100
import plot_ratios_param_salpeter_sfr_Mup300 as s_sfr_300
import plot_ratios_param_salpeter_ssp_Mup100 as s_ssp_100
import plot_ratios_param_salpeter_ssp_Mup300 as s_ssp_300
import plot_ratios_param_x030_sfr_Mup100 as x_sfr_100
import plot_ratios_param_x030_sfr_Mup300 as x_sfr_300
import plot_ratios_param_x030_ssp_Mup100 as x_ssp_100
import plot_ratios_param_x030_ssp_Mup300 as x_ssp_300

plt.figure('ratios.png')
data1k = k_sfr_100.ratios_k100_sfr
data2k = k_sfr_300.ratios_k100_sfr
data3k = k_ssp_100.ratios_k100_ssp
data4k = k_ssp_300.ratios_k100_ssp

data1k = data1k[np.log10(data1k["O4"]/data1k["Ne3"])>-2]
data1k = data1k[np.log10(data1k["Ne3"]/data1k["Ne2"])>-2]
data1k = data1k[np.log10(data1k["Ne3"]/data1k["Ne2"])< 2]

data2k = data2k[np.log10(data2k["O4"]/data2k["Ne3"])>-2]
data2k = data2k[np.log10(data2k["Ne3"]/data2k["Ne2"])>-2]
data2k = data2k[np.log10(data2k["Ne3"]/data2k["Ne2"])< 2]

data3k = data3k[np.log10(data3k["O4"]/data3k["Ne3"])>-2]
data3k = data3k[np.log10(data3k["Ne3"]/data3k["Ne2"])>-2]
data3k = data3k[np.log10(data3k["Ne3"]/data3k["Ne2"])< 2]

data4k = data4k[np.log10(data4k["O4"]/data4k["Ne3"])>-2]
data4k = data4k[np.log10(data4k["Ne3"]/data4k["Ne2"])>-2]
data4k = data4k[np.log10(data4k["Ne3"]/data4k["Ne2"])< 2]

#plt.plot(np.log10(data2k["O4"]/data2k["Ne3"]), np.log10(data2k["Ne3"]/data2k["Ne2"]),'*',color='orange')
#plt.plot(np.log10(data3k["O4"]/data3k["Ne3"]), np.log10(data3k["Ne3"]/data3k["Ne2"]),'*',color='orange')
#plt.plot(np.log10(data4k["O4"]/data4k["Ne3"]), np.log10(data4k["Ne3"]/data4k["Ne2"]),'*',color='orange')

data1s = s_sfr_100.ratios_k100_sfr
data2s = s_sfr_300.ratios_k100_sfr
data3s = s_ssp_100.ratios_k100_ssp
data4s = s_ssp_300.ratios_k100_ssp

data1s = data1s[np.log10(data1s["O4"]/data1s["Ne3"])>-2]
data1s = data1s[np.log10(data1s["Ne3"]/data1s["Ne2"])>-2]
data1s = data1s[np.log10(data1s["Ne3"]/data1s["Ne2"])< 2]

data2s = data2s[np.log10(data2s["O4"]/data2s["Ne3"])>-2]
data2s = data2s[np.log10(data2s["Ne3"]/data2s["Ne2"])>-2]
data2s = data2s[np.log10(data2s["Ne3"]/data2s["Ne2"])< 2]

data3s = data3s[np.log10(data3s["O4"]/data3s["Ne3"])>-2]
data3s = data3s[np.log10(data3s["Ne3"]/data3s["Ne2"])>-2]
data3s = data3s[np.log10(data3s["Ne3"]/data3s["Ne2"])< 2]

data4s = data4s[np.log10(data4s["O4"]/data4s["Ne3"])>-2]
data4s = data4s[np.log10(data4s["Ne3"]/data4s["Ne2"])>-2]
data4s = data4s[np.log10(data4s["Ne3"]/data4s["Ne2"])< 2]
#plt.plot(np.log10(data1s["O4"]/data1s["Ne3"]), np.log10(data1s["Ne3"]/data1s["Ne2"]),'*',color='orange')
#plt.plot(np.log10(data2s["O4"]/data2s["Ne3"]), np.log10(data2s["Ne3"]/data2s["Ne2"]),'*',color='orange')
#plt.plot(np.log10(data3s["O4"]/data3s["Ne3"]), np.log10(data3s["Ne3"]/data3s["Ne2"]),'*',color='orange')**
#plt.plot(np.log10(data4s["O4"]/data4s["Ne3"]), np.log10(data4s["Ne3"]/data4s["Ne2"]),'*',color='orange')**

data1x = x_sfr_100.ratios_k100_sfr
data2x = x_sfr_300.ratios_k100_sfr
data3x = x_ssp_100.ratios_k100_ssp
data4x = x_ssp_300.ratios_k100_ssp
data1x = data1x[np.log10(data1x["O4"]/data1x["Ne3"])>-2]
data1x = data1x[np.log10(data1x["Ne3"]/data1x["Ne2"])>-2]
data1x = data1x[np.log10(data1x["Ne3"]/data1x["Ne2"])< 2]

data2x = data2x[np.log10(data2x["O4"]/data2x["Ne3"])>-2]
data2x = data2x[np.log10(data2x["Ne3"]/data2x["Ne2"])>-2]
data2x = data2x[np.log10(data2x["Ne3"]/data2x["Ne2"])< 2]

data3x = data3x[np.log10(data3x["O4"]/data3x["Ne3"])>-2]
data3x = data3x[np.log10(data3x["Ne3"]/data3x["Ne2"])>-2]
data3x = data3x[np.log10(data3x["Ne3"]/data3x["Ne2"])< 2]

data4x = data4x[np.log10(data4x["O4"]/data4x["Ne3"])>-2]
data4x = data4x[np.log10(data4x["Ne3"]/data4x["Ne2"])>-2]
data4x = data4x[np.log10(data4x["Ne3"]/data4x["Ne2"])< 2]
#plt.plot(np.log10(data1x["O4"]/data1x["Ne3"]), np.log10(data1x["Ne3"]/data1x["Ne2"]),'*',color='orange')
#plt.plot(np.log10(data2x["O4"]/data2x["Ne3"]), np.log10(data2x["Ne3"]/data2x["Ne2"]),'^',color='orange')
#plt.plot(np.log10(data3x["O4"]/data3x["Ne3"]), np.log10(data3x["Ne3"]/data3x["Ne2"]),'o',color='orange')
#plt.plot(np.log10(data4x["O4"]/data4x["Ne3"]), np.log10(data4x["Ne3"]/data4x["Ne2"]),'s',color='orange')

####Full DATA
data100 = pd.concat([k_sfr_100.ratios_k100_sfr,k_sfr_300.ratios_k100_sfr,k_ssp_100.ratios_k100_ssp,k_ssp_300.ratios_k100_ssp,s_sfr_100.ratios_k100_sfr,s_sfr_300.ratios_k100_sfr,s_ssp_100.ratios_k100_ssp,s_ssp_300.ratios_k100_ssp])

data100x = pd.concat([x_sfr_100.ratios_k100_sfr,x_ssp_100.ratios_k100_ssp])

data300 = pd.concat([k_sfr_300.ratios_k100_sfr,k_ssp_300.ratios_k100_ssp,s_sfr_300.ratios_k100_sfr,s_ssp_300.ratios_k100_ssp])

data300x = pd.concat([x_sfr_300.ratios_k100_sfr,x_ssp_300.ratios_k100_ssp])

data100 = data100[np.log10(data100["O4"]/data100["Ne3"])>-2]
data100 = data100[np.log10(data100["Ne3"]/data100["Ne2"])>-2]
data100 = data100[np.log10(data100["Ne3"]/data100["Ne2"])< 2]

data300 = data300[np.log10(data300["O4"]/data300["Ne3"])>-2]
data300 = data300[np.log10(data300["Ne3"]/data300["Ne2"])>-2]
data300 = data300[np.log10(data300["Ne3"]/data300["Ne2"])< 2]

data100x = data100x[np.log10(data100x["O4"]/data100x["Ne3"])>-2]
data100x = data100x[np.log10(data100x["Ne3"]/data100x["Ne2"])>-2]
data100x = data100x[np.log10(data100x["Ne3"]/data100x["Ne2"])< 2]

data300x = data300x[np.log10(data300x["O4"]/data300x["Ne3"])>-2]
data300x = data300x[np.log10(data300x["Ne3"]/data300x["Ne2"])>-2]
data300x = data300x[np.log10(data300x["Ne3"]/data300x["Ne2"])< 2]


plt.subplot(221)
plt.hist(data100["u"], label='k+s+sfr+ssp+Mup100')
plt.hist(data300["u"], label='k+s+sfr+ssp+Mup300')
plt.hist(data100x["u"], label='x+sfr+ssp+Mup100')
plt.hist(data300x["u"], label='x+sfr+ssp+Mup300')
plt.legend(loc='best')
plt.subplot(222)
plt.hist(data100["age"])
plt.hist(data300["age"])
plt.hist(data100x["age"])
plt.hist(data300x["age"])

plt.subplot(223)
plt.hist(data100["ne"])
plt.hist(data300["ne"])
plt.hist(data100x["ne"])
plt.hist(data300x["ne"])

plt.subplot(224)
plt.hist(data100["z"])
plt.hist(data300["z"])
plt.hist(data100x["z"])
plt.hist(data300x["z"])

#data_mean = data.groupby(by=["ne"]).mean()
#data_std = data.groupby(by=["ne"]).std()
#print("Full Data")
#print(data_mean)
#print(data_std)
#plt.plot(np.log10(data["O4"]/data["Ne3"]),np.log10(data["Ne3"]/data["Ne2"]),'o',color='navy')



plt.show()
