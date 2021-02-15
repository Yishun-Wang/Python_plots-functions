from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# 1.5 J 

# link_level_schedule_length = {10: 7.6, 2: 8.02, 3: 9.4, 4: 10.62, 5: 11.42, 6: 12.56, 7: 13.48, 8: 14.36, 9: 15.32, 10: 16.72, 11: 17.26, 12: 17.92, 13: 19.32, 14: 20.36, 15: 20.5}




# link_level_co_length = {1: 0.0, 2: 1.24, 3: 2.8, 4: 3.52, 5: 4.72, 6: 5.96, 7: 6.82, 8: 7.96, 9: 9.02, 10: 10.08, 11: 11.16, 12: 12.18, 13: 12.54, 14: 14.06, 15: 15.02}

# link_level_energy_length= {1: 0.0, 2: 5.2, 3: 6.16, 4: 6.42, 5: 6.14, 6: 6.44, 7: 6.36, 8: 6.2, 9: 6.12, 10: 6.48, 11: 6.02, 12: 5.72, 13: 6.02, 14: 6.24, 15: 5.42}


# link_level_data_length = {1: 7.6, 2: 1.58, 3: 0.44, 4: 0.68, 5: 0.56, 6: 0.16, 7: 0.3, 8: 0.2, 9: 0.18, 10: 0.16, 11: 0.08, 12: 0.02, 13: 0.76, 14: 0.06, 15: 0.06}

# max_dic = {1: 10.0, 2: 11.0, 3: 12.0, 4: 13.0, 5: 14.0, 6: 15.0, 7: 16.0, 8: 17.0, 9: 18.0, 10: 19.0, 11: 20.0, 12: 21.0, 13: 22.0, 14: 23.0, 15: 24.0}

# min_dic = {1: 3.0, 2: 4.0, 3: 4.0, 4: 6.0, 5: 7.0, 6: 8.0, 7: 9.0, 8: 10.0, 9: 10.0, 10: 12.0, 11: 13.0, 12: 14.0, 13: 14.0, 14: 16.0, 15: 16.0}
link_level_schedule_length ={}
link_level_co_length ={}
link_level_data_length = {}
link_level_energy_length={}
max_dic = {}
min_dic ={}
# for i in range(10,220,10):
# 	link_level_schedule_length[i]=0








for i in range(50,100,20):
	lines = []#Declare an empty list named "lines"
	with open ('100LPAAnpower_500-1000energy_t5.0gamma100_50_eh_'+str(i)+'_size=80.0_link=100_110'+'.txt', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
		for line in in_file: #For each line of text store in a string variable named "line", and
			lines.append(line)
	a=lines[9]
	b=lines[10]
	c=lines[11]
	# d=lines[11]
	e=lines[14]
	co=lines[13]
	link_level_schedule_length[i] = float(a[21:27])
	max_dic[i] =float(b[19:22])
	min_dic[i] =float(c[19:22])
	link_level_co_length[i]=float(co[24:30])
	link_level_energy_length[i]=float(e[26:31])
	# amax_dic[i] = float(b[14:19])
	# amin_dic[i]=float(c[14:19])# amax_dic[i]=#add that line to our list of lines.
	# a_d_schedule[i]=float(d[29:34])
	# a_e_schedule[i]=float(e[31:36])
	# a_co_schedule[i]=float(co[27:32])


for i in range(110,210,20):
	lines = []#Declare an empty list named "lines"
	with open ('100LPAAnpower_500-1000energy_t5.0gamma100_50_eh_'+str(i)+'_size=80.0_link=100_110'+'.txt', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
		for line in in_file: #For each line of text store in a string variable named "line", and
			lines.append(line)
	a=lines[9]
	b=lines[10]
	c=lines[11]
	# d=lines[11]
	e=lines[14]
	co=lines[13]
	link_level_schedule_length[i] = float(a[21:27])
	max_dic[i] =float(b[19:22])
	min_dic[i] =float(c[19:22])
	link_level_co_length[i]=float(co[24:30])
	link_level_energy_length[i]=float(e[26:31])


link_level_schedule_length[100]= 126.80
link_level_co_length[100] = 100.0
link_level_energy_length[100] = 26.80
max_dic[100] = 129.0
min_dic[100] = 124.0
















schedule_figure = plt.figure(345)

NoL= range(50,210,20)
s_link_level_schedule_length = []
s_link_level_co_length = []
s_link_level_energy_length = []

# s_link_level_data_length = []
s_max_dic = []
s_min_dic = []
for i in NoL:
	s_link_level_schedule_length.append(link_level_schedule_length[i])
	s_link_level_co_length.append(link_level_co_length[i])
	s_link_level_energy_length.append(link_level_energy_length[i])
	# s_link_level_data_length.append(link_level_data_length[i])
	s_max_dic.append(round(max_dic[i]))
	s_min_dic.append(round(min_dic[i]))
yl =[]
yu= []


for j in range(0,8):
	print(j)
	print(s_max_dic[j])
	print(s_link_level_schedule_length[j])
	yu.append(s_max_dic[j]-s_link_level_schedule_length[j])
	yl.append(s_link_level_schedule_length[j]- s_min_dic[j])




x = np.arange(50,210,20)
y = s_link_level_schedule_length
y1=np.arange(0,140,10)
# example variable error bar values
yerr_lower= s_min_dic
yerr_upper = s_max_dic
width = 1.5
stacked = []
for k in range(0,8):
	stacked.append(s_link_level_energy_length[k] )
# First illustrate basic pyplot interface, using defaults where possible.
plt.figure(234)
p0 =plt.errorbar(x, y, yerr=[yl,yu],capsize=6, capthick=2,ecolor='black',fmt='-o',color='black')
p1 = plt.bar(x, s_link_level_co_length,bottom=stacked,color='white',edgecolor="black",linewidth ="1",width = 10)
# p2= plt.bar(x,s_link_level_data_length,bottom=s_link_level_energy_length,color="grey",edgecolor= "black")
p3= plt.bar(x,s_link_level_energy_length,hatch="//",fc='None',edgecolor='black',width = 10)
plt.xticks(NoL)
plt.xlabel('Number of EH nodes')
# plt.title("Link schedule propotion with 1.5 Joules energy requirement ")
plt.ylabel('Number of time slots')
plt.legend((p0,p1, p3), ('schedule length','mixed timeslot','energy timeslot'))
plt.yticks(y1)
# plt.grid()
plt.show()
# lco= []
# for i in range(1,16):
# 	le.append(link_level_co_length[i]/link_level_schedule_length[i])
