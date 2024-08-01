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
> - :white_check_mark: [building.py](#ex05-building-py) 

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

<h3>From now on you must follow these additional rules</h3>

- No code in the global scope. Use functions!
- Each program must have its main and not be a simple script:

```python
def main():
# your tests and your error handling
if __name__ == "__main__":
main()
```

- Any exception not caught will invalidate the exercices, even in the event of an error
that you were asked to test.
- All your functions must have a documentation (__doc__)
- Your code must be at the norm
    - pip install flake8
    - alias norminette=flake8


***The following note is not from the subject, it is my interpretation***
Example of code following the new rules

```python
def my_function(argument):
"""This function does something with an argument.

Args:
argument: A value of any type.

Returns:
The result of the operation.
"""
# Function code

def main():
try:
result = my_function(value)
except Exception as e:
print(f"Error: {e}")

if __name__ == "__main__":
main()
```    

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 05: First standalone program python</h3>

Turn-in directory : ex05/<br />
Files to turn in : building.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

This time you have to make a real autonomous program, with a main, which takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits and spaces.

- If None or nothing is provided, the user is prompted to provide a string.
- If more than one argument is provided to the program, print an AssertionError.

Expected outputs:

```python
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```

Expected outputs: (the carriage return counts as a space, if you don’t want to return
one use ctrl + D)

```python
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

```
By Odin, by Thor ! Use your brain !!! Don’t reinvent the wheel, use
the language features.
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 06:</h3>

Turn-in directory : ex06/<br />
Files to turn in : ft_filter.py, filterstring.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

***Part 1: Recode filter function***

Recode your own ft_filter, it should behave like the original built-in function (it should return the same thing as "print(filter.__doc__)"), you should use **list comprehensions** to recode your ft_filter.

```
Of course using the original filter built-in is forbidden
```

```
You can validate the module from here, but we encourage you to
continue as there are things you will need to know for the following
projects
```
***Part 2: The program***

Create a program that accepts two arguments: a string(S), and an integer(N). The
program should output a list of words from **S** that have a length greater than **N**.
- Words are separated from each other by space characters.
- Strings do not contain any special characters. (Punctuation or invisible)
- The program must contain at least one **list comprehension** expression and one **lambda**.
- If the number of argument is different from 2, or if the type of any argument is wrong, the program prints an **AssertionError**.

Expected outputs:

```
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 07: Dictionaries SoS</h3>

Turn-in directory : ex07/<br />
Files to turn in : sos.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

Make a program that takes a string as an argument and encodes it into Morse Code.

- The program supports space and alphanumeric characters
- An alphanumeric character is represented by dots . and dashes -
- Complete morse characters are separated by a single space
- A space character is represented by a slash /

You must use a dictionary to store your morse code.

```
NESTED_MORSE = { " ": "/ ",
"A": ".- ",
...
```

If the number of arguments is different from 1, or if the type of any argument is wrong, the program prints an **AssertionError**.

```
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 08: Loading ...</h3>

Turn-in directory : ex08/<br />
Files to turn in : Loading.py<br />
Allowed functions : None<br />

So let’s create a function called ft_tqdm.
The function must copy the function tqdm with the yield operator.

Here’s how it should be prototyped:

```python
def ft_tqdm(lst: range) -> None:
#your code here
```

Your tester.py: (you compare your version with the original)

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(333)):
sleep(0.005)
print()
for elem in tqdm(range(333)):
sleep(0.005)
print()
```

Expected output: (you must have a function as close as possible to the original version)

```python
$> python tester.py
100%|[===============================================================>]| 333/333
100%|                                                                  | 333/333 [00:01<00:00, 191.61it/s]
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 09: My first package creation</h3>

Turn-in directory : ex09/<br />
Files to turn in : *.py, *.txt, *.toml, README.md, LICENSE<br />
Allowed functions : PyPI or any library for creation package<br />

Create your first package in python the way you want, it will appear in the list of installed packages when you type the command "pip list" and display its characteristics when you type "pip show -v ft_package"

```python
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

The package will be installed via pip using one of the following commands (both should work):
- pip install ./dist/ft_package-0.0.1.tar.gz
- pip install ./dist/ft_package-0.0.1-py3-none-any.whl

Your package must be able to be called from a script like this one:

```python
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

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

<h3>A partir de ahora debes seguir estas reglas adicionales</h3>

- No hay código en el ámbito global. ¡Usa funciones!
- Cada programa debe tener su main y no ser un simple script:

```python
def main():
# your tests and your error handling
if __name__ == "__main__":
main()
```

- Cualquier excepción no capturada invalidará los ejercicios, incluso en el caso de un error que se te pidió que probaras.
- Todas tus funciones deben tener una documentación (__doc__)
- Tu código debe estar en la norma
- pip install flake8
- alias norminette=flake8

***El siguiente apunte no es del subject, es mi interpretación***
Ejemplo de código siguiendo las nuevas normas

```python
def mi_funcion(argumento):
  """Esta función hace algo con un argumento.

  Args:
    argumento: Un valor de cualquier tipo.

  Returns:
    El resultado de la operación.
  """
  # Código de la función

def main():
  try:
    resultado = mi_funcion(valor)
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
```
<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 05: First standalone program python</h3>

Turn-in directory : ex05/<br />
Files to turn in : building.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

Esta vez tienes que hacer un programa autónomo real, con un main, que toma un único argumento de cadena y muestra las sumas de sus caracteres en mayúsculas, minúsculas, signos de puntuación, dígitos y espacios.

- Si se proporciona None o nada, se le solicita al usuario que proporcione una cadena.
- Si se proporciona más de un argumento al programa, imprime un AssertionError.

Resultados esperados:

```python
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```

Resultados esperados: (el retorno de carro cuenta como un espacio, si no desea devolver uno, use Ctrl + D)

```python
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

```
¡Por Odín, por Thor! ¡Usa tu cerebro! No reinventes la rueda, utiliza las características del lenguaje.
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 06:</h3>

Turn-in directory : ex06/<br />
Files to turn in : ft_filter.py, filterstring.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

***Parte 1: Recodificar la función de filtro***

Recodifica tu propio ft_filter, debería comportarse como la función incorporada original (debería devolver lo mismo que "print(filter.__doc__)"), deberías usar **comprensiones de listas** para recodificar tu ft_filter.

```
Por supuesto, está prohibido usar el filtro original incorporado
```

```
Puede validar el módulo desde aquí, pero le recomendamos que
continúe ya que hay cosas que necesitará saber para los siguientes
proyectos
```
***Parte 2: El programa***

Cree un programa que acepte dos argumentos: una cadena(S) y un entero(N). El
programa debe generar una lista de palabras de **S** que tengan una longitud mayor que **N**.
- Las palabras están separadas entre sí por caracteres de espacio.
- Las cadenas no contienen ningún carácter especial (puntuación o invisible)
- El programa debe contener al menos una **expresión de comprensión de lista** y una **lambda**.
- Si el número de argumentos es diferente de 2, o si el tipo de algún argumento es incorrecto, el programa imprime un **AssertionError**.

Resultados esperados:

```
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 07: Dictionaries SoS</h3>

Turn-in directory : ex07/<br />
Files to turn in : sos.py<br />
Allowed functions : sys or any other library that allows to receive the args<br />

Realice un programa que tome una cadena como argumento y la codifique en código Morse.

- El programa admite espacios y caracteres alfanuméricos
- Un carácter alfanumérico se representa con puntos . y guiones -
- Los caracteres Morse completos se separan con un solo espacio
- Un carácter de espacio se representa con una barra /

Debe utilizar un diccionario para almacenar su código Morse.

```
NESTED_MORSE = { " ": "/ ",
"A": ".- ",
...
```

Si el número de argumentos es diferente de 1, o si el tipo de algún argumento es incorrecto, el programa imprime un **AssertionError**.

```
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 08: Loading ...</h3>

Turn-in directory : ex08/<br />
Files to turn in : Loading.py<br />
Allowed functions : None<br />

Creemos una función llamada ft_tqdm.
La función debe copiar la función tqdm con el operador yield.

Así es como debería ser el prototipo:

```python
def ft_tqdm(lst: range) -> None:
#your code here
```

Tu tester.py: (comparas tu versión con la original)

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(333)):
sleep(0.005)
print()
for elem in tqdm(range(333)):
sleep(0.005)
print()
```

Resultado esperado: (debes tener una función lo más parecida posible a la versión original)

```python
$> python tester.py
100%|[===============================================================>]| 333/333
100%|                                                                  | 333/333 [00:01<00:00, 191.61it/s]
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

<h3>Exercise 09: My first package creation</h3>

Turn-in directory : ex09/<br />
Files to turn in : *.py, *.txt, *.toml, README.md, LICENSE<br />
Allowed functions : PyPI or any library for creation package<br />

Crea tu primer paquete en Python de la forma que quieras, aparecerá en la lista de paquetes instalados cuando escribas el comando "pip list" y mostrará sus características cuando escribas "pip show -v ft_package"

```python
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

El paquete se instalará a través de pip usando uno de los siguientes comandos (ambos deberían funcionar):
- pip install ./dist/ft_package-0.0.1.tar.gz
- pip install ./dist/ft_package-0.0.1-py3-none-any.whl

Su paquete debe poder ser invocado desde un script como este:

```python
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

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

<h3>ex05 building py</h3>

```python
import sys                      # Proporciona acceso a variables y funciones del sistema operativo, como argumentos en la línea de comandos
from collections import Counter # Importa la clase Counter del módulo collections que permite crear contadores de elementos en una colección (como una cadena de texto).

def count_chars(text):          # Función que recibe un argumento text (que será la cadena de texto a analizar).
    '''
    Counts the occurrences of different character types in a string.

    Args:
        text: The string to analyze.

    Returns:
        A dictionary where keys are character types ("upper", "lower", 
        "punctuation", "digit", "space") and values are their counts.
    '''
    char_counts = Counter()     # Crea un objeto char_counts de la clase Counter. Este objeto actuará como un diccionario donde se guardarán el conteo de cada tipo de carácter.

    for char in text:           # Recorre cada carácter individual (char) en la cadena text.
        if char.isupper():
            char_counts["upper"] += 1
        elif char.islower():
            char_counts["lower"] += 1
        elif char.isdigit():
            char_counts["digit"] += 1
        elif char.isspace():
            char_counts["space"] += 1
        else:
            char_counts["punctuation"] += 1
    return char_counts

def main():
    try:                          # El bloque try-except maneja posibles errores
      if len(sys.argv) == 1:      # Si no hay argumentos, se imprime un mensaje indicando que el usuario debe introducir el texto y presionar Ctrl+D para finalizar
        print("What is the text to count? Press Ctrl+D to end input.")
        text = sys.stdin.read()   # Lee toda la entrada incluyendo retornos de carro
      elif len(sys.argv) == 2:    # Si se ha proporcionado exactamente un argumento (además del nombre del script)        
        text = sys.argv[1]        # Se asigna el argumento 
      else:                       # Si se han proporcionado más de un argumento, muestra un mensaje de error indicando que solo se permite un argumento
        print("Only one argument is allowed.")
        return                    
    except AssertionError as e:   # Si ocurre una AssertionError, se imprime el mensaje de error original.
      print(e) 
      return

    char_counts = count_chars(text)         # Llama a la función count_chars para obtener el conteo de caracteres.
    total_chars = sum(char_counts.values()) # Calcula el total de caracteres sumando los valores de todas las claves en el diccionario char_counts.

    print(f"The text contains {total_chars} characters:")
    print(f"{char_counts['upper']} upper letter{'s' if char_counts['upper'] != 1 else ''}")
    print(f"{char_counts['lower']} lower letter{'s' if char_counts['lower'] != 1 else ''}")
    print(f"{char_counts['punctuation']} punctuation mark{'s' if char_counts['punctuation'] != 1 else ''}")
    print(f"{char_counts['space']} space{'s' if char_counts['space'] != 1 else ''}")
    print(f"{char_counts['digit']} digit{'s' if char_counts['digit'] != 1 else ''}")

if __name__ == "__main__":
    main()
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
