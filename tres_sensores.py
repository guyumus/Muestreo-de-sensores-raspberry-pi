# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:35:38 2021

@author: Estudiante
"""
# importamos "time" para controlar la frecuencia con la que se recopilan los 
# datos del sensor e importamos w1thermsensor y Adafruit para permitir que 
# nuestro proyecto se comunique con el módulo ADC y el sensor de temperatura.
import time
from w1thermsensor import W1ThermSensor
import Adafruit_ADS1x15

# Importamos RPI.GPIO para permitir que nuestro código
# se comunique con el sensor de ultrasonido.
import RPi.GPIO as GPIO

# Se crea un objeto para almacenar una conexión con el sensor de temperatura.
sensor = W1ThermSensor()

# Se crea un objeto para almacenar la conexión con nuestro módulo ADC
adc = Adafruit_ADS1x15.ADS1115()

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# Se configuran los pines
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#Se configura la dirección del TRIGGER y del ECHO (entrada o salida)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
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
    # Se multiplica por la velocidad del sonido y se divide entre dos debido a
    # que la señal va de ida y vuelta
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# Se escoge un valor de ganancia para elegir el valor máximo
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# En este caso se elige 1
GAIN = 1

# Se utiliza while True loop para ejecutar el código dentro de él para siempre.
while True:
        # Se obtiene el valor de temperatura y se almacena en temperature
        temperature = sensor.get_temperature()
        # Se imprime el valor de temperatura
        print("La temperatura es %s celsius" % temperature)
        # Se toma el valor de salida del sensor de ultrasonido y se almacena en la variable dist
        dist = distance()
        # Se imprime el valor de distancia en la consola
        print ("Distancia medida = %.1f cm" % dist)        
        # Se leen los 4 canales del ADC
        values = [0]*4
        for i in range(4):
            # Se guardan los 4 canales del ADC
            values[i] = adc.read_adc(i, gain=GAIN)
        # Se imprime el valor del canal 0
        print('| {0:>6} |'.format(*values))        
        # Se espera 1 segundo para tomar la siguiente muestra        
        time.sleep(1)
