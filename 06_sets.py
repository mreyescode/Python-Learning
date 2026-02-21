### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es de tipo diccionario

my_other_set = {"Milton", "Reyes", 16}
print(type(my_other_set))

print(len(my_other_set))

print(my_other_set)
my_other_set.add("Martínez")
print(my_other_set)

"""
Un set no es una estructura Ordenanda
Y tampoco admite elementos repetidos
"""
print(my_other_set) #Cada vez imprime un orden distinto

print("Reyes" in my_other_set)
#Así se compureba si ese elemento existe en tus sets
print("Reyess" in my_other_set)

my_other_set.remove("Reyes")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

#del my_other_set Da error, ya que elimina toda la propiedad
#print(my_other_set)

my_set = {"Milton", "Reyes", 16}
my_list = list(my_set)
print(type(my_list))
print(my_list)
print(my_list[1]) # Es muy peligroso hacer esto, ya que cada vez que uno imprime un set, transformado en una lista, aún así cambia de posición

my_other_set = {"Javascript", "HTML", "CSS", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union({"Java"})) # Por qué poner corchetes cuando quieres agregrar un elemento?
#Porque sino cada caracter se agrega al set como un elemento diferente: "a", "j", "v", solo agregaría una "a", ya que solo permite elementos únicos
print(my_new_set.union(my_new_set)) #No es un error, pero no aparece nada, ya que los sets, no permiten elementos duplicados

print(my_new_set.difference(my_other_set))
"""
Lo que hace esta función, esque imprime los elementos del primer set, 
que no están en el segundo set
"""
