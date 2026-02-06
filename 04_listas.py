### List ###
my_list = list()
my_other_list = []


print(len(my_list))

my_list = [35, 24, 62, 52, 12]

print(my_list)
print(len(my_list))

my_other_list = [16, 1.65, "Milton", "Reyes", ] #No hace falta que guardemos el mismo tipo de dato en una lista
print(my_other_list)
print(len(my_other_list))

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(24)) #Cuenta cuántas veces aparece el valor 24 en la lista
#print(my_other_list[-5]) #IndexError: list index out of range

"""
Para ontar los elementos de una lista usamos la función len(),
pero para contar cuántas veces aparece un valor específico en la lista usamos el método count().

"""
age, height, name, surname = my_other_list #Se les puede asignar variables a los elementos de una lista
"""
Pero ojo, el número de variables debe coincidir con el número de elementos en la lista.
"""
print(age)
print(height)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list) 


my_new_list = my_list.copy() #Copia una lista en otra, por lo tanto ,si eliminas un elemento de una lista no se elimina de la otra, porque ya cuenta como una lista independiente
print(my_new_list)

my_other_list.append("Reyes Code") #Agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Azul") #Agrega un elemento en la posición indicada
print(my_other_list)

my_other_list.insert(1, "Rojo") 
print(my_other_list)

my_other_list[1] = "Azul" #Modifica el valor en la posición indicada
print(my_other_list)


my_other_list.insert(1, "Nuevo valor") #Agrega un elemento en la posición indicada
print(my_other_list)

my_other_list.remove("Nuevo valor") #Elimina el primer elemento que coincida con el valor indicado
print(my_other_list)
my_list.remove(52) #Elimina el primer elemento que coincida con el valor indicado
print(my_list)

print(my_list.pop(2)) #Elimina el último elemento de la lista
print(my_list)

del my_list[1] #Elimina el elemento en la posición indicada
print(my_list)

my_pop_element = my_list.pop(1) #Elimina el elemento en la posición indicada y lo guarda en una variable
print(my_pop_element)
print(my_list)

my_list.clear() #Elimina todos los elementos de la lista
print(my_list)

"""
la dunción "remove" elimina el primer elemento que coincida con el valor indicado,
mientras que la función "pop" elimina el elemento en la posición indicada y lo devuelve.
"del" elimina el elemento en la posición indicada sin devolverlo por índice.
"clear" elimina todos los elementos de la lista.    
"""


my_new_list.reverse() #Invierte el orden de los elementos en la lista
print(my_new_list)

my_new_list.sort() #Ordena los elementos de la lista de menor a mayor
print(my_new_list)

print(my_new_list[1:3])

print  (my_other_list.index("Reyes")) #Devuelve la posición del primer elemento que coincida con el valor indicado