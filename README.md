# Python-Learning
<h4>Todos los ejercicios los pueden ver en el archivo "00_ejercicios.py"</h4>
Repositorio de aprendizaje en Python donde documento mi progreso como programador junior. Incluye fundamentos, ejercicios prácticos y mini proyectos enfocados en resolver problemas reales y automatizar tareas, especialmente aplicadas a flujos creativos.
Nota: Cada concepto que aprendo lo documento con detalle y lo aplico en ejercicios reales. Este repositorio es un reflejo transparente de mi aprendizaje. Si tienes feedback o sugerencias, mis redes están abiertas para colaborar.
!!!!Todos los archivos que no tengan un "_ejerc.py" es código que fue creado por el curso de Python de Mourdev!!!!


 <hr>
<h1>Hola Mundo 01/02/2026</h1>
¡Bienvenido al inicio de mi viaje con Python!

Este es el clásico primer programa que todo desarrollador escribe cuando comienza a aprender un lenguaje de programación. Es simple, directo y con un propósito fundamental: imprimir mensajes en la consola y familiarizarnos con la sintaxis básica del lenguaje.

<h2>🎯 ¿Qué aprendí aquí?</h2>
En esta sección trabajé con lo esencial:

Imprimir mensajes con print(): La función más básica pero fundamental de Python

Comentarios: Aprendí a documentar mi código usando # para comentarios de una línea y """ """ para comentarios de varias líneas

Tipos de datos: Exploré los tipos de datos fundamentales usando type() para identificarlos

str (cadenas de texto)

int (números enteros)

float (números decimales)

bool (valores booleanos: True/False)

complex (números complejos)

Concatenación de cadenas: Uní texto usando el operador +

Variables: Almacené información en variables y las mostré en pantalla

Entrada del usuario con input(): Interactué con el usuario capturando datos desde la consola

F-strings: Usé formateo moderno de cadenas para crear mensajes dinámicos

📂 Archivos relacionados
00_hello.py: Código basado en el curso de Brais Moure, donde exploramos tipos de datos y comentarios

00.5_hello_ejerc.py: Mis propios ejercicios prácticos donde apliqué todo lo aprendido

<h4>💡 Reflexión personal</h4>
Este es el punto de partida. Puede parecer básico, pero estos fundamentos son la base de todo. Sin entender cómo funcionan print(), las variables y los tipos de datos, no puedes avanzar a conceptos más complejos.

Me gustó la claridad que ofrece Python. Es elegante, directo y fácil de leer. El uso de f-strings para formatear cadenas es algo que definitivamente seguiré usando más adelante.

🚀 Siguiente paso
Con estos fundamentos dominados, es momento de explorar variables más a fondo y comenzar a trabajar con operadores. El camino apenas comienza.

Nota: Este repositorio está en construcción activa. Cada archivo que suba será documentado con el mismo nivel de detalle y profesionalismo. Si tienes sugerencias o quieres conectar, mi LinkedIn y GitHub están abiertos para colaborar.
<hr>
<h1>📦Variables</h1>
Las variables son el corazón de cualquier programa. Sin ellas, no podríamos almacenar información, procesarla ni crear aplicaciones dinámicas. En esta sección me sumergí en cómo Python maneja las variables y por qué son tan flexibles.

<h2>🎯 ¿Qué aprendí aquí?</h2>
Aquí me enfoqué en dominar el almacenamiento y manipulación de datos:
Declaración y asignación de variables: Aprendí que Python es dinámico, no necesitas declarar el tipo de variable explícitamente
Tipado dinámico: Una variable puede cambiar de tipo en cualquier momento (de int a str, por ejemplo)
Conversión de tipos (Casting): Convertí datos entre tipos usando str(), int(), float(), etc.
Variables booleanas: Trabajé con valores True y False para representar estados lógicos
Función len(): Calculé la longitud de cadenas para contar caracteres
Asignación múltiple: Declaré varias variables en una sola línea (aunque hay que usarlo con cuidado para no sacrificar legibilidad)
Entrada del usuario con input(): Capturé datos dinámicos del usuario
Reasignación de variables: Descubrí que las variables son mutables y pueden cambiar de valor en cualquier momento
Type hints (anotaciones de tipo): Usé la sintaxis variable: tipo para documentar el tipo esperado, aunque Python no lo fuerza
El tipo especial NoneType: Entendí que funciones como print() no retornan valor, por eso su tipo es None.

<h4>💡 Reflexión personal</h2>
Las variables son mucho más que simples "cajas" para guardar información. En Python, el tipado dinámico te da una flexibilidad increíble, pero también te exige responsabilidad. Puedes cambiar el tipo de una variable en cualquier momento, pero eso no significa que debas hacerlo sin razón.

