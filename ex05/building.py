#!/usr/bin/env python3
"""
Ejercicio 05: Contador de Tipos de Caracteres

Este script recibe una cadena de texto como argumento o, si no se proporciona
ningún argumento, solicita al usuario que introduzca una cadena.
Luego, analiza la cadena y cuenta la cantidad de caracteres en mayúsculas,
minúsculas, signos de puntuación, dígitos y espacios. Finalmente, muestra los
resultados del conteo.

Si se proporciona más de un argumento en la línea de comandos, se lanza una
excepción de tipo AssertionError.

Nombre del archivo: building.py
Funciones permitidas: sys, collections

Salida esperada: (Ver enunciado del ejercicio)
"""

import sys
from collections import Counter


def count_chars(text: str) -> dict:
    """
    Cuenta las ocurrencias de diferentes tipos de caracteres en una cadena.

    Esta función toma una cadena de texto como entrada y cuenta la cantidad
    de caracteres en mayúsculas, minúsculas, dígitos, espacios y signos de
    puntuación.

    Args:
        text (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario donde las claves son los tipos de caracteres
              ("upper", "lower", "punctuation", "digit", "space") y los
              valores son sus respectivas cantidades.
    """
    # Se crea un objeto Counter que actuará como un diccionario
    # para almacenar los conteos de cada tipo de carácter.
    char_counts = Counter()
    # Se itera sobre cada carácter de la cadena de texto.
    for char in text:
        # Si el caracter está en mayúsculas.
        if char.isupper():
            char_counts["upper"] += 1  # Se incrementa el contador de "upper".
        # Si el carácter está en minúsculas.
        elif char.islower():
            char_counts["lower"] += 1  # Se incrementa el contador de "lower".
        # Si el carácter es un dígito.
        elif char.isdigit():
            char_counts["digit"] += 1  # Se incrementa el contador de "digit".
        # Si el carácter es un espacio.
        elif char.isspace():
            char_counts["space"] += 1  # Se incrementa el contador de "space".
        # Si no es ninguno de los anteriores, es un signo de puntuación.
        else:
            char_counts["punctuation"] += 1  # Se incrementa el contador.
    # Se devuelve el diccionario con los conteos de caracteres.
    return char_counts


def pluralize(count: int, word: str) -> str:
    """
    Añade una 's' a una palabra si el contador es distinto de 1.

    Esta función se utiliza para gestionar la pluralización de palabras en
    la salida del programa, añadiendo una 's' al final de la palabra si la
    cantidad (count) es diferente de 1.

    Args:
        count (int): La cantidad de elementos.
        word (str): La palabra a pluralizar potencialmente.

    Returns:
        str: La palabra con o sin 's' al final, dependiendo de count.
    """
    # Si el contador es diferente de 1, añade una "s" a la palabra.
    return f"{word}{'s' if count != 1 else ''}"


def main():
    """
    Función principal del programa.

    Esta función gestiona la entrada del usuario, realiza el conteo de
    caracteres y muestra los resultados.

    Si no se proporciona ningún argumento en la línea de comandos, se solicita
    al usuario que introduzca una cadena de texto. Si se proporciona un
    argumento, se utiliza como la cadena de entrada. Si se proporcionan más
    de un argumento, se lanza una excepción AssertionError.
    """
    # Se utiliza un bloque try-except para manejar la excepción AssertionError.
    try:
        # 1. Comprobar la cantidad de argumentos en la linea de comandos
        # Si no hay argumentos.
        if len(sys.argv) == 1:
            # Se solicita al usuario que introduzca una cadena.
            print("What is the text to count?")
            # Se lee la entrada del usuario.
            text = sys.stdin.read()
        # Si hay exactamente 2 argumentos (el nombre del script y uno mas).
        elif len(sys.argv) == 2:
            # El segundo argumento es el texto que se va a analizar.
            text = sys.argv[1]
        # Si hay más de 2 argumentos.
        else:
            # Se lanza un error porque solo se permite un argumento.
            raise AssertionError("Only one argument is allowed.")
    # Si se lanza la excepción AssertionError.
    except AssertionError as error:
        # Se imprime el mensaje de error.
        print("AssertionError:", error)
        # Se sale de la funcion, con lo que el programa termina.
        return

    # 2. Contar los caracteres en el texto de entrada.
    # Se llama a la función count_chars para contar los caracteres.
    char_counts = count_chars(text)
    # Se suman todos los valores del contador para obtener el total
    total_chars = sum(char_counts.values())

    # 3. Imprimir los resultados.
    # Se imprime el total de caracteres.
    print(f"The text contains {total_chars} characters:")
    # Se imprime el conteo de letras mayúsculas.
    print(f"{char_counts['upper']} {pluralize(char_counts['upper'], 'upper letter')}")
    # Se imprime el conteo de letras minúsculas.
    print(f"{char_counts['lower']} {pluralize(char_counts['lower'], 'lower letter')}")
    print(f"{char_counts['punctuation']} {pluralize(char_counts['punctuation'], 'punctuation mark')}")
    print(f"{char_counts['space']} {pluralize(char_counts['space'], 'space')}")
    print(f"{char_counts['digit']} {pluralize(char_counts['digit'], 'digit')}")

