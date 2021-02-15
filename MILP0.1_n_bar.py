from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 0.1 J 

link_level_n_d = {1: 325.03583692126705, 2: 194.6021199514308, 3: 275.8443296707702, 4: 235.93067451803157, 5: 167.25033274080278, 6: 154.95265847899688, 7: 180.76722560759652, 8: 175.52008254387883, 9: 178.27303417655585, 10: 173.31897346749128, 11: 159.12264469495608, 12: 169.3452404577567, 13: 174.4127636689093, 14: 132.3075183540338, 15: 167.79769290474906}



link_level_n_e = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}

# link_level_energy_length= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}


link_level_n_co ={1: 0.0, 2: 0.05124078492601319, 3: 6.018182446917399, 4: 7.201791997358944, 5: 30.865981814925348, 6: 31.835909179378028, 7: 25.00349201721809, 8: 30.22671666391273, 9: 19.81520911197992, 10: 33.517957631276175, 11: 40.04319275342259, 12: 37.68245378328516, 13: 42.27467481220764, 14: 54.35694880188558, 15: 28.41271847670929}

schedule_figure = plt.figure(112)

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
y=np.repeat(0.1, len(x1))
for k in range(0,15):
	stacked.append(n_link_level_energy_length[k] +n_link_level_data_length[k])

# p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black',)
p1 = plt.bar(x, n_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width=0.7)
p2= plt.bar(x,n_link_level_data_length,bottom=n_link_level_energy_length,color="grey",edgecolor= "black",width=0.7)
p3= plt.bar(x,n_link_level_energy_length,hatch="/",fc='None',edgecolor='black',width=0.35)
p4,=plt.plot(x1,y,linewidth=2.0,color ='black',linestyle='dashed')
plt.xticks(NoL)
plt.xlabel('Number of links')
# plt.title("EH node harvested energy propotion with 0.1 Joules energy requirement")
plt.ylabel('Hravested energy in Joules')
plt.legend((p1[0], p2[0],p4), ('mixed timeslot', 'data timeslot', 'Energy requirement'))
plt.show()
ll=[]
for i in range(1,16):
	print(i)
	n= (link_level_n_d[i]+link_level_n_co[i])
	ll.append(link_level_n_d[i]/float(n))