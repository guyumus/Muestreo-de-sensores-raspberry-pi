# Importamos RPI.GPIO para permitir que nuestro código se comunique con el sensor.
import RPi.GPIO as GPIO
# Se importa time para poder estimar el tiempo de diferencia entre el momento
# en que se envió la señal y cuando el sensor la recibió
import time
 
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
    # que la señal va de ida y vuelta para calcular la distancia
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            # Se toma el valor de salida del sensor y se almacena en la variable dist
            dist = distance()
            # Se imprime el valor de distancia en la consola
            print ("Distancia medida = %.1f cm" % dist)
            time.sleep(1)
 
        # Si se presiona ctrl+c se para el programa
    except KeyboardInterrupt:
        print("Medida detenida por el ususario")
        GPIO.cleanup()
