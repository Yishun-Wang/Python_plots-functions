from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 0.1 J 

link_level_n_d = {1: 325.03583692126705, 2: 191.94771717457223, 3: 271.02186258873996, 4: 231.1468749014979, 5: 186.72694055546523, 6: 173.33882090867792, 7: 178.27543864209179, 8: 180.67641328627923, 9: 162.2983704849061, 10: 169.47005620011637, 11: 149.3789296810835, 12: 148.64726644977392, 13: 188.1428729008606, 14: 156.46544592193655, 15: 162.96920886483352}



link_level_n_e = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}

# link_level_energy_length= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}


link_level_n_co ={1: 0.0, 2: 6.068379953598958, 3: 10.671994247819669, 4: 6.0470490402779715, 5: 11.957722613862142, 6: 28.813239882561376, 7: 21.155134582105767, 8: 27.550263054228143, 9: 33.73259842032836, 10: 37.49694376460221, 11: 49.42591509069504, 12: 40.39535375634294, 13: 36.24191012379084, 14: 35.04179730193013, 15: 37.93049655649815}


link_level_n_d = {}

link_level_n_e = {}


link_level_n_co = {}

for i in range(50,100,20):
	lines = []#Declare an empty list named "lines"
	with open ('100LPAAnpower_500-1000energy_t5.0gamma100_50_eh_'+str(i)+'_size=80.0_link=100_110'+'.txt', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
		for line in in_file: #For each line of text store in a string variable named "line", and
			lines.append(line)
	# a=lines[9]
	# b=lines[10]
	c=lines[17]
	# d=lines[11]
	e=lines[15]
	# co=lines[12]
	link_level_n_e[i] = float(e[16:27])
	link_level_n_co[i]= float(c[13:24]) 
	# amax_dic[i] = float(b[14:19])







for i in range(110,210,20):
	lines = []#Declare an empty list named "lines"
	with open ('100LPAAnpower_500-1000energy_t5.0gamma100_50_eh_'+str(i)+'_size=80.0_link=100_110'+'.txt', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
		for line in in_file: #For each line of text store in a string variable named "line", and
			lines.append(line)
	# a=lines[9]
	# b=lines[10]
	c=lines[17]
	# d=lines[11]
	e=lines[15]
	# co=lines[12]
	link_level_n_e[i] = float(e[16:27])
	link_level_n_co[i]= float(c[13:24]) 
	# min_dic[i] =float(c[19:22])
	# link_level_co_length[i]=100.0
	# link_level_energy_length[i]=float(e[26:31])


















schedule_figure = plt.figure(112)

NoL= range(50,210,20)
# n_link_level_schedule_length = []
n_link_level_co_length = []
n_link_level_energy_length = []
n_link_level_data_length = []

for i in NoL:
	n_link_level_co_length.append(link_level_n_co[i]/1000.0)
	n_link_level_energy_length.append(link_level_n_e[i]/1000.0)
	# n_link_level_data_length.append(link_level_n_d[i]/1000.0)

width = 0.05
stacked = []
x = np.arange(50,210,20)
x1=np.arange(43,200,3)
y=np.repeat(5.0, len(x1))
for k in range(0,8):
	stacked.append(n_link_level_energy_length[k] )

# p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black',)
p1 = plt.bar(x, n_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width=10)
# p2= plt.bar(x,n_link_level_data_length,bottom=n_link_level_energy_length,color="grey",edgecolor= "black",width=0.3)
p3= plt.bar(x,n_link_level_energy_length,hatch='//',fc='None',edgecolor='black',width=10)
p4=plt.plot(x1,y,linewidth=2.0,color ='black',linestyle='dashed')
plt.xticks(NoL)
plt.xlabel('Number of EH nodes')
# plt.title("EH node harvested energy propotion with 0.1 Joules ")
plt.ylabel('Hravested energy in Joules')
plt.legend((p1, p3,p4[0]), ('mixed timeslot', 'energy timeslot', 'Energy requirement'))
plt.show()