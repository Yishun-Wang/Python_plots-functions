import numpy as np
import itertools
# from gurobipy import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

##################################
yiwu_E_min = 1.5

yiwu_schedule = {1: 7.6, 2: 8.02, 3: 9.44, 4: 10.64, 5: 11.44, 6: 12.56, 7: 13.48, 8: 14.5, 9: 15.36, 10: 16.72, 11: 17.34, 12: 18.0, 13: 19.4, 14: 20.44, 15: 20.76}

#################################

yisi_E_min = 1.4
yisi_schedule = {1: 6.96, 2: 8.16, 3: 8.68, 4: 10.06, 5: 10.82, 6: 11.76,
                 7: 13.3, 8: 13.54, 9: 14.92, 10: 15.58, 11: 16.6, 12: 17.26, 13: 18.36, 14: 20.08, 15: 20.46}

################################
yisan_E_min = 1.3

yisan_schedule = {1: 6.22, 2: 7.28, 3: 8.74, 4: 10.06, 5: 10.86, 6: 11.18, 7: 12.24, 8: 13.58, 9: 14.66, 10: 15.04, 11: 16.28, 12: 17.66, 13: 18.6, 14: 19.24, 15: 20.32}

############################
yier_E_min = 1.2
yier_schedule = {1: 6.26, 2: 7.44, 3: 7.94, 4: 9.14, 5: 10.04, 6: 11.04, 7: 11.92,
                 8: 13.22, 9: 14.32, 10: 14.66, 11: 15.36, 12: 17.08, 13: 17.64, 14: 18.88, 15: 19.16}

#############################
yiyi_E_min = 1.1
yiyi_schedule ={1: 5.62, 2: 6.48, 3: 7.82, 4: 8.42, 5: 9.74, 6: 10.46, 7: 11.74, 8: 12.5, 9: 13.36, 10: 14.44, 11: 15.94, 12: 16.46, 13: 17.58, 14: 18.52, 15: 19.3}

#############################
yiling_E_min = 1.0
yiling_schedule = {1: 5.3, 2: 6.3, 3: 6.92, 4: 8.18, 5: 9.2, 6: 10.04, 7: 11.42,
                   8: 11.7, 9: 13.04, 10: 13.98, 11: 14.78, 12: 15.6, 13: 17.18, 14: 17.9, 15: 18.82}

############################
lingjiu_E_min = 0.9
lingjiu_schedule = {1: 4.74, 2: 5.82, 3: 6.62, 4: 7.38, 5: 8.24, 6: 9.66, 7: 10.54, 8: 11.84, 9: 12.5, 10: 13.66, 11: 14.34, 12: 15.62, 13: 16.6, 14: 17.44, 15: 18.54}

##################################
lingba_E_min = 0.8
lingba_schedule = {1: 4.42, 2: 5.24, 3: 6.16, 4: 7.0, 5: 8.38, 6: 9.18, 7: 10.04,
                   8: 10.9, 9: 12.36, 10: 13.14, 11: 14.28, 12: 14.88, 13: 15.84, 14: 16.9, 15: 17.88}

########################################
lingqi_E_min = 0.7
lingqi_schedule =  {1: 3.82, 2: 4.6, 3: 5.84, 4: 6.66, 5: 7.92, 6: 8.6, 7: 9.6, 8: 10.8, 9: 11.74, 10: 12.44, 11: 13.48, 12: 14.64, 13: 15.56, 14: 16.62, 15: 17.44}
##########################################
lingliu_E_min = 0.6
lingliu_schedule = {1: 3.36, 2: 4.08, 3: 5.58, 4: 6.18, 5: 7.34, 6: 8.22, 7: 9.1,
                    8: 10.18, 9: 11.08, 10: 12.2, 11: 13.2, 12: 13.88, 13: 14.96, 14: 16.04, 15: 16.92}

#########################################
ling_wu_E_min = 0.5
ling_wu_schedule = {1: 2.82, 2: 3.86, 3: 4.86, 4: 5.64, 5: 6.8, 6: 7.86, 7: 8.92, 8: 9.64, 9: 10.76, 10: 11.7, 11: 12.84, 12: 13.66, 13: 14.68, 14: 15.84, 15: 16.6}

###################################
ling_si_E_min = 0.4
ling_si_schedule = {1: 2.48, 2: 3.54, 3: 4.42, 4: 5.34, 5: 6.3, 6: 7.28, 7: 8.26, 8: 9.2,
                    9: 10.22, 10: 11.22, 11: 12.26, 12: 12.999999999837835, 13: 14.06, 14: 15.14, 15: 16.06}

###############################
ling_san_E_min = 0.3
ling_san_schedule = {1: 1.76, 2: 2.9, 3: 3.64, 4: 4.68, 5: 5.86, 6: 6.72, 7: 7.74, 8: 8.7, 9: 9.84, 10: 10.86, 11: 11.86, 12: 12.78, 13: 13.78, 14: 14.82, 15: 15.7}

