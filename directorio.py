import os

dir = r"ruta_del_directorio"
file = os.path.isfile

for file in dir:
    print(os.listdir(dir))
    break