Me gustó descubrir que Python no te obliga a declarar tipos explícitamente, pero sí puedes usar type hints para hacer tu código más legible y profesional. Es un balance perfecto entre flexibilidad y claridad.

También fue interesante ver cómo input() siempre devuelve un str, así que si necesitas trabajar con números, tienes que hacer el casting manualmente. Ese tipo de detalles son los que separan el código que funciona del código que funciona bien.

<h1>⚙️ Operadores</h1>
Los operadores son las herramientas que nos permiten hacer cálculos, comparar valores y tomar decisiones lógicas en Python. Sin ellos, nuestros programas serían estáticos y sin vida. En esta sección exploré cómo Python maneja las operaciones matemáticas, las comparaciones y la lógica booleana.

<h2>🎯 ¿Qué aprendí aquí?</h2>
Aquí me enfoqué en dominar las tres categorías principales de operadores:

Operadores Aritméticos
+ Suma

- Resta

* Multiplicación

/ División (siempre retorna float)

% Módulo (residuo de una división)

** Exponente (potencias)

// División entera (elimina los decimales)

Operadores con Cadenas
+ Concatenación de strings

* Repetición de cadenas (ej: "Python" * 3 → "PythonPythonPython")

Operadores de Comparación
> Mayor que

< Menor que

>= Mayor o igual que

<= Menor o igual que

== Igual a

!= Diferente de

Dato importante: Las comparaciones siempre retornan un valor booleano (True o False)

Operadores Lógicos
and → Retorna True solo si ambas condiciones son verdaderas

or → Retorna True si al menos una condición es verdadera

not → Invierte el valor lógico (True → False, False → True)

📂 Archivos relacionados
02_operadores.py: Código basado en el curso de Brais Moure, donde exploramos todos los tipos de operadores

02.5_operadores_ejerc.py: Mis ejercicios prácticos donde apliqué operaciones aritméticas, comparaciones y lógica booleana

<h4>💡 Reflexión personal</h4>
Los operadores son el motor de cualquier programa. Lo que más me sorprendió fue descubrir que Python puede comparar cadenas de texto usando el orden alfabético. Por ejemplo, "apple" < "banana" retorna True porque la letra a viene antes que b.

También entendí algo crucial: cuando multiplicas un float por un número entero, el resultado sigue siendo float. Por eso, si quieres usar ese resultado para repetir una cadena (como "Hola" * my_float), primero debes convertirlo a int con int(). Ese tipo de detalles hacen la diferencia entre un código que funciona y un código que genera errores.

Los operadores lógicos (and, or, not) son fundamentales para construir condiciones complejas. Son la base de las decisiones que tomará mi código más adelante cuando trabaje con condicionales y bucles.
<hr>
<h1>📜 Strings (Cadenas de Texto)</h1>
Las cadenas de texto son uno de los tipos de datos más utilizados en cualquier programa. Desde mensajes en pantalla hasta procesamiento de información, los strings están en todas partes. En esta sección me sumergí en cómo Python maneja el texto y todas las herramientas poderosas que ofrece para manipularlo.

<h1>🎯 ¿Qué aprendí aquí?</h1>
Aquí me enfoqué en dominar el arte de trabajar con texto:

Operaciones Básicas
len(): Calcular la longitud de un string

Concatenación: Unir cadenas usando +

Caracteres de escape: \n (salto de línea), \t (tabulación)

Repetición: Multiplicar strings (ej: "Python" * 3)

Formateo de Strings
.format(): Método tradicional para insertar variables

f-strings: La forma moderna y elegante (ej: f"Hola {name}")

Desempaquetado de Caracteres
Puedes asignar cada carácter de un string a variables individuales:

python
p, y, t, h, o, n = "Python"
Slicing (Cortes)
El slicing te permite extraer porciones específicas de un string:

string[1:3] → Caracteres desde índice 1 hasta 2 (el 3 no se incluye)

string[0:6:2] → Cada dos caracteres

string[::-1] → Invierte el string completamente

string[-1] → Último carácter

<h5>Métodos Importantes</h5>
.upper() → Convertir a MAYÚSCULAS

.lower() → Convertir a minúsculas

.capitalize() → Primera letra en mayúscula

.count("x") → Contar cuántas veces aparece un carácter

.isnumeric() → Verificar si es numérico

.isupper() → Verificar si está en mayúsculas

.startswith("Py") → Verificar si empieza con cierto texto
<hr>
<h4>📂 Archivos relacionados</h4>
03_strings.py: Código basado en el curso de Brais Moure, donde exploramos strings desde lo básico hasta técnicas avanzadas

03.5_strings_ejerc.py: Mis ejercicios prácticos donde apliqué slicing, métodos, formateo y más

