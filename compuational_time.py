from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas



LPAA= {1: 0.805716701052, 2: 1.79587408114, 3: 2.8520176617, 4: 3.86525113998, 5: 4.9131666054, 6: 5.8930330817, 7: 6.93891903838, 8: 8.02691154271, 9: 9.07922906541, 10: 10.2034665774, 11: 11.3626756407, 12: 12.4566312316, 13: 13.5435633282, 14: 14.7230868217, 15: 15.6430945927}
LPAAMAX_DIC = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16, 8: 17, 9: 18, 10: 19, 11: 20, 12: 21, 13: 22, 14: 23, 15: 24}
LPAAMin_DIC = {1: 3, 2: 4, 3: 4, 4: 6, 5: 7, 6: 8, 7: 9, 8: 11, 9: 10, 10: 12, 11: 13, 12: 14, 13: 14, 14: 16, 15: 16}

MILP = {1: 0.836446052755, 2: 1.11381462606, 3: 1.87629582075, 4: 2.48527048787, 5: 3.24855808164, 6: 4.12612195428, 7: 5.24788195797, 8:6.68768376868, 9: 8.4464285054, 10: 9.40793525142, 11: 11.2121077053, 12: 13.1315792992, 13: 17.6473151746, 14: 19.1350170908, 15: 23.5945470924}
milpMAX_DIC ={1: 10.0, 2: 11.0, 3: 12.0, 4: 13.0, 5: 14.0, 6: 15.0, 7: 16.0, 8: 17.0, 9: 18.0, 10: 19.0, 11: 20.0, 12: 21.0, 13: 22.0, 14: 23.0, 15: 24.0}
MILP_MIN_DIC = {1: 3.0, 2: 4.0, 3: 4.0, 4: 6.0, 5: 7.0, 6: 8.0, 7: 9.0, 8: 10.0, 9: 10.0, 10: 12.0, 11: 13.0, 12: 14.0, 13: 14.0, 14: 16.0, 15: 16.0}
NoL= range(1,16,1)
LPAA_link_level_schedule_length = []
MILP_link_level_schedule_length = []
lpamax= []
lpamin =[]
milmax =[ ]
milmin= []
for i in NoL:
	LPAA_link_level_schedule_length.append(LPAA[i])
	MILP_link_level_schedule_length.append(MILP[i])
	lpamax.append(LPAAMAX_DIC[i])
	lpamin.append(LPAAMin_DIC[i])
	milmax.append(milpMAX_DIC[i])
	milmin.append(MILP_MIN_DIC[i])

x = np.arange(1,16,1)
y = np.arange(0.5,24 ,2)
# y = ga_link_level_schedule_length
lu=[]
ll=[]
mu=[]
ml=[]
for j in range(0,15):
	print(j)
	lu.append(lpamax[j]-LPAA_link_level_schedule_length[j])
	ll.append(LPAA_link_level_schedule_length[j] +lpamin[j])
	mu.append(milmax[j]-MILP_link_level_schedule_length[j])
	ml.append(MILP_link_level_schedule_length[j]-milmin[j])



# example variable error bar values
# yerr_lower= s_min_dic
# yerr_upper = s_max_dic
width = 0.35 
stacked = []
# for k in range(0,15):
# 	stacked.append(s_link_level_energy_length[k] +s_link_level_data_length[k])
# First illustrate basic pyplot interface, using defaults where possible.
plt.figure(17)
p0 =plt.errorbar(x, LPAA_link_level_schedule_length, capsize=7, capthick=1,ecolor='black',fmt='--o',color='black',linewidth=2)

p1 = plt.errorbar(x, MILP_link_level_schedule_length,capsize=7, capthick=1,ecolor='black',fmt='--^',color='red',linewidth=2)
# p2 = plt.errorbar(x, gc_link_level_schedule_length,yerr=[gcyl,gcyu],capsize=7, capthick=1,ecolor='black',fmt='--*',color='blue',linewidth=2)

plt.xticks(NoL)
plt.yticks(y)
plt.xlabel('Number of links')
# plt.title("Link schedule length with two 1.5 Joules energy requirement EH nodes and 15 links ")
plt.ylabel('Computational time in seconds')
plt.legend((p0[0],p1[0]), ('LPAA', 'MILP'))
plt.grid()
plt.show()
