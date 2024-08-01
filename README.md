# Python for Data Science

<h1>0 - Starting</h1>

<br /><br />

> Subject
> - :white_check_mark: [English](#subject-english)
>
> - :white_check_mark: [Castellano](#subject-castellano)

<br /><br />

> Evaluation     
> - :white_check_mark: [English](#evaluation) 
>
> - :white_check_mark: [Castellano](#evaluación)

<br /><br />

> Ficheros ex00
>
> - :white_check_mark: [Hello.py](#ex00-hello-py) 

<br /><br />

> Ficheros ex01
>
> - :white_check_mark: [format_ft_time.py](#ex01-format_ft_time-py) 

<br /><br />

> Ficheros ex02
>
> - :white_check_mark: [find_ft_type.py](#ex02-find_ft_type-py) 

<br /><br />

> Ficheros ex03
>
> - :white_check_mark: [NULL_not_found.py](#ex03-null_not_found-py) 

<br /><br />

> Ficheros ex04
>
> - :white_check_mark: [whatis.py](#ex04-whatis-py) 

<br /><br />

> Ficheros ex05
>
> - :white_check_mark: [Hello.py](#ex00-hello-py) 

<br /><br />

> Ficheros ex06
>
> - :white_check_mark: [Hello.py](#ex00-hello-py) 

<br /><br />

> Ficheros ex07
>
> - :white_check_mark: [Hello.py](#ex00-hello-py) 

<br /><br />

> Ficheros ex08
>
> - :white_check_mark: [Hello.py](#ex00-hello-py) 

<br /><br />

> Ficheros ex09
>
> - :white_check_mark: [Hello.py](#ex00-hello-py) 

<br /><br /><br /><br />

## <h2>Subject English</h2>

<h3>General rules</h3>

- You have to render your modules from a computer in the cluster either using a virtual machine:
    - You can choose the operating system to use for your virtual machine
    - Your virtual machine must have all the necessary software to realize your project. This software must be configured and installed.
- Or you can use the computer directly in case the tools are available.
    - Make sure you have the space on your session to install what you need for all the modules (use the goinfre if your campus has it)
    - You must have everything installed before the evaluations
- Your functions should not quit unexpectedly (segmentation fault, bus error, double free, etc) apart from undefined behaviors. If this happens, your project will be considered non functional and will receive a 0 during the evaluation.
- We encourage you to create test programs for your project even though this work **won’t have to be submitted and won’t be graded**. It will give you a chance to easily test your work and your peers’ work. You will find those tests especially useful during your defence. Indeed, during defence, you are free to use your tests and/or the tests of the peer you are evaluating.
- Submit your work to your assigned git repository. Only the work in the git repository will be graded. If Deepthought is assigned to grade your work, it will be done after your  peer-evaluations. If an error happens in any section of your work during Deepthought’s grading, the evaluation will stop.
- You must use the Python 3.10 version
- You can use any built-in function if it is not prohibited in the exercise.
- Your lib imports must be explicit, for example you must "import numpy as np". Importing "from pandas import *" is not allowed, and you will get 0 on the exercise.
- There is no global variable.
- By Odin, by Thor! Use your brain!!!

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Exercise 00: First python script</h3>

Turn-in directory : ex00/<br />
Files to turn in : Hello.py<br />
Allowed functions : None<br />

You need to modify the string of each data object to display the following greetings:
"Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello «name of your campus»"

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Expected output:

```python
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 01: First use of package</h3>

Turn-in directory : ex01/<br />
Files to turn in : format_ft_time.py<br />
Allowed functions : time, datetime or any other library that allows to
receive the date<br />

Write a script that formats the dates this way, of course your date will not be mine as in the example but it must be formatted the same.

Expected output:

```python
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 02: First function python</h3>

Turn-in directory : ex02/<br />
Files to turn in : find_ft_type.py<br />
Allowed functions : None<br />

Write a function that prints the object types and returns 42.

Here’s how it should be prototyped:

```python
def all_thing_is_obj(object: any) -> int:
#your code here
```

Your tester.py:

```python
from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

Expected output:

```python
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

```
Running your function alone does nothing.
```

Expected output:

```python
$>python find_ft_type.py | cat -e
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 03: NULL not found</h3>

Turn-in directory : ex03/<br />
Files to turn in : NULL_not_found.py<br />
Allowed functions : None<br />

Write a function that prints the object type of all types of "Null".
Return 0 if it goes well and 1 in case of error.
Your function needs to print all types of NULL.

Here’s how it should be prototyped:

```python
def NULL_not_found(object: any) -> int:
#your code here
```

Your tester.py:

```python
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ’’
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
```

```
Empty = ”
```

Expected output:

```python
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

```
Running your function alone does nothing.
```

Expected output:

```python
$>python NULL_not_found.py | cat -e
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 04: The Even and the Odd</h3>

Turn-in directory : ex04/<br />
Files to turn in : whatis.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

Create a script that takes a number as argument, checks whether it is odd or even, and prints the result.

If more than one argument is provided or if the argument is not an integer, print an **AssertionError**.

Expected output:

```python
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 05: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 06: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 07: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 08: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 09: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

## <h2>Subject Castellano</h2>

<h3>Reglas generales</h3>

- Debes renderizar tus módulos desde una computadora en el cluster usando una máquina virtual:
    - Puedes elegir el sistema operativo que usarás para tu máquina virtual
    - Tu máquina virtual debe tener todo el software necesario para realizar tu proyecto. Este software debe estar configurado e instalado.
- O puedes usar la computadora directamente en caso de que las herramientas estén disponibles.
    - Asegúrate de tener el espacio en tu sesión para instalar lo que necesitas para todos los módulos (usa goinfre si tu campus lo tiene)
    - Debes tener todo instalado antes de las evaluaciones
- Tus funciones no deben cerrarse inesperadamente (error de segmentación, error de bus, doble liberación, etc.) además de comportamientos indefinidos. Si esto sucede, tu proyecto se considerará no funcional y recibirá un 0 durante la evaluación.
- Te alentamos a crear programas de prueba para tu proyecto, aunque este trabajo **no tendrá que ser entregado y no será calificado**. Te dará la oportunidad de probar fácilmente tu trabajo y el de tus compañeros. Encontrarás esas pruebas especialmente útiles durante tu defensa. De hecho, durante la defensa, eres libre de usar tus pruebas y/o las pruebas del compañero que estás evaluando.
- Envía tu trabajo al repositorio git que se te haya asignado. Solo se calificará el trabajo en el repositorio git. Si se le asigna a Deepthought la calificación de tu trabajo, se hará después de las evaluaciones de tus compañeros. Si ocurre un error en cualquier sección de tu trabajo durante la calificación de Deepthought, la evaluación se detendrá.
- Debes usar la versión Python 3.10
- Puedes usar cualquier función incorporada si no está prohibida en el ejercicio.
- Tus importaciones de biblioteca deben ser explícitas, por ejemplo, debes "importar numpy como np". Importar "desde pandas import *" no está permitido y obtendrás 0 en el ejercicio.
- No hay ninguna variable global.
- ¡Por Odin, por Thor! ¡Usa tu cerebro!

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **subir** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Exercise 00: First python script</h3>

Turn-in directory : ex00/<br />
Files to turn in : Hello.py<br />
Allowed functions : None<br />

Debes modificar la cadena de cada objeto de datos para mostrar los siguientes saludos:
"Hola mundo", "Hola «país de tu campus»", "Hola «ciudad de tu campus»", "Hola «nombre de tu campus»"

```python
ft_list = ["Hola", "tata!"]
ft_tuple = ("Hola", "toto!")
ft_set = {"Hola", "tutu!"}
ft_dict = {"Hola" : "titi!"}

#tu código aquí

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Salida esperada:

```python
$>python Hello.py | cat -e
['Hola', '¡Mundo!']$
('Hola', '¡Francia!')$
{'Hola', '¡París!'}$
{'Hola': '42¡París!'}$
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 01: First use of package</h3>

Turn-in directory : ex01/<br />
Files to turn in : format_ft_time.py<br />
Allowed functions : time, datetime or any other library that allows to
receive the date<br />

Escribe un script que formatee las fechas de esta manera, por supuesto tu fecha no será la mía como en el ejemplo pero debe tener el mismo formato.

Resultado esperado:

```python
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 02: First function python</h3>

Turn-in directory : ex02/<br />
Files to turn in : find_ft_type.py<br />
Allowed functions : None<br />

Escribe una función que imprima los tipos de objetos y devuelva 42.

Así es como debería crearse el prototipo:

```python
def all_thing_is_obj(object: any) -> int:
#your code here
```

Tu tester.py:

```python
from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

Resultado esperado:

```python
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

```
Ejecutar la función por sí sola no hace nada.
```

Resultado esperado:

```python
$>python find_ft_type.py | cat -e
$>
```
<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 03: NULL not found</h3>

Turn-in directory : ex03/<br />
Files to turn in : NULL_not_found.py<br />
Allowed functions : None<br />

Escriba una función que imprima el tipo de objeto de todos los tipos de "Null".
Devuelva 0 si todo va bien y 1 en caso de error.
Su función debe imprimir todos los tipos de NULL.

Así es como debería crearse el prototipo:

```python
def NULL_not_found(object: any) -> int:
#your code here
```

Tu tester.py:

```python
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ’’
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
```

```
Empty = ”
```

Resultado esperado:

```python
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

```
Ejecutar la función por sí sola no hace nada.
```

Resultado esperado:

```python
$>python NULL_not_found.py | cat -e
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 04: The Even and the Odd</h3>

Turn-in directory : ex04/<br />
Files to turn in : whatis.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

Crear un script que tome un número como argumento, verifique si es par o impar e imprima el resultado.

Si se proporciona más de un argumento o si el argumento no es un entero, imprima un **AssertionError**.

Resultado esperado:

```python
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 05: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 06: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 07: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 08: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 09: XXX</h3>

Turn-in directory : exXXX/<br />
Files to turn in : XXX.py<br />
Allowed functions : None<br />

XXX

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

## <h2>Evaluation</h2>

<h3>Guidelines</h3>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

## <h2>Evaluación</h2>

<h3>Pautas</h3>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **subir** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>ex00 hello py</h3>

```python
ft_list  = ["Hello", "tata!"]  # Lista
ft_tuple = ("Hello", "toto!")  # Tupla
ft_set   = {"Hello", "tutu!"}  # Conjunto
ft_dict  = {"Hello" : "titi!"} # Diccionario
#your code here
ft_list[1] = "World!"            # Modifico la lista
ft_tuple = ("Hello", "Bizkaia!") # No se puede modificar la tupla, creo una nueva tupla
ft_set.discard("tutu!")          # Elimino del conjunto
ft_set.add("Urduliz!")           # Agrego al conjunto
ft_dict["Hello"] = "42Urduliz!"  # Modifico la referencia "Hello" del diccionario

print(ft_list)  # Muestro los 4 tipos por pantalla
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>ex01 format_ft_time py</h3>

```python
import time

# Get the current timestamp in seconds since the epoch (January 1, 1970)
current_time = time.time()

# Format the timestamp in scientific notation
scientific_notation = "{:.2e}".format(current_time)

# Format the timestamp as a human-readable date string (month, day, year)
human_readable_date = time.strftime("%b %d %Y", time.localtime())

# Print the formatted output
print(f"Seconds since January 1, 1970: {current_time:.2f} or {scientific_notation} in scientific notation")
print(human_readable_date)
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>ex02 find_ft_type py</h3>

```python
def all_thing_is_obj(object: any) -> int:
    # Diccionario llamado type_names que mapea tipos de datos built-in a cadenas descriptivas    
    type_names = {                          
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    object_type = type(object)
    # Se intenta obtener un nombre descriptivo para el tipo de objeto usando el diccionario type_names. 
    # Si no se encuentra, se asigna "Type not found" a type_name                   
    type_name = type_names.get(object_type, "Type not found")

    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name != "Type not found":
        print(f"{type_name} : {object_type}")
    else:
        print(f"{type_name}")

    return 42

'''    tester.py
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

print(all_thing_is_obj(10))
'''
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>ex03 null_not_found py</h3>

```python
import math                                                # Libreria que proporciona funciones matemáticas (isnan)

def NULL_not_found(object: any) -> int:                    # Esta función identifica y clasifica diferentes tipos de objetos.
    if object is None:                                     # Si el objeto es exactamente None: Esto identifica claramente los objetos nulos
        type_name = "Nothing"                              # Se asigna el valor "Nothing" a type_name. 
    elif isinstance(object, float) and math.isnan(object): # Si el objeto es un número flotante (float) Y es NaN (Not a Number): Esta condición verifica si el objeto es un número flotante y si además es un valor especial NaN.
        type_name = "Cheese"                               # Se asigna el valor "Cheese" a type_name.
    elif isinstance(object, bool):                         # Si el objeto es de tipo booleano (bool): Esto identifica los valores True y False.
        type_name = "Fake"                                 # Se asigna el valor "Fake" a type_name.
    elif object == 0:                                      # Si el objeto es exactamente igual a 0: Esto identifica el número cero.
        type_name = "Zero"                                 # Se asigna el valor "Zero" a type_name.
    elif object == '':                                     # Si el objeto es una cadena vacía: Esto identifica cadenas vacías.
        type_name = "Empty"                                # Se asigna el valor "Empty" a type_name 
    else:                                                  # Si no se encuentra una coincidencia
        print("Type not Found")                            # Imprimo "Type not Found"
        return 1                                           
    print(f"{type_name}: {object} {type(object)}")         # Imprimo el nombre del tipo, el objeto y su tipo real
    return 0

'''  tester.py
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
'''
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>ex04 whatis py</h3>

```python
import sys                        # Se utiliza para acceder a los argumentos de línea de comandos pasados al script

def is_event(number):             # Esta función toma un número como entrada y determina si es par o impar
  if number % 2 == 0:             # Si el número dividido por 2 tiene resto 0 (es decir, es divisible por 2 por lo tanto par)
    return "I'm Even."
  else:
    return "I'm Odd."    

if __name__ == "__main__":        # Este bloque de código se ejecuta cuando el script se ejecuta directamente, no cuando se importa como módulo.
    try:                          # El bloque try-except maneja posibles errores
      if len(sys.argv) == 2:      # Si se ha proporcionado exactamente un argumento (además del nombre del script)
        number = int(sys.argv[1]) # Convierto el segundo argumento (índice 1 en sys.argv) a un entero
        print(is_event(number))
      elif len(sys.argv) > 2:     # Si se han proporcionado más de un argumento, muestra un mensaje de error indicando que solo se permite un argumento
        print("AssertionError: more than one argument is provided")
      else:                       # Si no se ha proporcionado ningún argumento, no hace nada 
        print("")
    except ValueError:            # Si ocurre un ValueError, significa que el argumento no se pudo convertir a un entero
      print("AssertionError: argument is not an integer")
    except AssertionError as e:   # Si ocurre una AssertionError, se imprime el mensaje de error original.
      print(e) 
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Ex05: XXX</h3>

```python

```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Ex06: XXX</h3>

```python

```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Ex07: XXX</h3>

```python

```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Ex08: XXX</h3>

```python

```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Ex09: XXX</h3>

```python

```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />
