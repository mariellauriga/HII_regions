import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from matplotlib.patches import Ellipse, Polygon
import math
import scipy.optimize as optimization
from scipy.interpolate import interp1d


import h5py
h = h5py.File('combined_models_MIR.hdf5')
lrO4_Ne3 = h['logrO4_Ne3'][:]
lrNe3_Ne2 = h['logrNe3_Ne2'][:]

plt.figure('MIR_BPT_combined')

xnew = np.arange(-2.5,0., 0.1)
m = 1.3
ynew = m*xnew +3.0
plt.plot(xnew, ynew, '-', linewidth='4',color='red')

scatter(lrO4_Ne3,lrNe3_Ne2,marker='.',s=1,linewidths=0,color='grey',alpha=0.5)


####Selecciona trozos de datos#################################
#with h5py.File('combined_models_MIR.hdf5', 'r') as f:
#	d1 = f['lrO4_Ne3']
#	d2 = f['lrNe3_Ne2']
#	data1 = []
#	data2 = []
#	for i in range(0,100):
#	    if d1[i]<-0.3 and d1[i]>-1.0:
#	        data1.append(d1[i])
#	        data2.append(d2[i])
#
#print(len(data1))
#print(len(data2))
#scatter(data1,data2,marker='.',s=2,linewidths=0,c='b',alpha=0.3)
##################################################################

plt.xlabel(r"log([O IV]25.9um/[Ne III]15.6um)", fontsize=14)
plt.ylabel(r"log([Ne III]15.6um/[Ne II]12.8um)", fontsize=14)

plt.title('SFR', fontsize=14)
text(0.05,0.2,'BAT-AGNs', fontsize=14)
text(-1.3,1.,'Starburst', fontsize=18, color='black')
text(-0.4,-0.2,'LINERs', fontsize=14)
text(-0.5,-0.5,'HII region', fontsize=14)
text(-0.5,-0.7,'galaxies', fontsize=14)
plt.xlim(-2.5,0.5)
plt.ylim(-2.5,6)

y0=(-2,2)
x0=(0,0)
y1=(0,0)
x1=(-2,2)
plt.plot(x0,y0,'k:')
plt.plot(x1,y1,'k:')
plt.grid(True)
plt.show()
plt.savefig('combined_efrac_y12.png',dpi=100)
