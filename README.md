# Python-Learning
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
