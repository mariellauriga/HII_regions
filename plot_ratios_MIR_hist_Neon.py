import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

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

plt.figure('ratios_Neon_comparing_models.png')


####Full DATA
#data = pd.concat([k_sfr_100.ratios_k100_sfr,k_sfr_300.ratios_k100_sfr,k_ssp_100.ratios_k100_ssp,k_ssp_300.ratios_k100_ssp,s_sfr_100.ratios_k100_sfr,s_sfr_300.ratios_k100_sfr,s_ssp_100.ratios_k100_ssp,s_ssp_300.ratios_k100_ssp,x_sfr_100.ratios_k100_sfr,x_sfr_300.ratios_k100_sfr,x_ssp_100.ratios_k100_ssp,x_ssp_300.ratios_k100_ssp])

#data = data[np.log10(data["O4"]/data["Ne3"])>-2]
#data = data[np.log10(data["Ne3"]/data["Ne2"])>-2]
#data = data[np.log10(data["Ne3"]/data["Ne2"])< 2]

###%%%%%%%%%%%%%%Data in common
#data_common = pd.read_excel("Ratios_common.xlsx", sheet_name='Sheet1')
#data_common_s = data_common[data_common["ne_n"]==2]
#plt.plot(data_common_s["Oxyg_rat_o"], data_common_s["Neon_rat_n"], 'o',markersize=10,color='blue')
#plt.plot(data_common_s["Oxyg_rat_o"], data_common_s["Neon_rat_n"], ':', markersize=10,color='black')
#plt.text(data_common_s.iloc[0,23], data_common_s.iloc[0,11],'logU=-3.0', color='black', fontsize=12)
#plt.text(data_common_s.iloc[1,23], data_common_s.iloc[1,11],'logU=-1.5', color='black', fontsize=12)
#plt.text(-1.52, -0.19,'logAge=6.7', color='black', fontsize=12)
#plt.text(data_common_s.iloc[2,23], data_common_s.iloc[2,11],'logU=-1.5, logAge=6.8', color='black', fontsize=12)
#data_common_u = data_common[data_common["age_n"]==6.9]
#plt.plot(data_common_u["Oxyg_rat_o"], data_common_u["Neon_rat_n"], 'o',markersize=10,color='blue')
#plt.text(-2.18,-0.32, 'logAge=6.9', color='black', fontsize=12)
#plt.text(-2.18,-0.44, 'logU=-2.5', color='black', fontsize=12)
#plt.text(-2.18,-0.55, 'log(ne)=-2.5', color='black', fontsize=12)
#plt.text(-2.18,-0.67, 'Z=0.060', color='black', fontsize=12)
####


####KROUPA
datak100sfr = k_sfr_100.ratios_k100_sfr
datak100sfr = datak100sfr[np.log10(datak100sfr["O4"]/datak100sfr["Ne3"])>-2.5]
datak100sfr = datak100sfr[np.log10(datak100sfr["Ne3"]/datak100sfr["Ne2"])>-2]
datak100sfr = datak100sfr[np.log10(datak100sfr["Ne3"]/datak100sfr["Ne2"])< 2]
neon_datak100sfr = np.log10(datak100sfr["Ne3"]/datak100sfr["Ne2"])
oxygen_datak100sfr = np.log10(datak100sfr["O4"]/datak100sfr["Ne3"])

datak100ssp = k_ssp_100.ratios_k100_ssp
datak100ssp = datak100ssp[np.log10(datak100ssp["O4"]/datak100ssp["Ne3"])>-2.5]
datak100ssp = datak100ssp[np.log10(datak100ssp["Ne3"]/datak100ssp["Ne2"])>-2]
datak100ssp = datak100ssp[np.log10(datak100ssp["Ne3"]/datak100ssp["Ne2"])< 2]
neon_datak100ssp = np.log10(datak100ssp["Ne3"]/datak100ssp["Ne2"])
oxygen_datak100ssp = np.log10(datak100ssp["O4"]/datak100ssp["Ne3"])

