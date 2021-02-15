from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 2.9 J 

link_level_schedule_length = {1: 14.16, 2: 15.0, 3: 15.5, 4: 16.54, 5: 18.58, 6: 19.0, 7: 19.82, 8: 21.8, 9: 21.92, 10: 22.76, 11: 23.3, 12: 24.3, 13: 25.52, 14: 26.32, 15: 27.62}



link_level_co_length = {1: 0.0, 2: 1.48, 3: 2.6, 4: 4.14, 5: 4.92, 6: 5.68, 7: 7.18, 8: 8.56, 9: 9.24, 10: 10.28, 11: 11.22, 12: 12.08, 13: 13.06, 14: 14.2, 15: 15.04}

link_level_energy_length= {1: 0.0, 2: 11.64, 3: 12.02, 4: 12.08, 5: 12.84, 6: 12.0, 7: 12.36, 8: 13.22, 9: 12.64, 10: 12.36, 11: 12.04, 12: 12.14, 13: 12.44, 14: 12.08, 15: 12.5}


link_level_data_length = {1: 14.16, 2: 1.88, 3: 0.88, 4: 0.32, 5: 0.82, 6: 1.32, 7: 0.28, 8: 0.02, 9: 0.04, 10: 0.12, 11: 0.04, 12: 0.08, 13: 0.02, 14: 0.04, 15: 0.08}

max_dic = {1: 20.0, 2: 20.0, 3: 22.0, 4: 22.0, 5: 23.0, 6: 24.0, 7: 25.0, 8: 26.0, 9: 27.0, 10: 29.0, 11: 29.0, 12: 30.0, 13: 31.0, 14: 32.0, 15: 33.0}

min_dic = {1: 5.0, 2: 7.0, 3: 8.0, 4: 9.0, 5: 11.0, 6: 11.0, 7: 10.0, 8: 13.0, 9: 15.0, 10: 13.0, 11: 15.0, 12: 15.0, 13: 17.0, 14: 19.0, 15: 19.0}



schedule_figure = plt.figure(10)

NoL= range(1,16,1)
s_link_level_schedule_length = []
s_link_level_co_length = []
s_link_level_energy_length = []

s_link_level_data_length = []
s_max_dic = []
s_min_dic = []
for i in NoL:
	s_link_level_schedule_length.append(link_level_schedule_length[i])
	s_link_level_co_length.append(link_level_co_length[i])
	s_link_level_energy_length.append(link_level_energy_length[i])
	s_link_level_data_length.append(link_level_data_length[i])
	s_max_dic.append(round(max_dic[i]))
	s_min_dic.append(round(min_dic[i]))
yl =[]
yu= []


for j in range(0,15):
	print(j)
	print(s_max_dic[j])
	print(s_link_level_schedule_length[j])
	yu.append(s_max_dic[j]-s_link_level_schedule_length[j])
	yl.append(s_link_level_schedule_length[j]- s_min_dic[j])




x = np.arange(1,16,1)
y = s_link_level_schedule_length

# example variable error bar values
yerr_lower= s_min_dic
yerr_upper = s_max_dic
width = 0.7
stacked = []
for k in range(0,15):
	stacked.append(s_link_level_energy_length[k] +s_link_level_data_length[k])
# First illustrate basic pyplot interface, using defaults where possible.
plt.figure(3)
p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black',)
p1 = plt.bar(x, s_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1")
p2= plt.bar(x,s_link_level_data_length,bottom=s_link_level_energy_length,color="grey",edgecolor= "black")
p3= plt.bar(x,s_link_level_energy_length,hatch='//',color='None',edgecolor='black',lw =1)
plt.xticks(NoL)
plt.xlabel('Number of links')
# plt.title("Link schedule propotion with 2.9 Joules energy requirement ")
plt.ylabel('Number of time slots')
plt.legend((p0,p1, p2,p3), ('schedule length','mixed timeslot', 'data timeslot','energy timeslot'))
plt.show()
