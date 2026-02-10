### Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (16,15,17,18,20)
my_tuple = (16, 1.65, "Milton", "Reyes")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[3])
#print(my_tuple[-6]) # IndexError: tuple index out of range

print(my_tuple.count("Milton"))
print(my_tuple.index(1.65))
#my_tuple[1] = 1.80  #Una tupla es inmutable, por lo que no se pueden modificar sus elementos

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
#Solo se puede hacer otra tupla sumanado dos tuplas existentes

my_tuple = list(my_tuple)  #Convertir una tupla en una lista
print(type(my_tuple))

my_tuple[3] = "Martínez"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)  #Volver a convertir la lista en una tupla
print(type(my_tuple))
print(my_tuple)

#del my_tuple
#del my_tuple[0]
#print(my_tuple) #NameError: name 'my_tuple' is not defined
#La función del, solo es propia de las variables mutables
#No se puede eliminar la tupla, pero si la variable que la contiene