datak300sfr = k_sfr_300.ratios_k100_sfr
datak300sfr = datak300sfr[np.log10(datak300sfr["O4"]/datak300sfr["Ne3"])>-2.5]
datak300sfr = datak300sfr[np.log10(datak300sfr["Ne3"]/datak300sfr["Ne2"])>-2]
datak300sfr = datak300sfr[np.log10(datak300sfr["Ne3"]/datak300sfr["Ne2"])< 2]
neon_datak300sfr = np.log10(datak300sfr["Ne3"]/datak300sfr["Ne2"])
oxygen_datak300sfr = np.log10(datak300sfr["O4"]/datak300sfr["Ne3"])

datak300ssp = k_ssp_300.ratios_k100_ssp
datak300ssp = datak300ssp[np.log10(datak300ssp["O4"]/datak300ssp["Ne3"])>-2.5]
datak300ssp = datak300ssp[np.log10(datak300ssp["Ne3"]/datak300ssp["Ne2"])>-2]
datak300ssp = datak300ssp[np.log10(datak300ssp["Ne3"]/datak300ssp["Ne2"])< 2]
neon_datak300ssp = np.log10(datak300ssp["Ne3"]/datak300ssp["Ne2"])
oxygen_datak300ssp = np.log10(datak300ssp["O4"]/datak300ssp["Ne3"])


####Salpeter
datas100sfr = s_sfr_100.ratios_k100_sfr
datas100sfr = datas100sfr[np.log10(datas100sfr["O4"]/datas100sfr["Ne3"])>-2.5]
datas100sfr = datas100sfr[np.log10(datas100sfr["Ne3"]/datas100sfr["Ne2"])>-2]
datas100sfr = datas100sfr[np.log10(datas100sfr["Ne3"]/datas100sfr["Ne2"])< 2]
neon_datas100sfr = np.log10(datas100sfr["Ne3"]/datas100sfr["Ne2"])
oxygen_datas100sfr = np.log10(datas100sfr["O4"]/datas100sfr["Ne3"])

datas100ssp = s_ssp_100.ratios_k100_ssp
datas100ssp = datas100ssp[np.log10(datas100ssp["O4"]/datas100ssp["Ne3"])>-2.5]
datas100ssp = datas100ssp[np.log10(datas100ssp["Ne3"]/datas100ssp["Ne2"])>-2]
datas100ssp = datas100ssp[np.log10(datas100ssp["Ne3"]/datas100ssp["Ne2"])< 2]
neon_datas100ssp = np.log10(datas100ssp["Ne3"]/datas100ssp["Ne2"])
oxygen_datas100ssp = np.log10(datas100ssp["O4"]/datas100ssp["Ne3"])

datas300sfr = s_sfr_300.ratios_k100_sfr
datas300sfr = datas300sfr[np.log10(datas300sfr["O4"]/datas300sfr["Ne3"])>-2.5]
datas300sfr = datas300sfr[np.log10(datas300sfr["Ne3"]/datas300sfr["Ne2"])>-2]
datas300sfr = datas300sfr[np.log10(datas300sfr["Ne3"]/datas300sfr["Ne2"])< 2]
neon_datas300sfr = np.log10(datas300sfr["Ne3"]/datas300sfr["Ne2"])
oxygen_datas300sfr = np.log10(datas300sfr["O4"]/datas300sfr["Ne3"])

datas300ssp = s_ssp_300.ratios_k100_ssp
datas300ssp = datas300ssp[np.log10(datas300ssp["O4"]/datas300ssp["Ne3"])>-2.5]
datas300ssp = datas300ssp[np.log10(datas300ssp["Ne3"]/datas300ssp["Ne2"])>-2]
datas300ssp = datas300ssp[np.log10(datas300ssp["Ne3"]/datas300ssp["Ne2"])< 2]
neon_datas300ssp = np.log10(datas300ssp["Ne3"]/datas300ssp["Ne2"])
oxygen_datas300ssp = np.log10(datas300ssp["O4"]/datas300ssp["Ne3"])

