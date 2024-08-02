# Python for Data Science

<h1>0 - Starting</h1>

<br />

> Otros Lenguajes
>
> - [English](https://github.com/inakilastra/Python_for_Data_Science_0_Starting/blob/main/README.md)

<br /><br />

>
> - :white_check_mark: [Subject](#subject)
>
>   - :white_check_mark: [Exercise 00 First python script](#exercise-00-first-python-script)
>
>   - :white_check_mark: [Exercise 01: First use of package](#exercise-01-first-use-of-package)
>
>   - :white_check_mark: [Exercise 02 First function python](#exercise-02-first-function-python)
>
>   - :white_check_mark: [Exercise 03 NULL not found](#exercise-03-null-not-found)
>
>   - :white_check_mark: [Exercise 04 The Even and the Odd](#exercise-04-the-even-and-the-odd)
>
>   - :white_check_mark: [A partir de ahora debes seguir estas reglas adicionales](#a-partir-de-ahora-debes-seguir-estas-reglas-adicionales)
>
>   - :white_check_mark: [Exercise 05 First standalone program python](#exercise-05-first-standalone-program-python)
>
>   - :white_check_mark: [Exercise 06](#exercise-06)
>
>   - :white_check_mark: [Exercise 07 Dictionaries SoS](#exercise-07-dictionaries-sos)
>
>   - :white_check_mark: [Exercise 08 Loading ...](#exercise-08-loading-...)
>
>   - :white_check_mark: [Exercise 09 My first package creation](#exercise-09-my-first-package-creation)

<br /><br />

>
> - :white_check_mark: [Evaluation](#evaluation)

<br /><br /><br /><br />

## <h2>Subject</h2>

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

### <h3>Exercise 00 First python script</h3>

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

### <h3>Exercise 01 First use of package</h3>

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

### <h3>Exercise 02 First function python</h3>

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

### <h3>Exercise 03 NULL not found</h3>

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

### <h3>Exercise 04 The Even and the Odd</h3>

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

### <h3>A partir de ahora debes seguir estas reglas adicionales</h3>

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

### <h3>Exercise 05 First standalone program python</h3>

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

### <h3>Exercise 06</h3>

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

### <h3>Exercise 07 Dictionaries SoS</h3>

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

### <h3>Exercise 08 Loading ...</h3>

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

### <h3>Exercise 09 My first package creation</h3>

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
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **subir** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

## <h2>Evaluation</h2>

<h3>Pautas</h3>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **subir** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />
