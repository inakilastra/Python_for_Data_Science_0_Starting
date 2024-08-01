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
  