<h4>💡 Reflexión personal</h4>
Los strings son más poderosos de lo que pensaba. Al principio parecen simples, pero cuando descubres el slicing y todos los métodos disponibles, te das cuenta de que Python te da control total sobre el texto.

Lo que más me sorprendió fue el slicing con [::-1] para invertir strings. Es elegante, pythónico y demuestra que Python fue diseñado para ser intuitivo. También me encanta que puedas desempaquetar caracteres directamente en variables, aunque hay que usarlo con cuidado para no sacrificar legibilidad.

Los f-strings son definitivamente la forma moderna de formatear texto. Son más limpios y legibles que .format(), y se sienten naturales al escribir código. A partir de ahora, serán mi método preferido.
<hr>

<h1>📋 Listas</h1>
Las listas son una de las estructuras de datos más importantes y versátiles en Python. Son mutables, ordenadas y pueden contener cualquier tipo de dato. Desde almacenar números hasta combinar strings, enteros y floats en una misma lista, las posibilidades son infinitas. En esta sección me sumergí en el poder de las listas y todas las operaciones que puedes realizar con ellas.

<h2>🎯 ¿Qué aprendí aquí?</h2>
Aquí me enfoqué en dominar la manipulación de colecciones de datos:

Crear Listas
my_list = list() → Crear lista vacía con constructor

my_list = [] → Crear lista vacía con sintaxis literal

my_list = [1, 2, 3] → Crear lista con elementos

Las listas pueden contener diferentes tipos de datos: [16, 1.65, "Milton", "Reyes"]

Acceder a Elementos
my_list[0] → Primer elemento

my_list[-1] → Último elemento

my_list[-2] → Penúltimo elemento

Slicing: my_list[1:3] → Elementos desde índice 1 hasta 2 (el 3 no se incluye)

Métodos para Agregar Elementos
.append(element) → Agregar al final de la lista

.insert(index, element) → Insertar en posición específica

Métodos para Eliminar Elementos
.remove(value) → Eliminar la primera ocurrencia del valor

.pop() → Eliminar y retornar el último elemento

.pop(index) → Eliminar y retornar elemento en posición específica

del my_list[index] → Eliminar elemento por índice (sin retornar)

.clear() → Vaciar toda la lista

Métodos de Ordenamiento y Manipulación
.reverse() → Invertir el orden de los elementos

.sort() → Ordenar de menor a mayor (modifica la lista original)

.copy() → Crear una copia independiente de la lista

Métodos de Búsqueda e Información
len(my_list) → Número total de elementos

.count(value) → Contar cuántas veces aparece un valor

.index(value) → Obtener la posición de la primera ocurrencia de un valor

Operaciones Avanzadas
Concatenación: list1 + list2 → Une dos listas

Desempaquetado: Asignar elementos a variables individuales

python
age, height, name, surname = my_list
⚠️ Importante: El número de variables debe coincidir con el número de elementos

📂 Archivos relacionados
04_listas.py: Código basado en el curso de Brais Moure, donde exploramos listas desde lo básico hasta operaciones avanzadas

04.5_listas_ejerc.py: Mis ejercicios prácticos donde apliqué todos los métodos de manipulación de listas

<h4>💡 Reflexión personal</h4>
Las listas son poderosas. Lo que más me impresionó es que son mutables, lo que significa que puedes modificarlas después de crearlas. Esto las hace perfectas para almacenar datos dinámicos.

Entender la diferencia entre .remove(), .pop() y del fue crucial:

.remove(value) elimina el primer elemento que coincida con el valor

.pop(index) elimina y devuelve el elemento (puedes guardarlo en una variable)

del list[index] elimina sin devolver nada
Entender la diferencia entre .remove(), .pop() y del fue crucial:

.remove(value) elimina el primer elemento que coincida con el valor

.pop(index) elimina y devuelve el elemento (puedes guardarlo en una variable)

del list[index] elimina sin devolver nada

También descubrí que .copy() es esencial cuando quieres trabajar con copias independientes. Si solo haces new_list = old_list, ambas variables apuntan a la misma lista en memoria, por lo que modificar una afecta a la otra. Con .copy(), tienes una lista completamente independiente.
<hr>
<h1>🔒 Tuplas</h1>
Las tuplas son estructuras de datos similares a las listas, pero con una diferencia fundamental: son inmutables. Una vez que creas una tupla, no puedes modificar sus elementos. Esta característica las hace perfectas para datos que no deben cambiar, ofreciendo seguridad y eficiencia. En esta sección exploré cómo funcionan las tuplas y cuándo usarlas.

<h2>🎯 ¿Qué aprendí aquí?</h2>
Aquí me enfoqué en entender las tuplas y sus diferencias con las listas:

Crear Tuplas
my_tuple = tuple() → Crear tupla vacía con constructor

