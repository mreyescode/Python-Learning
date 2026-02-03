# Python-Learning
Repositorio de aprendizaje en Python donde documento mi progreso como programador junior. Incluye fundamentos, ejercicios prácticos y mini proyectos enfocados en resolver problemas reales y automatizar tareas, especialmente aplicadas a flujos creativos.
 <hr>
<h1>Hola Mundo 01/02/2026</h1>
¡Bienvenido al inicio de mi viaje con Python!

Este es el clásico primer programa que todo desarrollador escribe cuando comienza a aprender un lenguaje de programación. Es simple, directo y con un propósito fundamental: imprimir mensajes en la consola y familiarizarnos con la sintaxis básica del lenguaje.

🎯 ¿Qué aprendí aquí?
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

💡 Reflexión personal
Este es el punto de partida. Puede parecer básico, pero estos fundamentos son la base de todo. Sin entender cómo funcionan print(), las variables y los tipos de datos, no puedes avanzar a conceptos más complejos.

Me gustó la claridad que ofrece Python. Es elegante, directo y fácil de leer. El uso de f-strings para formatear cadenas es algo que definitivamente seguiré usando más adelante.

🚀 Siguiente paso
Con estos fundamentos dominados, es momento de explorar variables más a fondo y comenzar a trabajar con operadores. El camino apenas comienza.

Nota: Este repositorio está en construcción activa. Cada archivo que suba será documentado con el mismo nivel de detalle y profesionalismo. Si tienes sugerencias o quieres conectar, mi LinkedIn y GitHub están abiertos para colaborar.
<hr>
<h1>📦Variables</h1>
Las variables son el corazón de cualquier programa. Sin ellas, no podríamos almacenar información, procesarla ni crear aplicaciones dinámicas. En esta sección me sumergí en cómo Python maneja las variables y por qué son tan flexibles.

🎯 ¿Qué aprendí aquí?
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

💡 Reflexión personal
Las variables son mucho más que simples "cajas" para guardar información. En Python, el tipado dinámico te da una flexibilidad increíble, pero también te exige responsabilidad. Puedes cambiar el tipo de una variable en cualquier momento, pero eso no significa que debas hacerlo sin razón.

Me gustó descubrir que Python no te obliga a declarar tipos explícitamente, pero sí puedes usar type hints para hacer tu código más legible y profesional. Es un balance perfecto entre flexibilidad y claridad.

También fue interesante ver cómo input() siempre devuelve un str, así que si necesitas trabajar con números, tienes que hacer el casting manualmente. Ese tipo de detalles son los que separan el código que funciona del código que funciona bien.


