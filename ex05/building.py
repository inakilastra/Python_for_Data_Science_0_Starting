import sys
from collections import Counter


def count_chars(text):
    '''
    Counts the occurrences of different character types in a string.

    Args:
        text: The string to analyze.

    Returns:
        A dictionary where keys are character types ("upper", "lower",
        "punctuation", "digit", "space") and values are their counts.
    '''
    char_counts = Counter()
    for char in text:
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
    try:
        if len(sys.argv) == 1:
            print("What is the text to count? Press Ctrl+D to end input.")
            text = sys.stdin.read()
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("Only one argument is allowed.")
            return
    except AssertionError as error:
        print("AssertionError:", error)
        return

    char_counts = count_chars(text)
    total_chars = sum(char_counts.values())

    print(f"The text contains {total_chars} characters:")
    print(f"{char_counts['upper']} upper letter \
          {'s' if char_counts['upper'] != 1 else ''}")
    print(f"{char_counts['lower']} lower letter \
          {'s' if char_counts['lower'] != 1 else ''}")
    print(f"{char_counts['punctuation']} punctuation mark \
          {'s' if char_counts['punctuation'] != 1 else ''}")
    print(f"{char_counts['space']} space \
          {'s' if char_counts['space'] != 1 else ''}")
    print(f"{char_counts['digit']} digit \
          {'s' if char_counts['digit'] != 1 else ''}")


if __name__ == "__main__":
    main()

'''
# Proporciona acceso a variables y funciones del sistema operativo, como
# argumentos en la línea de comandos
import sys

# Importa la clase Counter del módulo collections que permite crear
# contadores de elementos en una colección (como una cadena de texto).
from collections import Counter

# Función que recibe un argumento text (que será la cadena de texto a analizar)
def count_chars(text):
    Counts the occurrences of different character types in a string.

    Args:
        text: The string to analyze.

    Returns:
        A dictionary where keys are character types ("upper", "lower",
        "punctuation", "digit", "space") and values are their counts.
# Crea un objeto char_counts de la clase Counter. Este objeto actuará como
# un diccionario donde se guardarán el conteo de cada tipo de carácter.
char_counts = Counter()

# Recorre cada carácter individual (char) en la cadena text.
# incrementados los contadores en función del tipo de caracter
for char in text:
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
    # El bloque try-except maneja posibles errores
    try:
        # Si no hay argumentos, se imprime un mensaje indicando que el usuario
        # debe introducir el texto y presionar Ctrl+D para finalizar
        if len(sys.argv) == 1:
            print("What is the text to count? Press Ctrl+D to end input.")
            # Lee toda la entrada incluyendo retornos de carro
            text = sys.stdin.read()
        # Si se ha proporcionado exactamente un argumento
        elif len(sys.argv) == 2:
            # Se asigna el argumento
            text = sys.argv[1]
        # Si se han proporcionado más de un argumento, muestra un mensaje de
        # error indicando que solo se permite un argumento
        else:
            print("Only one argument is allowed.")
            return
    # Si ocurre una AssertionError, se imprime el mensaje de error original.
    except AssertionError as error:
        print("AssertionError:", error)
        return

    # Llama a la función count_chars para obtener el conteo de caracteres.
    char_counts = count_chars(text)
    # Calcula el total de caracteres sumando los valores de todas las claves
    # en el diccionario char_counts.
    total_chars = sum(char_counts.values())

    print(f"The text contains {total_chars} characters:")
    print(f"{char_counts['upper']} upper letter \
          {'s' if char_counts['upper'] != 1 else ''}")
    print(f"{char_counts['lower']} lower letter \
          {'s' if char_counts['lower'] != 1 else ''}")
    print(f"{char_counts['punctuation']} punctuation mark \
          {'s' if char_counts['punctuation'] != 1 else ''}")
    print(f"{char_counts['space']} space \
          {'s' if char_counts['space'] != 1 else ''}")
    print(f"{char_counts['digit']} digit \
          {'s' if char_counts['digit'] != 1 else ''}")


if __name__ == "__main__":
    main()

# Resumen
# Este código analiza un texto y cuenta la ocurrencia de diferentes tipos de
# caracteres (mayúsculas, minúsculas, dígitos, espacios y puntuación).
# Muestra el conteo total de caracteres y un desglose de cada tipo.
'''
