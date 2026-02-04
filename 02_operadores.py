### Operadores Aritméticos###

print( 2 + 2 )      # Suma
print( 5 - 3 )      # Resta
print( 4 * 3 )      # Multiplicación
print( 8 / 2 )      # División
print( 7 % 3 )      # Módulo (residuo de la división) (7 dividido 3 es 2, lo que queda, osea el residuo 1)
print( 2 ** 3 )     # Exponente (2 elevado a la 3)
print( 10 // 3 )    # División entera (10 dividido 3 es 3.33, pero solo toma la parte entera, osea 3)
print( 3 + 2 * 5 / 2 ** 2 )  # Se pueden comninar todos lo operadores


print("Hola " + "Python")  # Concatenación de cadenas
print("Hola " + str(2))          # Repetición de cadenas
print("Hola " * 3)          # Repetición de cadenas

my_float = 2.5 * 2
print("Hola " * int(my_float)) # POR QUÉ NO FUNCIONA SIN ANTES CONVERTIOMOS A ENTERO LA VARIABLE?
"""
Porque a pesar que la multiplicación da como resultado da un número entero (5), el tipo de dato de la variable my_float es float (2.5 * 2 = 5.0).
Por lo tanto lo toma comom float y no comom entero, por eso no funciona sin antes
convertirlo a entero
"""

### Operadores de Comparación ###

print( 3 > 2 )      # Mayor que
print( 3 < 2 )      # Menor que
print( 3 >= 2 )     # Mayor o igual que
print( 3 <= 2 )     # Menor o igual que
print( 3 == 2 )     # Igual a
print( 3 != 2 )     # Diferente de
print( 3 > 2 > 1 )  # Se pueden combinar todos los operadores de comparación
print("Hola" > "Python")  # Comparación de cadenas (se basa en el orden alfabético, H se encuentra antes que P)

### Operadores Lógicos ###

print( 3 > 4 and "Hola" > "Python" )  # AND (y) Si todso son un False, el resultado es False
print( 3 > 4 or "Hola" > "Python" )        # OR (o) Si hay al menos un True, el resultado es True
print( not( 3 > 4 ) )                      # NOT (no) Invierte el valor lógico (True -> False, False -> True)

