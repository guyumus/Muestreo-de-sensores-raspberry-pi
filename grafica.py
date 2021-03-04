# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:23:22 2021

@author: Jocko
"""

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np
import pandas as pd
import math

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

x_vals_2 = []
y_vals_2 = []

x_vals_3 = []
y_vals_3 = []

data = pd.read_excel("datos_Iot_presentacion.xlsx", sheet_name= 'temperatura')
data = data.to_numpy()

data_2 = pd.read_excel("datos_Iot_presentacion.xlsx", sheet_name= 'turbidez')
data_2 = data_2.to_numpy()

data_3 = pd.read_excel("datos_Iot_presentacion.xlsx", sheet_name= 'distancia')
data_3 = data_3.to_numpy()

plt.plot(x_vals, y_vals)

index = count()

def animate(i):
    
    x_vals.append(next(index))
    y_vals.append(data[next(index),1])
    
    x_vals_2.append(next(index))
    y_vals_2.append(data_2[next(index),1])

    x_vals_3.append(next(index))
    y_vals_3.append(data_3[next(index),1])    
    
    plt.cla()
    plt.plot(x_vals,y_vals, label = 'temperatura')
    plt.plot(x_vals_2,y_vals_2, label = 'turbidez')
    plt.plot(x_vals_3,y_vals_3, label = 'distancia')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()
    

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()