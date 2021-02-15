# from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import num2date, date2num
import numpy as np
import matplotlib.dates
import pandas

# E=1.0j alpha= 0.85 nol 

g1_link_level_schedule_length = {1: 5.62, 2: 6.48, 3: 7.82, 4: 8.4, 5: 9.68, 6: 10.44, 7: 11.66, 8: 12.34, 9: 13.24, 10: 14.28, 11: 15.76, 12: 16.36, 13: 17.34, 14: 18.34, 15: 19.04}
g1_max_dic = {1: 8.0, 2: 9.0, 3: 10.0, 4: 11.0, 5: 12.0, 6: 13.0, 7: 14.0, 8: 15.0, 9: 15.0, 10: 17.0, 11: 18.0, 12: 18.0, 13: 20.0, 14: 21.0, 15: 21.0}
g1_min_dic = {1: 3.0, 2: 3.0, 3: 4.0, 4: 6.0, 5: 6.0, 6: 7.0, 7: 8.0, 8: 9.0, 9: 10.0, 10: 11.0, 11: 12.0, 12: 14.0, 13: 14.0, 14: 15.0, 15: 16.0}
g2_link_level_schedule_length = {1: 4.42, 2: 5.36, 3: 6.76, 4: 7.54, 5: 8.36, 6: 9.7, 7: 10.6, 8: 11.1, 9: 12.36, 10: 13.46, 11: 14.52, 12: 15.36, 13: 16.46, 14: 17.16, 15: 18.3}
g2_max_dic = {1: 8.0, 2: 9.0, 3: 10.0, 4: 11.0, 5: 12.0, 6: 13.0, 7: 14.0, 8: 15.0, 9: 16.0, 10: 17.0, 11: 17.0, 12: 18.0, 13: 19.0, 14: 20.0, 15: 21.0}
g2_min_dic = {1: 2.0, 2: 3.0, 3: 4.0, 4: 4.0, 5: 6.0, 6: 7.0, 7: 8.0, 8: 9.0, 9: 10.0, 10: 11.0, 11: 12.0, 12: 13.0, 13: 14.0, 14: 15.0, 15: 16.0}
g3_link_level_schedule_length = {1: 5.64, 2: 6.56, 3: 8.2, 4: 8.92, 5: 9.74, 6: 11.02, 7: 11.900000189812685, 8: 12.34, 9: 13.54, 10: 14.72, 11: 16.04, 12: 16.72, 13: 17.82, 14: 18.44, 15: 19.68}
g3_max_dic = {1: 10.0, 2: 11.0, 3: 12.0, 4: 13.0, 5: 14.0, 6: 15.0, 7: 16.0, 8: 17.0, 9: 18.0, 10: 19.0, 11: 20.0, 12: 20.0, 13: 22.0, 14: 23.0, 15: 24.0}
g3_min_dic = {1: 2.0, 2: 3.0, 3: 4.0, 4: 5.0, 5: 6.0, 6: 7.0, 7: 8.0, 8: 9.0, 9: 10.0, 10: 11.0, 11: 13.0, 12: 13.0, 13: 14.0, 14: 15.0, 15: 16.0}
g4_link_level_schedule_length ={1: 1.0, 2: 1.1200004548812514, 3: 1.180000814621866, 4: 1.260000827781046, 5: 1.320000112258575, 6: 1.5800004892348432, 7: 1.7199998625420412, 8: 1.7999998894061775, 9: 2.040000036067432, 10: 1.999999975360029, 11: 2.0199998952742186, 12: 2.059999961563586, 13: 2.1199999902002467, 14: 2.1199999516307937, 15: 2.1600001226889405}
g4_max_dic ={1: 1.0, 2: 2.0, 3: 2.0, 4: 2.0, 5: 1.999999995035293, 6: 2.0000000000167075, 7: 3.000001764186074, 8: 3.0000038223463577, 9: 4.000001118688761, 10: 3.0, 11: 4.0, 12: 3.999999984388508, 13: 3.9999999943922373, 14: 4.000000203177342, 15: 3.9999999893848077}
g4_min_dic ={1: 1.0, 2: 1.0, 3: 1.0, 4: 1.000000703927708, 5: 1.0, 6: 1.0000002781708526, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0000003864848876, 11: 1.0000002713926723, 12: 1.0000002844684337, 13: 1.9999965891885219, 14: 1.999999119419023, 15: 1.9999984483599145}
g5_link_level_schedule_length ={1: 5.0, 2: 5.88, 3: 6.720000093226875, 4: 6.900000017434454, 5: 7.1600002402933205, 6: 7.640000332749645, 7: 8.04000050429159, 8: 7.580000958110131, 9: 8.24000120988441, 10: 8.640001715585225, 11: 9.340001889987096, 12: 9.32000185781049, 13: 9.780002703961044, 14: 9.900002288183416, 15: 10.260001905114578}
g5_max_dic ={1: 9.0, 2: 10.0, 3: 11.0, 4: 11.000000111886724, 5: 12.0, 6: 12.000003407098301, 7: 12.000000280374106, 8: 13.0, 9: 13.000000146970242, 10: 13.000000321217533, 11: 15.0, 12: 15.000005307816119, 13: 15.000003502159855, 14: 16.000004725472195, 15: 17.000000059922314}
g5_min_dic ={1: 2.0, 2: 3.0, 3: 3.0, 4: 3.0, 5: 3.0, 6: 3.0000011212496984, 7: 3.0000006272538124, 8: 3.0000002532992953, 9: 4.0, 10: 4.000014510352101, 11: 5.000000112694402, 12: 4.000000821884765, 13: 5.999993303839297, 14: 6.00000018951165, 15: 6.000002796368238}


