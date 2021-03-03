# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:35:38 2021

@author: Estudiante
"""
# Importamos w1thermsensor para permitir que nuestro código
# se comunique con el sensor.
from w1thermsensor import W1ThermSensor
# Se importa count para realizar el conteo para el meustreo y para graficar
# el tiempo en el eje x
from itertools import count
# Se importa Matplotlib para realizar la gráfica en tiempo real de los sensores
# esto se logra con FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Se crea un objeto para almacenar una conexión con el sensor.
sensor = W1ThermSensor()

# Se crean dos variables vacias las cuales irán almacenando el valor del sensor
x_vals = []
y_vals = []

# Se almacena el conteo en la variable index para posteriormente graficar el
# tiempo en el eje x
index = count()

def animate(i):
    # Se toma el valor de salida del sensor y se almacena en la variable temperature
    temperature = sensor.get_temperature()
    # Se indexa tanto el valor de tiempo como de temperatura
    x_vals.append(next(index))
    y_vals.append(temperature)
    # Se imprime el valor de temperatura en la consola
    print("The temperature is %s celsius" % temperature)
    # Se borran los datos graficados para que al recibir un nuevo dato, este
    # no cambie el color de la gráfica en tiempo real
    plt.cla()
    # se grafican los datos
    plt.plot(x_vals,y_vals)
    
# con FuncAnimation se logra realizar la gráfica en tiempo real. Debido al 
# intervalo establecido (1 segundo), no es necesario usar un while loop para
# el muestreo, pues, a medida que se vaya actualizando la gráfica, también lo
# hará el valor de temperatura cuando se llame a la función "animate"    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

