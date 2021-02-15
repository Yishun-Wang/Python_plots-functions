from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 1.5 J 

link_level_n_d =  {1: 4346.170703161924, 2: 426.7578892701518, 3: 210.68431790085785, 4: 25.89781849809029, 5: 125.63823791823121, 6: 260.29339978281996, 7: 26.67308129640989, 8: 1.7196967967441825, 9: 8.37718568357818, 10: 15.469152469761235, 11: 4.854962953742026, 12: 12.9982895672392, 13: 2.6725483338262785, 14: 10.341341460300187, 15: 6.722589408372425}


link_level_n_e= {1: 0.0, 2: 3122.5339271623047, 3: 3041.0235006984794, 4: 3320.8475770121545, 5: 3249.617232935805, 6: 2900.5273049003545, 7: 2879.65461640129, 8: 3400.8697536095383, 9: 2942.1737716859166, 10: 2801.0706625675525, 11: 3133.701972497347, 12: 2864.2072553946305, 13: 2910.937167629675, 14: 3175.0905758010867, 15: 3309.5617577050157}

# link_level_energy_length= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}


link_level_n_co ={1: 0.0, 2: 231.85782826135687, 3: 219.17801993770976, 4: 353.66448559913096, 5: 311.6330014384374, 6: 273.7853877584355, 7: 325.1462863497567, 8: 347.775809959443, 9: 344.7160286935577, 10: 320.2508813731409, 11: 376.8497707530367, 12: 312.77900298029806, 13: 301.0510873740233, 14: 353.5335207347733, 15: 329.3407217578855}
schedule_figure = plt.figure(114)

NoL= range(1,16,1)
# n_link_level_schedule_length = []
n_link_level_co_length = []
n_link_level_energy_length = []
n_link_level_data_length = []

for i in NoL:
	n_link_level_co_length.append(link_level_n_co[i]/1000.0)
	n_link_level_energy_length.append(link_level_n_e[i]/1000.0)
	n_link_level_data_length.append(link_level_n_d[i]/1000.0)

# width = 0.05
stacked = []
x = np.arange(1,16,1)
x1=np.arange(0.5,16,0.5)
y=np.repeat(2.9, len(x1))
for k in range(0,15):
	stacked.append(n_link_level_energy_length[k] +n_link_level_data_length[k])

# p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black',)
p1 = plt.bar(x, n_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width=0.7)
p2= plt.bar(x,n_link_level_data_length,bottom=n_link_level_energy_length,color="grey",edgecolor= "black",width=0.7)
p3= plt.bar(x,n_link_level_energy_length,hatch="//",fc='None',edgecolor='black',width=0.7)
p4,=plt.plot(x1,y,linewidth=2.0,color ='black',linestyle='dashed')
plt.xticks(NoL)
plt.xlabel('Number of links')
# plt.title("EH node harvested energy propotion with 2.9 Joules ")
plt.ylabel('Hravested energy in Joules')


plt.legend((p1[0], p2[0],p3[10],p4), ('mixed timeslot', 'data timeslot','energy timeslot', 'Energy requirement'),bbox_to_anchor=(0.44, 0.13), bbox_transform=plt.gcf().transFigure)
# plt.legend(bbox_to_anchor=(1, 0.5))
# plt.grid()
plt.show()