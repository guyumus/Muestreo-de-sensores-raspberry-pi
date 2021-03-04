# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:38:37 2021

@author: Estudiante
"""
# importamos "time" para controlar la frecuencia con la que se recopilan los 
# datos del sensor e importamos Adafruit_ADS1x15 para permitir que nuestro proyecto
# se comunique con nuestro módulo
import time
import Adafruit_ADS1x15

# Se crea un objeto para almacenar la conexión con nuestro módulo
adc = Adafruit_ADS1x15.ADS1115()

# Se escoge un valor de ganancia para elegir el valor máximo d3e referencia en el ADC
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# En este caso se elige 1
GAIN = 1

print('leyendo los valores del ADS1x15, presiona Ctrl-C para detener...')

while True:
    # Se leen los 4 valores del ADC
    values = [0]*4
    for i in range(4):
        # Se guardan los 4 canales del ADC
        values[i] = adc.read_adc(i, gain=GAIN)
    # Se imprime el valor del canal 0
    print('| {0:>6} |'.format(*values))
    # Se espera medio segundo para tomar el siguiente dato
    time.sleep(0.5)

