#Ejercicio 1
my_m_set = {1,2,3,4,5}
print(my_m_set)
print(type(my_m_set))

#Ejercicio 2
my_m_set.add(6)
print(my_m_set)

#Ejercicio 3
my_m_set.add(5)
print(my_m_set) #No da ningún error, pero tampoco pasa nada, ya que a un set no se le puede agregar elementos duplicados


#Ejercicio 4
print(3 in my_m_set)

#Ejercicio 5
my_m_set.remove(4)
print(my_m_set)

#Ejercicio 6
my_m_set.clear()
print(len(my_m_set))

#Ejercicio 7
my_fruit_set = {"apple", "banana", "orange"}
my_fruit_list = list(my_fruit_set)
print(type(my_fruit_list))
print(my_fruit_list[0])


#Ejercicio 8
my_first_set = {1, 2, 3}
my_second_set = {4, 5, 6}
my_third_set = my_first_set.union(my_second_set)
print(my_third_set)

#Ejercicio 9
my_num1_set = {1, 2, 3, 4}
my_num2_set = {3, 4, 5, 6}
my_num3_set = my_num1_set.difference(my_num2_set)
print(my_num3_set)
#El resultado es que imprime los elementos del primer set, que no se encuentran en el segundo
#Pero si en el segundo set, hay elementos que no están en el primero, este no los toma en cuenta al momento de imprimirlos

#Ejercicio 10
#my_set = {"Milton", "Reyes"}
#del my_set
#print(my_set)
"""
Muestra error, ya que NO puedes usar del para eliminar elementos específicos porque los sets no tienen índices.
Para eso usas .remove() o .discard()
"""






