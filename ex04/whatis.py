import sys


def is_event(number):
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            number = int(sys.argv[1])
            print(is_event(number))
        elif len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
        else:
            print("")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(e)

'''
# Se utiliza para acceder a los argumentos de línea de comandos pasados
import sys

# Esta función toma un número como entrada y determina si es par o impar
def is_event(number):
  # Si el número dividido por 2 tiene resto 0 (es decir,
  # es divisible por 2 por lo tanto par)
  if number % 2 == 0:
    return "I'm Even."
  else:
    return "I'm Odd."


# Este bloque de código se ejecuta cuando el script se ejecuta directamente,
# no cuando se importa como módulo.
if __name__ == "__main__":
    # El bloque try-except maneja posibles errores
    try:
      # Si se ha proporcionado exactamente un argumento
      if len(sys.argv) == 2:
        # Convierto el segundo argumento (índice 1 en sys.argv) a un entero
        number = int(sys.argv[1])
        print(is_event(number))
      # Si se han proporcionado más de un argumento, muestra un mensaje de
      # error indicando que solo se permite un argumento
      elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
      # Si no se ha proporcionado ningún argumento, no hace nada
      else:
        print("")
    # Si ocurre un ValueError, significa que el argumento no se pudo
    # convertir a un entero
    except ValueError:
      print("AssertionError: argument is not an integer")
    # Si ocurre una AssertionError, se imprime el mensaje de error original.
    except AssertionError as e:
      print(e)
'''
