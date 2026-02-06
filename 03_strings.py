### Strings ###
my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon un salto de línea"
print(my_new_line_string)
my_tab_string = "\tEste es un stringcon una tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formateo
name, surname, age = "Milton", "Reyes", 16
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años") #La manera moderna de formatear strings

# Desempaquetado de caracteres
lenguage = "Python"
a, b, c, d, e, f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
lenguage_slice = lenguage[1:3]
print(lenguage_slice)

lenguage_slice = lenguage[0:2]
print(lenguage_slice)

lenguage_slice = lenguage[1:]
print(lenguage_slice)

lenguage_slice = lenguage[-1]
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2] # Cada dos caracteres
print(lenguage_slice)

# Reverse string
reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

# Funciones de string

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.lower())
print(lenguage.upper().isupper())
print(lenguage.startswith("Py"))
print("hola Python" [0:4])