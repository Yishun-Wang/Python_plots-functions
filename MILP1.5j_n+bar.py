from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 1.5 J 

link_level_n_d = {1: 2337.252207550432, 2: 345.2846805731774, 3: 57.78394271338908, 4: 91.66346631469222, 5: 61.26605524385425, 6: 19.697027109429495, 7: 24.40604569559572, 8: 13.114098986803358, 9: 20.06231412897616, 10: 18.003389551911145, 11: 13.690021703463604, 12: 1.8088390590535268, 13: 89.00788298886779, 14: 11.964624791218945, 15: 6.085289675665963}


link_level_n_e = {1: 0.0, 2: 1400.9178737769462, 3: 1481.096627116087, 4: 1537.4099602618255, 5: 1404.229993396844, 6: 1528.563339224502, 7: 1437.4853890689349, 8: 1314.924985023216, 9: 1321.4948178585792, 10: 1351.9170197700435, 11: 1391.101137665058, 12: 1278.5170298579437, 13: 1312.4113600399207, 14: 1317.2225950672694, 15: 1313.5167216100267}

# link_level_energy_length= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}


link_level_n_co ={1: 0.0, 2: 221.78438170169522, 3: 279.70890346970026, 4: 230.75941044125514, 5: 284.2865203530604, 6: 263.7827322327203, 7: 274.0577174277689, 8: 273.8088421175123, 9: 290.21521875676086, 10: 256.8513070836754, 11: 293.2554069548232, 12: 316.0650236562262, 13: 268.1359466155733, 14: 290.7579131153406, 15: 327.9618836257086}
schedule_figure = plt.figure(113)

NoL= range(1,16,1)
# n_link_level_schedule_length = []
n_link_level_co_length = []
n_link_level_energy_length = []
n_link_level_data_length = []

for i in NoL:
	n_link_level_co_length.append(link_level_n_co[i]/1000.0)
	n_link_level_energy_length.append(link_level_n_e[i]/1000.0)
	n_link_level_data_length.append(link_level_n_d[i]/1000.0)

width = 0.05
stacked = []
x = np.arange(1,16,1)
x1=np.arange(0.5,16,0.5)
y=np.repeat(1.5, len(x1))
for k in range(0,15):
	stacked.append(n_link_level_energy_length[k] +n_link_level_data_length[k])

# p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black',)
p1 = plt.bar(x, n_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width=0.7)
p2= plt.bar(x,n_link_level_data_length,bottom=n_link_level_energy_length,color="grey",edgecolor= "black",width=0.7)
p3= plt.bar(x,n_link_level_energy_length,hatch="//",color='None',edgecolor='black',width=0.7)
p4,=plt.plot(x1,y,linewidth=2.0,color ='black',linestyle='dashed')
plt.xticks(NoL)
plt.xlabel('Number of links')
# plt.title("EH node harvested energy propotion with 1.5 Joules Energy requirement ")
plt.ylabel('Hravested energy in Joules')
plt.legend((p1, p2,p3,p4), ('mixed timeslot', 'data timeslot','energy timeslot', 'Energy requirement'))
plt.show()
lco= []
le=[]
for i in range(1,16):
	le.append(link_level_n_e[i]/(link_level_n_d[i]+link_level_n_e[i]+link_level_n_co[i]))
