# Debemos crear un script que nos diga si es la hora de ir a casa. Tenemos que hacer uso del modulo times
# Necesitamos la fecha del sistema para poder comprobar la hora. En el caso que sean mas de las 21 se
# mostrara un mensaje.

import time

# Inicializamos las variables y le damos formato para que solo se vean las horas y minutos
hora = time.strftime('%H')
minutos = time.strftime('%M')

# Comprobamos si la hora es mayor que 21
if int(hora) >= 21:
    print ("Es la hora de salir")
else:
    print (f'Quedan {format(20-int(hora))} horas y {format(59-int(minutos))} minutos para la salida')
#    print ("Quedan {} horas y {} minutos para salir".format(20-int(hora),59-int(minutos)))

# Con el else podemos ver las dos formas de mostrarlo por pantalla
