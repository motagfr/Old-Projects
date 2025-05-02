import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df=pd.read_csv('C:\\mobilePrice.csv')
x, y = np.meshgrid(np.arange(-20,20,.1), np.arange(-20,20,.1))
def f(x,y):
    return (x+np.sin(y))

len(x)
len(y)

z=f(x,y)
z

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z)
plt.show()