################################
ling_er_E_min = 0.2
ling_er_schhedule = {1: 1.42, 2: 2.44, 3: 3.34, 4: 4.44, 5: 5.4, 6: 6.26, 7: 7.2, 8: 8.26,
                     9: 9.319999999902363, 10: 10.26, 11: 11.22, 12: 12.18, 13: 13.1, 14: 14.16, 15: 15.1}

###################################
ling_yi_E_min = 0.1
ling_yi_schedule = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0, 5: 5.0, 6: 6.0, 7: 7.0, 8: 8.0, 9: 9.0, 10: 10.0, 11: 11.0, 12: 12.0, 13: 13.0, 14: 14.0, 15: 15.0}


################################
erliu=2.6
erlius= {1: 11.5, 2: 13.06, 3: 14.46, 4: 15.32, 5: 15.76, 6: 17.24, 7: 17.96, 8: 19.12, 9: 20.0, 10: 20.38, 11: 22.04, 12: 23.12, 13: 24.4, 14: 25.04, 15: 26.52}

#########################
erwu = 2.5 
erwus = {1: 12.76, 2: 12.94, 3: 14.52, 4: 14.82, 5: 16.0, 6: 15.42, 7: 17.96, 8: 19.08, 9: 19.56, 10: 21.54, 11: 22.24, 12: 23.16, 13: 23.52, 14: 24.88, 15: 26.04}

###########################
ersi = 2.4 
ersis = {1: 12.3, 2: 13.06, 3: 13.46, 4: 14.26, 5: 16.0, 6: 16.52, 7: 17.98, 8: 18.14, 9: 18.92, 10: 20.24, 11: 21.06, 12: 21.84, 13: 23.68, 14: 24.52, 15: 24.64}

##############################
ersan = 2.3 
ersans ={1: 10.82, 2: 12.52, 3: 12.82, 4: 14.52, 5: 15.3, 6: 15.66, 7: 16.18, 8: 17.72, 9: 18.14, 10: 19.78, 11: 21.18, 12: 21.3, 13: 22.7, 14: 23.08, 15: 23.8}
##################################
erer= 2.2 
erers = {1: 10.6, 2: 11.38, 3: 12.72, 4: 13.34, 5: 13.96, 6: 15.68, 7: 16.12, 8: 17.58, 9: 18.08, 10: 19.38, 11: 20.5, 12: 21.56, 13: 22.1, 14: 22.86, 15: 24.38}

####################################
eryi=2.1
eryis =  {1: 10.06, 2: 11.58, 3: 11.84, 4: 13.14, 5: 14.28, 6: 15.28, 7: 16.48, 8: 16.64, 9: 18.18, 10: 19.04, 11: 20.34, 12: 20.72, 13: 21.36, 14: 22.98, 15: 23.78}
######################################
erling = 2.0 
erlings = {1: 9.6, 2: 10.46, 3: 10.82, 4: 12.94, 5: 14.08, 6: 15.24, 7: 15.44, 8: 16.34, 9: 17.3, 10: 18.62, 11: 19.52, 12: 19.78, 13: 20.94, 14: 22.88, 15: 23.12}
#########################################
yijiu= 1.9 
yijus = {1: 9.5, 2: 10.32, 3: 11.0, 4: 12.04, 5: 13.22, 6: 14.04, 7: 15.1, 8: 15.98, 9: 16.48, 10: 18.04, 11: 19.26, 12: 19.7, 13: 21.34, 14: 22.28, 15: 22.42}

#########################################
yiba = 1.8 
yibas = {1: 8.8, 2: 9.62, 3: 10.84, 4: 11.48, 5: 12.18, 6: 13.82, 7: 14.44, 8: 15.7, 9: 16.34, 10: 17.58, 11: 18.62, 12: 19.76, 13: 20.26, 14: 21.06, 15: 22.46}
###########################################
yiqi =1.7 
yiqis=  {1: 8.4, 2: 9.36, 3: 10.6, 4: 11.36, 5: 12.76, 6: 13.14, 7: 13.7, 8: 15.38, 9: 15.9, 10: 17.16, 11: 18.0, 12: 19.08, 13: 20.32, 14: 20.76, 15: 22.14}
###########################################
yiliu =1.6 
yilius = {1: 7.78, 2: 8.72, 3: 9.18, 4: 11.02, 5: 12.2, 6: 13.32, 7: 13.58, 8: 14.5, 9: 15.52, 10: 16.7, 11: 17.76, 12: 18.16, 13: 19.2, 14: 20.92, 15: 21.42}

##################################################

erqi = 2.7 
erqis = {1: 13.9, 2: 14.62, 3: 15.6, 4: 16.8, 5: 17.08, 6: 17.14, 7: 19.36, 8: 20.5, 9: 20.9, 10: 22.32, 11: 23.1, 12: 22.9, 13: 24.88, 14: 26.14, 15: 26.86}

######################
erjiu = 2.9 
erjius= {1: 14.16, 2: 15.0, 3: 15.5, 4: 16.58, 5: 18.64, 6: 19.0, 7: 19.86, 8: 21.96, 9: 22.04, 10: 22.88, 11: 23.34, 12: 24.44, 13: 25.7, 14: 26.36, 15: 27.76}

################################