my_tuple = () → Crear tupla vacía con sintaxis literal

my_tuple = (1, 2, 3) → Crear tupla con elementos

Las tuplas pueden contener diferentes tipos de datos: (16, 1.65, "Milton", "Reyes")

⚠️ Importante - Tuplas de un solo elemento:

python
tupla = (100,)  # ✅ Tupla válida (nota la coma)
no_tupla = (100)  # ❌ Esto es un entero, NO una tupla
Acceder a Elementos
my_tuple[0] → Primer elemento

my_tuple[-1] → Último elemento

Slicing: my_tuple[2:4] → Elementos desde índice 2 hasta 3

Métodos Disponibles
Las tuplas tienen solo dos métodos (porque son inmutables):

.count(value) → Contar cuántas veces aparece un valor

.index(value) → Obtener la posición de la primera ocurrencia

Operaciones con Tuplas
Concatenación: tuple1 + tuple2 → Crear una nueva tupla combinada

Conversión a lista: list(my_tuple) → Para modificar elementos indirectamente

Conversión a tupla: tuple(my_list) → Volver a convertir la lista en tupla

Eliminar tupla: del my_tuple → Elimina la variable (no elementos individuales)

Inmutabilidad: La clave de las tuplas
python
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
Si necesitas modificar una tupla:

Conviértela en lista: my_list = list(my_tuple)

Modifica la lista: my_list[0] = 10

Vuelve a convertirla en tupla: my_tuple = tuple(my_list)

📂 Archivos relacionados
05_tuplas.py: Código basado en el curso de Brais Moure, donde exploramos tuplas y su inmutabilidad

05.5_tuplas_ejerc.py: Mis ejercicios prácticos donde apliqué todos los conceptos de tuplas

<h4>💡 Reflexión personal</h4>
Las tuplas son la versión segura e inmutable de las listas. Al principio, pueden parecer limitadas porque no puedes modificarlas, pero esa es precisamente su fortaleza. Si tienes datos que no deben cambiar (coordenadas, configuraciones, datos fijos), las tuplas son la mejor opción.

Lo que más me sorprendió fue descubrir que para crear una tupla de un solo elemento, debes incluir una coma: (100,). Si no lo haces, Python lo interpreta como un entero entre paréntesis, no como una tupla. Ese tipo de detalles técnicos son los que separan el código amateur del profesional.

También aprendí que aunque las tuplas son inmutables, puedes convertirlas temporalmente en listas para modificarlas. Esto es útil cuando necesitas hacer cambios específicos pero quieres mantener la inmutabilidad como regla general.

Las tuplas son más eficientes en memoria que las listas porque Python sabe que no cambiarán. Además, pueden usarse como claves en diccionarios (las listas no pueden), lo cual las hace indispensables en ciertos contextos.
<hr>
<h1>🧩Sets (Conjuntos)</h1> 

Los sets en Python son una estructura de datos diseñada para trabajar con elementos únicos y para hacer validaciones rápidas de pertenencia (si algo está o no está). Son perfectos cuando no te interesa el orden, pero sí te importa evitar duplicados y manejar “colecciones limpias”.
​

<h2>🎯 ¿Qué aprendí aquí?</h2>
Cómo crear sets: con set() o con llaves {} (pero ojo: {} vacío es un diccionario, no un set).
​

Un set NO está ordenado: al imprimirlo, el orden puede cambiar, así que no debes confiar en posiciones.
​

No admite repetidos: si intentas agregar un valor duplicado, no truena, solo no pasa nada.

Agregar y quitar elementos: add() para agregar, remove() para eliminar un elemento específico, clear() para vaciar.

Pertenencia con in: la forma correcta de comprobar si un elemento existe dentro de un set.

Operaciones entre sets: union() para unir conjuntos y difference() para obtener lo que está en uno y no en el otro.

Convertir a lista: se puede con list(my_set), pero es “peligroso” indexar esa lista si dependes del orden, porque viene de algo que no es ordenado.

📂 Archivos relacionados
06_sets.py: práctica guiada (basada en el curso) donde exploré creación, tipos, pertenencia, conversión a lista y operaciones como union() y difference().
​

06.5_set_ejerc.py: mis ejercicios aplicando lo esencial: no duplicados, in, remove(), clear(), union() y difference().
​

<h4>💡 Reflexión personal</h4>
Un set es como un filtro automático: tú metes cosas y Python se asegura de que no haya copias. Eso lo vuelve muy útil para limpiar datos repetidos o verificar rápidamente si algo ya existe (por ejemplo: usuarios, IDs, tags).

También entendí una regla de oro: si necesito orden y posiciones, uso listas; si necesito unicidad y validación rápida, uso sets.
​