if __name__ == "__main__":
    main()

'''    
import sys
from collections import Counter


def count_chars(text: str) -> dict:
    """
    Cuenta las ocurrencias de diferentes tipos de caracteres en una cadena.

    Esta función toma una cadena de texto como entrada y cuenta la cantidad
    de caracteres en mayúsculas, minúsculas, dígitos, espacios y signos de
    puntuación.

    Args:
        text (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario donde las claves son los tipos de caracteres
              ("upper", "lower", "punctuation", "digit", "space") y los
              valores son sus respectivas cantidades.
    """
    # Se crea un objeto Counter que actuará como un diccionario
    # para almacenar los conteos de cada tipo de carácter.
    char_counts = Counter()
    # Se itera sobre cada carácter de la cadena de texto.
    for char in text:
        # Si el caracter está en mayúsculas.
        if char.isupper():
            char_counts["upper"] += 1  # Se incrementa el contador de "upper".
        # Si el carácter está en minúsculas.
        elif char.islower():
            char_counts["lower"] += 1  # Se incrementa el contador de "lower".
        # Si el carácter es un dígito.
        elif char.isdigit():
            char_counts["digit"] += 1  # Se incrementa el contador de "digit".
        # Si el carácter es un espacio.
        elif char.isspace():
            char_counts["space"] += 1  # Se incrementa el contador de "space".
        # Si no es ninguno de los anteriores, es un signo de puntuación.
        else:
            char_counts["punctuation"] += 1  # Se incrementa el contador.
    # Se devuelve el diccionario con los conteos de caracteres.
    return char_counts


def pluralize(count: int, word: str) -> str:
    """
    Añade una 's' a una palabra si el contador es distinto de 1.

    Esta función se utiliza para gestionar la pluralización de palabras en
    la salida del programa, añadiendo una 's' al final de la palabra si la
    cantidad (count) es diferente de 1.

    Args:
        count (int): La cantidad de elementos.
        word (str): La palabra a pluralizar potencialmente.

    Returns:
        str: La palabra con o sin 's' al final, dependiendo de count.
    """
    # Si el contador es diferente de 1, añade una "s" a la palabra.
    return f"{word}{'s' if count != 1 else ''}"


def main():
    """
    Función principal del programa.

    Esta función gestiona la entrada del usuario, realiza el conteo de
    caracteres y muestra los resultados.

    Si no se proporciona ningún argumento en la línea de comandos, se solicita
    al usuario que introduzca una cadena de texto. Si se proporciona un
    argumento, se utiliza como la cadena de entrada. Si se proporcionan más
    de un argumento, se lanza una excepción AssertionError.
    """
    # Se utiliza un bloque try-except para manejar la excepción AssertionError.
    try:
        # 1. Comprobar la cantidad de argumentos en la linea de comandos
        # Si no hay argumentos.
        if len(sys.argv) == 1:
            # Se solicita al usuario que introduzca una cadena.
            print("What is the text to count?")
            # Se lee la entrada del usuario.
            text = sys.stdin.read()
        # Si hay exactamente 2 argumentos (el nombre del script y uno mas).
        elif len(sys.argv) == 2:
            # El segundo argumento es el texto que se va a analizar.
            text = sys.argv[1]
        # Si hay más de 2 argumentos.
        else:
            # Se lanza un error porque solo se permite un argumento.
            raise AssertionError("Only one argument is allowed.")
    # Si se lanza la excepción AssertionError.
    except AssertionError as error:
        # Se imprime el mensaje de error.
        print("AssertionError:", error)
        # Se sale de la funcion, con lo que el programa termina.
        return

    # 2. Contar los caracteres en el texto de entrada.
    # Se llama a la función count_chars para contar los caracteres.
    char_counts = count_chars(text)
    # Se suman todos los valores del contador para obtener el total
    total_chars = sum(char_counts.values())

    # 3. Imprimir los resultados.
    # Se imprime el total de caracteres.
    print(f"The text contains {total_chars} characters:")
    # Se imprime el conteo de letras mayúsculas.
    print(f"{char_counts['upper']} {pluralize(char_counts['upper'], 'upper letter')}")
    # Se imprime el conteo de letras minúsculas.
    print(f"{char_counts['lower']} {pluralize(char_counts['lower'], 'lower letter')}")
    # Se imprime el conteo de signos de puntuación.
    print(f"{char_counts['punctuation']} {pluralize(char_counts['punctuation'], 'punctuation mark')}")
    # Se imprime el conteo de espacios.
    print(f"{char_counts['space']} {pluralize(char_counts['space'], 'space')}")
    # Se imprime el conteo de dígitos.
    print(f"{char_counts['digit']} {pluralize(char_counts['digit'], 'digit')}")


# El bloque if __name__ == "__main__": se ejecuta solo cuando el script
# se ejecuta directamente (no cuando se importa como un módulo).
if __name__ == "__main__":
    # Se llama a la función principal.
    main()
'''