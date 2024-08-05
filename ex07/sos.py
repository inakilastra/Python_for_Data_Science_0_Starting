import sys


MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/", ".": ".-.-.-", ",": "--..--",
    "?": "..--..", "\"": ".-..-."
}


def morse_code(text):
    """Convierte una cadena de texto a código Morse.

    Args:
        text: La cadena de texto a convertir.

    Returns:
        Una cadena con la representación en código Morse.
    """
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE:
            morse_code += MORSE_CODE[char] + " "
        else:
            raise ValueError(f"Character \"{char}\" is not supported.")
    return morse_code.strip()


def main():
    if len(sys.argv) != 2:
        raise AssertionError("Exactly one argument (the text to \
                              convert) is required.")
    if not isinstance(sys.argv[1], str):
        raise TypeError("The argument must be a string.")

    text = sys.argv[1]
    try:
        result = morse_code(text)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

'''
# Importa el módulo sys que proporciona acceso a variables y funciones
# utilizadas o mantenidas por el intérprete de Python.
import sys:

# Defino un diccionario llamado MORSE_CODE que mapea caracteres
# (letras, números, signos de puntuación) a su correspondiente código Morse.
MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/", ".": ".-.-.-", ",": "--..--",
    "?": "..--..", "\"": ".-..-."
}

# Define una función llamada morse_code que toma una cadena de texto como
# entrada y devuelve una cadena con la representación en código Morse.

# Inicializa una cadena vacía morse_code para almacenar el resultado.

# Itera sobre cada carácter char en la cadena de texto convertida a mayúsculas.

# Si el carácter char está presente en el diccionario MORSE_CODE, añade su
# correspondiente código Morse seguido de un espacio a la cadena morse_code.
# Si el carácter char no está en el diccionario, lanza una excepción
# ValueError indicando el carácter no soportado.
# Devuelve la cadena morse_code eliminando los espacios al final
# (utilizando strip()).
def morse_code(text):
    """Convierte una cadena de texto a código Morse.

    Args:
        text: La cadena de texto a convertir.

    Returns:
        Una cadena con la representación en código Morse.
    """
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE:
            morse_code += MORSE_CODE[char] + " "
        else:
            raise ValueError(f"Character \"{char}\" is not supported.")
    return morse_code.strip()

# Define la función principal main del programa.
# Comprueba si el número de argumentos pasados al script es exactamente 2
# (el nombre del script y el texto a convertir). Si no es así, lanza una
# excepción AssertionError.
# Comprueba si el segundo argumento es una cadena. Si no es así, lanza
# una excepción TypeError.
# Asigna el segundo argumento a la variable text.
# Intenta convertir el texto a código Morse utilizando la función morse_code
# y almacena el resultado en result.
# Imprime el resultado.
# Maneja posibles excepciones ValueError lanzadas por la función morse_code
# e imprime un mensaje de error.
def main():
    if len(sys.argv) != 2:
        raise AssertionError("Exactly one argument (the text to \
                              convert) is required.")
    if not isinstance(sys.argv[1], str):
        raise TypeError("The argument must be a string.")

    text = sys.argv[1]
    try:
        result = morse_code(text)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

# Resumen
El código define un diccionario con la equivalencia entre caracteres y
código Morse.
Luego, implementa una función morse_code que convierte una cadena de texto a
código Morse utilizando el diccionario. La función main maneja la entrada del
usuario, llama a la función morse_code y muestra el resultado o un mensaje de
error en caso de errores.

En esencia, el código toma una cadena de texto como entrada, la convierte a
código Morse utilizando un diccionario predefinido y muestra el resultado.
'''
