# con kwargs pasamos un numero variable de argumentos con nombre

import operaciones

def suma(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

    if kwargs['coche']=='rojo':
        print("Tu coche es rojo")

    res = operaciones.resta(5, 2)
    print(res)

    div = operaciones.division(6, 2)
    print(div)

suma(vivienda="piso", coche="rojo")

