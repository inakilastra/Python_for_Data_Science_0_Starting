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