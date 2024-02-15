import  matplotlib.pyplot as plt
from FT.Forcetool import Forcetool



torques= []
forces,angles = [],[]
ft = Forcetool(m=2400)

x = []
y = []

for i in range(-60,70,10): 
    total_force = ft.latforce(west=False,push=False,theta=i)
    print(total_force)
    ff = ft.get_torque_factor(force=total_force,push=False)
    y.append( ((total_force * ff )))
    x.append(i)

plt.plot(x,y)
plt.show()