####X030
datax100sfr = x_sfr_100.ratios_k100_sfr
datax100sfr = datax100sfr[np.log10(datax100sfr["O4"]/datax100sfr["Ne3"])>-2.5]
datax100sfr = datax100sfr[np.log10(datax100sfr["Ne3"]/datax100sfr["Ne2"])>-2]
datax100sfr = datax100sfr[np.log10(datax100sfr["Ne3"]/datax100sfr["Ne2"])< 2]
neon_datax100sfr = np.log10(datax100sfr["Ne3"]/datax100sfr["Ne2"])
oxygen_datax100sfr = np.log10(datax100sfr["O4"]/datax100sfr["Ne3"])

datax100ssp = x_ssp_100.ratios_k100_ssp
datax100ssp = datax100ssp[np.log10(datax100ssp["O4"]/datax100ssp["Ne3"])>-2.5]
datax100ssp = datax100ssp[np.log10(datax100ssp["Ne3"]/datax100ssp["Ne2"])>-2]
datax100ssp = datax100ssp[np.log10(datax100ssp["Ne3"]/datax100ssp["Ne2"])< 2]
neon_datax100ssp = np.log10(datax100ssp["Ne3"]/datax100ssp["Ne2"])
oxygen_datax100ssp = np.log10(datax100ssp["O4"]/datax100ssp["Ne3"])

datax300sfr = x_sfr_300.ratios_k100_sfr
datax300sfr = datax300sfr[np.log10(datax300sfr["O4"]/datax300sfr["Ne3"])>-2.5]
datax300sfr = datax300sfr[np.log10(datax300sfr["Ne3"]/datax300sfr["Ne2"])>-2]
datax300sfr = datax300sfr[np.log10(datax300sfr["Ne3"]/datax300sfr["Ne2"])< 2]
neon_datax300sfr = np.log10(datax300sfr["Ne3"]/datax300sfr["Ne2"])
oxygen_datax300sfr = np.log10(datax300sfr["O4"]/datax300sfr["Ne3"])

datax300ssp = x_ssp_300.ratios_k100_ssp
datax300ssp = datax300ssp[np.log10(datax300ssp["O4"]/datax300ssp["Ne3"])>-2.5]
datax300ssp = datax300ssp[np.log10(datax300ssp["Ne3"]/datax300ssp["Ne2"])>-2]
datax300ssp = datax300ssp[np.log10(datax300ssp["Ne3"]/datax300ssp["Ne2"])< 2]
neon_datax300ssp = np.log10(datax300ssp["Ne3"]/datax300ssp["Ne2"])
oxygen_datax300ssp = np.log10(datax300ssp["O4"]/datax300ssp["Ne3"])

plt.subplot(221)
plt.title(r"M$_{up}=100$ M$_{\odot}$, Continuous")
plt.hist(neon_datax100sfr, alpha=0.5, color='orange',label='x030')
plt.hist(neon_datak100sfr, alpha=0.5,color='blue',label='Kroupa')
plt.hist(neon_datas100sfr, alpha=0.5, color='brown',label='Salpeter')
plt.legend(loc='upper left')
plt.xlim(-2,2)

plt.subplot(222)
plt.title(r"M$_{up}=100$ M$_{\odot}$, Single")
plt.hist(neon_datax100ssp, alpha=0.5, color='orange',label='x030')
plt.hist(neon_datak100ssp, alpha=0.5, color='blue',label='Kroupa')
plt.hist(neon_datas100ssp, alpha=0.5, color='brown',label='Salpeter')
plt.xlim(-2,2)

plt.subplot(223)
plt.title(r"M$_{up}=300$ M$_{\odot}$, Continuous")
plt.hist(neon_datax300sfr, alpha=0.5, color='orange',label='x030')
plt.hist(neon_datak300sfr, alpha=0.5, color='blue',label='Kroupa')
plt.hist(neon_datas300sfr, alpha=0.5, color='brown', label='Salpeter')
plt.xlabel(r"log([Ne$_{III}$]/[Ne$_{II}$])")
plt.xlim(-2,2)

plt.subplot(224)
plt.title(r"M$_{up}=300$ M$_{\odot}$, Single")
plt.hist(neon_datax300ssp, alpha=0.5, color='orange',label='x030')
plt.hist(neon_datak300ssp, alpha=0.5, color='blue',label='Kroupa')
plt.hist(neon_datas300ssp, alpha=0.5, color='brown',label='Salpeter')
plt.xlabel(r"log([Ne$_{III}$]/[Ne$_{II}$])")
plt.xlim(-2,2)

