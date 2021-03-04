# importamos "time" para controlar la frecuencia con la que se recopilan los 
# datos del sensor e importamos w1thermsensor para permitir que nuestro proyecto 
# se comunique con el sensor.
import time
from w1thermsensor import W1ThermSensor

# Se crea un objeto para almacenar una conexión con el sensor.
sensor = W1ThermSensor()

# Se utiliza while True loop para ejecutar el código dentro de él para siempre.
while True:
        # Se obtiene el valor de temperatura y se almacena en temperature
        temperature = sensor.get_temperature()
        # Se imprime el valor de temperatura
        print("The temperature is %s celsius" % temperature)
        # Se espera 1 segundo para tomar la siguiente muestra
        time.sleep(1)

