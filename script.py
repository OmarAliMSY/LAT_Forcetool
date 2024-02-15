import  matplotlib.pyplot as plt
from FT.Forcetool import Forcetool
import numpy as np


torques= []
forces,angles = [],[]
ft = Forcetool(m=2400,west=False,push=True)
ft.y = 70
x = []
y = []


for i in range(-60,65,5): 
    total_force = ft.latforce(theta=i)
    print(total_force)
    
    ff = ft.get_torque_factor(force=total_force)
    y.append( (np.abs((total_force * ff ))))
    
    x.append(i)

plt.plot(x,y)
plt.show()