from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 0.1 J 

link_level_schedule_length = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0, 5: 5.0, 6: 6.0, 7: 7.0, 8: 8.0, 9: 9.0, 10: 10.0, 11: 11.0, 12: 12.0, 13: 13.0, 14: 14.0, 15: 15.0}




link_level_co_length = {1: 0.0, 2: 0.02, 3: 0.14, 4: 0.22, 5: 0.74, 6: 1.18, 7: 1.1, 8: 1.4, 9: 1.58, 10: 2.0, 11: 2.8, 12: 1.72, 13: 2.1, 14: 3.6, 15: 2.76}

link_level_energy_length= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}


link_level_data_length = {1: 1.0, 2: 1.98, 3: 2.86, 4: 3.78, 5: 4.26, 6: 4.82, 7: 5.9, 8: 6.6, 9: 7.42, 10: 8.0, 11: 8.2, 12: 10.28, 13: 10.9, 14: 10.4, 15: 12.24}

max_dic = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0, 5: 5.0, 6: 6.0, 7: 7.0, 8: 8.0, 9: 9.0, 10: 10.0, 11: 11.0, 12: 12.0, 13: 13.0, 14: 14.0, 15: 15.0}

min_dic = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0, 5: 5.0, 6: 6.0, 7: 7.0, 8: 8.0, 9: 9.0, 10: 10.0, 11: 11.0, 12: 12.0, 13: 13.0, 14: 14.0, 15: 15.0}



schedule_figure = plt.figure(9)

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
width = 0.35 
stacked = []
for k in range(0,15):
	stacked.append(s_link_level_energy_length[k] +s_link_level_data_length[k])
# First illustrate basic pyplot interface, using defaults where possible.
plt.figure(3)
p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black')
p1 = plt.bar(x, s_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width = 0.7)
p2= plt.bar(x,s_link_level_data_length,bottom=s_link_level_energy_length,color="grey",edgecolor= "black",width = 0.7)
# p3= plt.bar(x,s_link_level_energy_length,hatch="/",fc='None',edgecolor='black')
plt.xticks(NoL)
plt.yticks(y)
plt.xlabel('Number of links')
# plt.title("Link schedule propotion with 0.1 Joules Energy Requirement ")
plt.ylabel('Number of time Slots')
plt.legend((p0,p1, p2), ('schedule length','mixed timeslot', 'data timeslot'))
plt.show()

