#Ejercicio 1
tupla1 = (10, 20, 30, 40, 50)


#Ejercicio 2
tupla2 = (100, 200, 300, 400, 500)
print(tupla2[1])

#Ejercicio 3
tupla3 = (1, 2, 3)
tupla4 = (4, 5, 6)
#tupla3.insert(0, 10)  # Esto generará un error porque las tuplas son inmutables

#Ejercicio 4
tupla5 = (1, 2, 3, 3, 4, 5, 3)
print(tupla5.count(3))

#Ejercicio 5
tupla5 = ("Java", "Python", "Javascript", "Python")
print(tupla5.index("Python")) #Me marca el índice del primer elemento que encuentra correspondiente al que le pido

#Ejercicio 6
tupla_combinada = tupla3 + tupla4
print(tupla_combinada)

#Ejercicio 7
sub_tupla = tupla1[2:4]
print(sub_tupla)

#Ejercicio 8
colors_tuple = ("rojo", "verde", "azul")
print(type(colors_tuple))
colors_list = list(colors_tuple)
print(type(colors_list))
colors_list.insert(1, "amarillo")
colors_tuple = tuple(colors_list)
print(colors_tuple)

#Ejercicio 9
del tupla1
#print(tupla1)  # Esto generará un error porque la tupla ha sido eliminada

#Ejercicio 10
tupla6 = (100,)
print(type(tupla6))  # Esto mostrará que es una tupla, no un entero
print(tupla6[0])  # Accediendo al único elemento de la tupla

"""
Si en una tupla agregas un solo elemento sin una "," lo toma como un entero y no como una tupla.
"""