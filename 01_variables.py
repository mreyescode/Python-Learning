# Variables

my_variable = "My string variable"
print(my_variable)


my_int_variable = 1
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = True
print(my_bool_variable)

print(my_variable, my_int_variable, my_bool_variable)

#Concatenación de variables e impresión

print(type(print((my_variable, my_int_variable, my_bool_variable))))

"""
¿Por qué se imprimió 'None' como tipo de dato?
Porque la función print() no retorna ningún valor,
por lo tanto su tipo de dato es 'NoneType',
ya que es una función predeterminada de python
"""

# Longitud de una variable string
print(len(my_variable))  # Imprime la longitud de la variable string

print("Este es el valor de :", my_variable)

# Variables en una sola línea
#Cuidado con abusar de esta práctica, puede dificultar la lectura del código
name, surname, age = "Milton", "Reyes", 17
print(name, surname, age) #No juntar las variables

#Inputs 
"""
name = input("¿Cuál es tu nombre? ")
age = input("¿Cuántos años tienes? ")

print(name)
print(age)
"""
"""
¿Qué está pasando aquí si las variables 'name' y 'age' ya estaban asignadas?
R: Las variables pueden ser reasignadas en cualquier momento, incluso si ya tenían un valor previo.
El nuevo valor sobrescribe al anterior. Por eso al momento de poner otro nombre
y otra edad en los input's, se reasigna las variables 'name' y 'age' con los nuevos valores ingresados.
"""

#Cammbiamos el tipo

name = 16
age = "Milton"

print(name)
print(age)

adress: str = "Mi calle"
adress = 32
print(adress)
print(type(adress))