plt.figure()
pos_k=(4,5)
pos_s=(2,3)
pos_x=(0,1)
pos = (0,1,2,3,4,5)
plt.subplot(221)
plt.title(r"M$_{up}=100$ M$_{\odot}$, Continuous")
values_x = (datax100sfr['stopC'][datax100sfr['stopC']==4].sum(),datax100sfr['stopC'][datax100sfr['stopC']==20].sum())
barh(pos_x,values_x,align='center', alpha=0.5, color='orange')
values_k = (datak100sfr['stopC'][datak100sfr['stopC']==4].sum(),datak100sfr['stopC'][datak100sfr['stopC']==20].sum())
barh(pos_k,values_k,align='center', alpha=0.5, color='blue')
values_s = (datas100sfr['stopC'][datas100sfr['stopC']==4].sum(),datas100sfr['stopC'][datas100sfr['stopC']==20].sum())
barh(pos_s,values_s,align='center', alpha=0.5, color='brown')


yticks(pos, ('temp','den','temp','den','temp','den'), rotation=90)
plt.xlim(0,11000)

plt.subplot(222)
plt.title(r"M$_{up}=100$ M$_{\odot}$, Single")
values_x = (datax100ssp['stopC'][datax100ssp['stopC']==4].sum(),datax100ssp['stopC'][datax100ssp['stopC']==20].sum())
barh(pos_x,values_x,align='center', alpha=0.5, color='orange', label='x030')
values_k = (datak100ssp['stopC'][datak100ssp['stopC']==4].sum(),datak100ssp['stopC'][datak100ssp['stopC']==20].sum())
barh(pos_k,values_k,align='center', alpha=0.5, color='blue', label='Kroupa')
values_s = (datas100ssp['stopC'][datas100ssp['stopC']==4].sum(),datas100ssp['stopC'][datas100ssp['stopC']==20].sum())
barh(pos_s,values_s,align='center', alpha=0.5, color='brown', label='Salpeter')


yticks(pos, ('temp','den','temp','den','temp','den'), rotation=90)

plt.xlim(0,11000)

plt.subplot(223)
plt.title(r"M$_{up}=300$ M$_{\odot}$, Continuous")
values_x = (datax300sfr['stopC'][datax300sfr['stopC']==4].sum(),datax300sfr['stopC'][datax300sfr['stopC']==20].sum())
barh(pos_x,values_x,align='center', alpha=0.5, color='orange')
values_k = (datak300sfr['stopC'][datak300sfr['stopC']==4].sum(),datak300sfr['stopC'][datak300sfr['stopC']==20].sum())
barh(pos_k,values_k,align='center', alpha=0.5, color='blue')
values_s = (datas300sfr['stopC'][datas300sfr['stopC']==4].sum(),datas300sfr['stopC'][datas300sfr['stopC']==20].sum())
barh(pos_s,values_s,align='center', alpha=0.5, color='brown')


yticks(pos, ('temp','den','temp','den','temp','den'), rotation=90)
plt.xlabel("Number of models")
plt.xlim(0,11000)

plt.subplot(224)
plt.title(r"M$_{up}=300$ M$_{\odot}$, Single")
values_x = (datax300ssp['stopC'][datax300ssp['stopC']==4].sum(),datax300ssp['stopC'][datax300ssp['stopC']==20].sum())
barh(pos_x,values_x,align='center', alpha=0.5, color='orange', label='x030')
values_k = (datak300ssp['stopC'][datak300ssp['stopC']==4].sum(),datak300ssp['stopC'][datak300ssp['stopC']==20].sum())
barh(pos_k,values_k,align='center', alpha=0.5, color='blue', label='Kroupa')
values_s = (datas300ssp['stopC'][datas300ssp['stopC']==4].sum(),datas300ssp['stopC'][datas300ssp['stopC']==20].sum())
barh(pos_s,values_s,align='center', alpha=0.5, color='brown', label='Salpeter')


yticks(pos, ('temp','den','temp','den','temp','den'), rotation=90)
plt.xlabel("Number of models")
plt.xlim(0,11000)
plt.legend(loc='upper right')
plt.show()