E_min = np.arange(0.1, 3.0, 0.2)
E_min_n = []
for i in E_min:
    E_min_n.append(round(i, 3))


NoL = np.arange(1, 16, 1)

function_list = tuplelist(itertools.product(E_min_n, NoL))

N_E_dic = {}


for e in E_min_n:
    if e == yiwu_E_min:
        for k in yiwu_schedule:
            N_E_dic[(e, k)] = yiwu_schedule[k]
    elif e == yisi_E_min:
        for k in yisi_schedule:
            N_E_dic[(e, k)] = yisi_schedule[k]
    elif e == yisan_E_min:
        for k in yisan_schedule:
            N_E_dic[(e, k)] = yisan_schedule[k]
    elif e == yier_E_min:
        for k in yier_schedule:
            N_E_dic[(e, k)] = yier_schedule[k]
    elif e == yiyi_E_min:
        for k in yiyi_schedule:
            N_E_dic[(e, k)] = yiyi_schedule[k]

    elif e == yiling_E_min:
        for k in yiling_schedule:
            N_E_dic[(e, k)] = yiling_schedule[k]
    elif e == lingjiu_E_min:
        for k in lingjiu_schedule:
            N_E_dic[(e, k)] = lingjiu_schedule[k]
    elif e == lingba_E_min:
        for k in lingba_schedule:
            N_E_dic[(e, k)] = lingba_schedule[k]
    elif e == lingqi_E_min:
        for k in lingqi_schedule:
            N_E_dic[(e, k)] = lingqi_schedule[k]
    elif e == lingliu_E_min:
        for k in lingliu_schedule:
            N_E_dic[(e, k)] = lingliu_schedule[k]
    elif e == ling_wu_E_min:
        for k in ling_wu_schedule:
            N_E_dic[(e, k)] = ling_wu_schedule[k]
    elif e == ling_si_E_min:
        for k in ling_si_schedule:
            N_E_dic[(e, k)] = ling_si_schedule[k]
    elif e == ling_san_E_min:
        for k in ling_san_schedule:
            N_E_dic[(e, k)] = ling_san_schedule[k]
    elif e == ling_er_E_min:
        for k in ling_er_schhedule:
            for k in ling_er_schhedule:
                N_E_dic[(e, k)] = ling_er_schhedule[k]
    elif e == ling_yi_E_min:
        for k in ling_yi_schedule:
            N_E_dic[(e, k)] = ling_yi_schedule[k]
    elif e == erliu:
        for k in erlius:
            N_E_dic[(e,k)] = erlius[k]
    elif e == erwu:
        for k in erwus:
            N_E_dic[(e,k)] =erwus[k]
    elif e == ersi:
        for k in ersis:
            N_E_dic[(e,k)] = ersis[k]
    elif e == ersan:
        for k in ersans:
            N_E_dic[(e,k)] =ersans[k]
    elif e ==erer:
        for k in erers:
            N_E_dic[(e,k)]=erers[k]
    elif e == eryi:
        for k in eryis:
            N_E_dic[(e,k)]=eryis[k]
    elif e == erling:
        for k in erlings:
            N_E_dic[(e,k)] = erlings[k]

    elif e == yijiu:
        for k in yijus:
            N_E_dic[(e,k)]=yijus[k]
    elif e == yiba:
        for k in yibas:
            N_E_dic[(e,k)] = yibas[k]
    elif e == yiqi:
        for k in yiqis:
            N_E_dic[(e,k)] = yiqis[k]
    elif e == yiliu:
        for k in yilius:
            N_E_dic[(e,k)] = yilius[k]
    elif e == erqi:
        for k in erqis:
            N_E_dic[(e,k)] =erqis[k]
    elif e ==erjiu:
        for k in erjius:
            N_E_dic[(e,k)] =erjius[k]




fig = plt.figure()
ax = plt.axes(projection='3d')


# y = np.arange(1, 16, 1)
# x = np.arange(0.1, 1.6, 0.1)
# for i in range(len(x)):
#     x[i] = round(x[i],2)

ax.set_xticks(NoL, minor=False)
ax.set_yticks(E_min_n, minor=False)
Z = []


N, E = np.meshgrid(NoL, E_min_n)


L = []
for i in NoL:
    l = []
    for ee in E_min_n:
        l.append(N_E_dic[(ee, i)])
    L.append(l)

L_try = np.array(L)
# for yy in NoL:
#   for xx in E_min_n:
#       Z.append(N_E_dic[(xx,yy)])
# colors = cm.viridis(L_try)
# for i in N:
#     i= np.array(i)
#     for j in E:
#         j=np.array(j)
#         for h in L_try:
#             h=np.array(h)
#             ax.plot_surface(i,j,h, color='red',edgecolor='black', linewidth=1.0)





ax.plot_surface(N, E, L_try, color= 'White',edgecolor='black', linewidth=1.0)
ax.scatter(N, E, L_try, color='white', s=50,
           marker='o', alpha=1.0, edgecolors='black',linewidth=2.0)

ax.set_xlabel('Number of Links')
ax.set_ylabel('Energy Requirement in Joules')
ax.set_zlabel('Schedule Length')
ax.set_title('LPAA results')


plt.show()
