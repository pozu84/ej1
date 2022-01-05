# a = 5
# b = 6
# c = 7
#
# resultado = (a < b)
# print(resultado)
#
# # podemos imprimir directamente el resultado de la condicion sin necesidad de asignarlo a una variable
# print(a > b)
#
# resultado2 = (a > 5 and c < 7)
# print(resultado2)
#
# if (a == 5):
#     print("Es cierta la condicion")
#
# if (b < 5):
#     print("Es cierta la condicion")
# print("La condicion no es cierta")
#
#
# # Bucle while
# contador = 1
#
# while contador <= 10:
#     print("El contador es", contador)
#     contador += 1
#
# ################################################################################################
# contador2 = 1
#
# while contador2 <= 10:
#     if contador2 % 2 == 0:
#         print(contador2, "es par")
#     contador2 += 1
#
# ################################################################################################
# contador3 = 1
#
# while contador3 <= 10:
#     print("Contador", contador3)
#     if contador3 == 5:
#         print("Rompo el Bucle")
#         break
#     contador3 += 1
# ################################################################################################
# lista = [1, 2, 3, 4, 5]
#
# for valorActual in lista:
#     print("Valor de la lista", valorActual)
#
# for numero in range(5, 10):
#     print(numero)
#
#
# lista2 = ["hola", "adios", "mensaje"]
#
# for palabra in lista2:
#     print("palabra actual del bucle", palabra)
#     if palabra == "mensaje":
#         print("He encontrado la palabra", palabra)
#
# lista3 = ["hola", "adios", "mensaje"]
#
# if "mercurio" not in lista3:
#     print("Mercurio no aparece en la lista")
#
# # Ordenar una lista
# lista4 = [3, 7, 4, 9, 1, 0]
# print(lista4)
#
# listaOrdenada = sorted(lista4)
# print(listaOrdenada)
#
# listaOrdenada = sorted(lista4, reverse=True)
# print(listaOrdenada)

################################################################################################
# NO COMPILA
# buscar = 4
#
# match buscar:
#     case 1:
#         print("valor 1")
#     case 2:
#         print("valor 2")
#     case 3:
#         print("valor 3")
#     case 4:
#         print("valor 4")

import os

dir = r"C:\Users\pozu8\Downloads"
file = os.path.isfile

for file in dir:
    print(os.listdir(dir))
