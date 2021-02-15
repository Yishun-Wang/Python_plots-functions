import matplotlib.pyplot as plt
#MILP
# plt.rcParams['patch.edgecolor'] = 'white' 
# Pie chart
labels = ['energy-timeslot', 'mix-timeslot']
sizes = [27.74566473988439,   72.2543352601156]
#colors
colors = ['white','white',]
size1=[100]
lb=['LPAA']

fig = plt.figure(566)
explode=[0,0]
patterns= [ "/" , "\\" , "|" , "-" ]
fig1, ax1 = plt.subplots()
f=ax1.pie(sizes, colors = colors, labels=labels,explode=explode, autopct='%1.1f%%', startangle=90,wedgeprops=dict(edgecolor='black') )
plt.pie(size1,colors='white',radius=0.75,startangle=90,wedgeprops=dict(edgecolor='black'))

#draw circle
patches = f[0]
patches[0].set_hatch('/')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()

plt.show()