# Filter aplica una funcion a todos los elementos de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def miFuncion(x):
    if x % 2 == 0:
        return True

    return False

resultado = filter(miFuncion, numeros)
print(list(resultado))

# Lo anterior podria hacerse con una lambda
# resultado = filter(lambda x: x % 2 == 0, numeros)

# zip asocia elementos de distintas listas

cursos = ['Java', 'Python', 'Ciberseguridad']
asistentes = [10, 20, 32]
demo = zip(cursos, asistentes)
print(list(demo))

# Se queda bloqueado hasta que escribamos por teclado
a = input('Diga su nombre:')
print(f'Hola {a}')