schedule_figure = plt.figure(9)

NoL= range(1,16,1)
ga_link_level_schedule_length = []
gb_link_level_schedule_length = []
gc_link_level_schedule_length = []
gd_link_level_schedule_length = []
ga_max_dic = []
ga_min_dic = []
gb_max_dic=[]
gb_min_dic=[]
gc_max_dic=[]
gc_min_dic=[]
gd_max_dic =[]
gd_min_dic = []
ge_link_level_schedule_length = []
ge_max_dic =[]
ge_min_dic = []
for i in NoL:
	ga_link_level_schedule_length.append(g1_link_level_schedule_length[i])
	gb_link_level_schedule_length.append(g2_link_level_schedule_length[i])
	gc_link_level_schedule_length.append(g3_link_level_schedule_length[i])
	gd_link_level_schedule_length.append(g4_link_level_schedule_length[i])
	ge_link_level_schedule_length.append(g5_link_level_schedule_length[i])
	ga_max_dic.append(g1_max_dic[i])
	ga_min_dic.append(g1_min_dic[i])
	gb_max_dic.append(g2_max_dic[i])
	gb_min_dic.append(g2_min_dic[i])
	gc_max_dic.append(g3_max_dic[i])
	gc_min_dic.append(g3_min_dic[i])
	gd_max_dic.append(g4_max_dic[i])
	gd_min_dic.append(g4_min_dic[i])
	ge_max_dic.append(g5_max_dic[i])
	ge_min_dic.append(g5_min_dic[i])


gayl =[]
gayu= []
gbyl=[]
gbyu=[]
gcyl=[]
gcyu=[]
gdyl =[]
gdyu =[]
geyl=[]
geyu=[]

for j in range(1,16):
	# print(j)
	# print(s_max_dic[j])
	# print(s_link_level_schedule_length[j])
	gayu.append(g1_max_dic[j]-g1_link_level_schedule_length[j])
	gayl.append(g1_link_level_schedule_length[j]- g1_min_dic[j])
	gbyl.append(g2_link_level_schedule_length[j]- g2_min_dic[j])
	gbyu.append(g2_max_dic[j]-g2_link_level_schedule_length[j])
	gcyl.append(g3_link_level_schedule_length[j]- g3_min_dic[j])
	gcyu.append(g3_max_dic[j]-g3_link_level_schedule_length[j])
	gdyl.append(g4_link_level_schedule_length[j]- g4_min_dic[j])
	gdyu.append(g4_max_dic[j]-g4_link_level_schedule_length[j])
	geyu.append(g5_max_dic[j]-g5_link_level_schedule_length[j])
	geyl.append(g5_link_level_schedule_length[j]-g5_min_dic[j])



x = np.arange(1,16,1)
y = ga_link_level_schedule_length
y1= np.arange(4,21,0.5)
# example variable error bar values
# yerr_lower= s_min_dic
# yerr_upper = s_max_dic
width = 0.35 
stacked = []
yax=[0,5,10,15,20]
# for k in range(0,15):
# 	stacked.append(s_link_level_energy_length[k] +s_link_level_data_length[k])
# First illustrate basic pyplot interface, using defaults where possible.
plt.figure(16)
# p0 =plt.errorbar(x, y, yerr=[gayl,gayu],capsize=7, capthick=1,ecolor='black',fmt='--o',markersize=18,color='black',linewidth=5)

# p1 = plt.errorbar(x, gb_link_level_schedule_length,yerr=[gbyl,gbyu],capsize=7, capthick=1,ecolor='black',fmt='--^',markersize=18, color='red',linewidth=5)
# p2 = plt.errorbar(x, gc_link_level_schedule_length,yerr=[gcyl,gcyu],capsize=7, capthick=1,ecolor='black',fmt='--*',markersize=18,color='blue',linewidth=5)
p3 = plt.errorbar(x,gd_link_level_schedule_length,yerr=[gdyl,gdyu], capsize=7, capthick=1,ecolor ='black',fmt='--v', markersize=18,color='green' ,linewidth=5)
p4=plt.errorbar(x,ge_link_level_schedule_length,yerr=[geyl,geyu],capsize=7, capthick=1,ecolor ='black',fmt='--H', markersize=18,color='purple' ,linewidth=5)
plt.xticks(NoL,fontsize=20)
plt.yticks(yax,fontsize=20)
plt.xlabel('Number of links',fontsize=20)
# plt.title("MILP Link schedule propotion with 0.1 Joules energy requirement and 15 links different SINR threshold")
plt.ylabel('Number of time slots',fontsize=20)
plt.legend((p3[0],p4[0]), ('no EHnode','one EHnode'), fontsize=18)
plt.grid()
plt.show()
l1=[]
for i in range(1,16):
	l1.append(g5_link_level_schedule_length[i]-g4_link_level_schedule_length[i])
