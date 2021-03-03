# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:56:27 2021

@author: Estudiante
"""

# Importamos RPI.GPIO para permitir que nuestro código
# se comunique con el sensor.
import RPi.GPIO as GPIO
# Se importa time para poder estimar el tiempo de diferencia de entre el momento
# en que se envió la señal y cuando el sensor la recibió
import time
# Se importa count para realizar el conteo para el jeustreo y para graficar
# el tiempo en el eje x
from itertools import count
# Se importa Matplotlib para realizar la gráfica en tiempo real de los sensores
# esto se logra con FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# Se configuran los pines
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#Se configura la dirección del TRIGGER y del ECHO (entrada o salida)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Se crean dos variables vacias las cuales irán almacenando el valor del sensor
x_vals = []
y_vals = []

# Se almacena el conteo en la variable index para posteriormente graficar el
# tiempo en el eje x
index = count()

def distance():
    # Se pone el TRIGGER en alto
    GPIO.output(GPIO_TRIGGER, True)
 
    # Se pone el TRIGGER en bajo después de 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # Se guarda el tiempo de inicio
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # Se guarda el tiempo de llegada de la señal
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # Se calcula el tiempo de diferencia de la salida y llegada de la señal
    TimeElapsed = StopTime - StartTime
    # Se multiplica por la velocidad del sonido y se divide entre dos devido a
    # que la señal va de ida y vuelta
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def animate(i):
    # Se toma el valor de salida del sensor y se almacena en la variable dist
    dist = distance()
    # Se indexa tanto el valor de tiempo como de distancia
    x_vals.append(next(index))
    y_vals.append(dist)
    # Se imprime el valor de temperatura en la consola
    print ("Measured Distance = %.1f cm" % dist)
    # Se borran los datos graficados para que al recibir un nuevo dato, este
    # no cambie el color de la gráfica en tiempo real
    plt.cla()
    # se grafican los datos
    plt.plot(x_vals,y_vals)

# con FuncAnimation se logra realizar la gráfica en tiempo real. Debido al 
# intervalo establecido (1 segundo), no es necesario usar un while loop para
# el muestreo, pues, a medida que se vaya actualizando la gráfica, también lo
# hará el valor de distancia cuando se llame a la función "animate"    

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()