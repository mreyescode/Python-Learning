# Ejercicio 1
name = "Milton Ovidio Reyes Martínez"
age = 16
heigth = 1.65
print(name)
print(age)
print(heigth)

#Ejercicio 2

age: str = "16"
print("¿Cuánto años tienes?", age)

#Ejercicio 3
is_student: bool = True
print("¿Eres estudiante?", is_student)

#Ejercicio 4
print(len(name))

character_count = len(name)
print("El nombre tiene", character_count, "caracteres.")
print(type(character_count))

#Ejercicio 5
yo: str = name + " " + age + " " + str(heigth) + " " + str(is_student)
print(yo)
print(type(yo))

"""
#Ejercicio 6
favorite_color = input("¿Cuál es tu color favorito?")
print("Tu color favorito es el:", favorite_color)
"""

"""
#Ejercicio 7
fruit = "Durazno"
fruit = input("¿Cuál es tu fruta favorita?")
print("Tu fruta favorita es:", fruit)
"""

"""
#Ejercicio 8
price = 19.99
print("El precio del producto es:", price)
price = input("Ingresa un nuevo precio para el producto:")
print("El nuevo precio del producto es:", price)
print(type((int(price))))
"""
"""
#Ejercicio 9
adress_len = input("Ingresa tu dirección:")
print("La longitud de tu dirección es:", len(adress_len))
"""

#Ejercicio 10
phone: str = "9671667694"
print(type(phone))
phone = int(phone)
phone = 2009
print(type(phone))