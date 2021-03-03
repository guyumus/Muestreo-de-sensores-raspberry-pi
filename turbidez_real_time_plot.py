# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:38:37 2021

@author: Estudiante
"""

# Importamos Adafruit_ADSx15 para permitir que nuestro proyecto 
# se comunique con nuestro módulo
import Adafruit_ADS1x15
# Se importa count para realizar el conteo para el jeustreo y para graficar
# el tiempo en el eje x
from itertools import count
# Se importa Matplotlib para realizar la gráfica en tiempo real de los sensores
# esto se logra con FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Se crea un objeto para almacenar la conexión con nuestro módulo
adc = Adafruit_ADS1x15.ADS1115()

# Se escoge un valor de ganancia para elegir el valor máximo
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# En este caso se elige 1
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)


x_vals = []
y_vals = []

index = count()

def animate(i):

    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).    
    
    x_vals.append(next(index))
    y_vals.append('{0:>6}'.format(*values))
    plt.cla()
    plt.plot(x_vals,y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

