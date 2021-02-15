from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

#   E_min = 1.5 J  \  Nol = 15. X- Variable = alpha  y-schedule = schedule length 


alpha=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
m_dic= {}
l_dic= {}
amin_dic ={}
a_d_schedule={}
a_e_schedule={}
a_co_schedule= {}
# for i in alpha:
# 	lines = []#Declare an empty list named "lines"
# 	with open ('alpha='+str(i)+'.txt', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
# 		for line in in_file: #For each line of text store in a string variable named "line", and
# 			lines.append(line)
# 	a=lines[10]
# 	b=lines[14]
# 	c=lines[15]
# 	d=lines[11]
# 	e=lines[13]
# 	co=lines[12]
# 	a_dic[i] = float(a[34:38])
# 	amax_dic[i] = float(b[14:19])
# 	amin_dic[i]=float(c[14:19])# amax_dic[i]=#add that line to our list of lines.
# 	a_d_schedule[i]=float(d[29:34])
# 	a_e_schedule[i]=float(e[31:36])
# 	a_co_schedule[i]=float(co[27:32])

# print(lines[10])       
m_dic= {0.1:52.74, 0.2:33.816326530612244, 0.3:27.16,0.4: 24.125, 0.5:21.382978723404257,\
0.6: 20.755102040816325, 0.7:19.78,0.8:19.083333333328145,0.9:18.306122448979593, 1.0:18.18} 
l_dic={0.1:52.96, 0.2:34.14, 0.3:27.3,0.4: 24.2, 0.5:22.12,\
0.6: 21.02, 0.7:20.02,0.8:19.32,0.9:18.3, 1.0:18.28}
m_max_dic = {0.1:69.0,0.2:41.0,0.3:33.0,0.4:28.0,0.5:25.0,0.6:24.0,0.7:22.0,0.8:21.0,0.9:20.0,1.0:20.0}
m_min_dic ={0.1:30.0,0.2:22.0,0.3:19.0,0.4:19.0,0.5:17.0,0.6:17.0,0.7:16.0,0.8:16.0,0.9:16.0, 1.0:16.0}
a_data_dic ={0.1:0.1, 0.2:0.0,0.3:0.06,0.4:0.10416666666666667,0.5:0.0851063829787234,\
0.6:0.4897959183673469,0.7:0.36,0.8:0.22916666666666666,0.9:0.7346938775510204,1.0:0.28}
a_co_dic ={0.1:15.0,0.2:15.16326530612245,0.3:15.08,0.4:14.9375,0.5:15.0,0.6:14.673469387755102,\
0.7:14.74,0.8:14.833333333333334,0.9:14.346938775510203,1.0:14.82}
a_energy_dic = {0.1:37.64, 0.2:18.653061224489797,0.3:12.02,0.4:9.083333333333334,0.5:6.297872340425532,\
0.6:5.591836734693878,0.7:4.68,0.8:4.020833333333333,0.9:3.2244897959183674,1.0:3.08}

schedule_figure = plt.figure(9)

# NoL= range(1,16,1)
m_link_level_schedule_length = []
l_link_level_co_length = []
a_link_level_energy_length = []
a_link_level_data_length = []
a_max_dic = []
a_min_dic = []
a_d =[]
a_co=[]
a_e=[]
for i in alpha:
	m_link_level_schedule_length.append(m_dic[i])
	a_max_dic.append(m_max_dic[i])
	a_min_dic.append(m_min_dic[i])
	a_d.append(a_data_dic[i])
	l_link_level_co_length.append(l_dic[i])
	a_co.append(a_co_dic[i])
	a_e.append(a_energy_dic[i])

ayl =[]
ayu= []


for j in range(0,10):
	ayu.append(a_max_dic[j]-m_link_level_schedule_length[j])
	ayl.append(m_link_level_schedule_length[j]- a_min_dic[j])




x = np.arange(0.1,1.1,0.1)
y = m_link_level_schedule_length
y1 = np.arange(17,75,5)
# example variable error bar values
# yerr_lower= a_min_dic
# yerr_upper = a_max_dic
width = 0.3 
stacked = []
for k in range(0,10):
	stacked.append(a_d[k] +a_e[k])
# First illustrate basic pyplot interface, using defaults where possible.
plt.figure(9)
p0=plt.bar(x,a_co,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width=0.05)
p1= plt.bar(x,a_d,bottom=a_e,color="grey",edgecolor= "black",width=0.05)
p2=plt.bar(x,a_e,hatch="//",color='None',edgecolor='black',width=0.05)
# p0 =plt.plot(x, y, capsize=6, capthick=2,ecolor='black',fmt='-o',color='black')
# p1 = plt.errorbar(x, l_link_level_co_length,capsize=6, capthick=2,ecolor='red',fmt='-*',color='red')
# p2= plt.bar(x,a_link_level_data_length,bottom=a_link_level_energy_length,color="grey",edgecolor= "black",width=0.05)
# p3= plt.bar(x,a_link_level_energy_length,hatch='\\',fc='None',edgecolor='black',width=0.05)
p3= plt.errorbar(x,y,yerr=[ayl,ayu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black')
plt.xticks(x)
plt.yticks(y1)
plt.xlabel('Conversion rate alpha')
# plt.title("Link schedule propotion with 1.0 Joules energy requirement  and 15 links")
plt.ylabel('Number of time slots')
plt.legend((p3,p0, p1,p2), ('schedule length','mixed timeslot', 'data timeslot','energy timeslot'))
# plt.grid()
plt.show()
