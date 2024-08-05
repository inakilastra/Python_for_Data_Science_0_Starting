import sys
from ft_filter import ft_filter


def main():
    '''
        Accepts only 2 arguments:
        1. string
        2. integer

        Args:
        string: A function that returns a boolean value.
        integer: An iterable object.

        Returns:
        A list of elements for which the function returned True.
    '''
    try:
        if len(sys.argv) == 3:
            string = sys.argv[1]
            number = int(sys.argv[2])
            result = ft_filter(lambda word: len(word) > number, string.split())
            print(result)
        else:
            print("AssertionError: Only three arguments is allowed.")
    except ValueError as error:
        print("ValueError:", error)


if __name__ == "__main__":
    main()

'''
# Importa el módulo sys que proporciona acceso a variables y funciones
# utilizadas o mantenidas por el intérprete de Python.
import sys:
# Importa la función ft_filter desde el módulo ft_filter
from ft_filter import ft_filter:


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    # try para manejar posibles errores.
    try:
        # Compruebo si el número de argumentos pasados es exactamente 3
        if len(sys.argv) != 3:
            # Asigno el segundo argumento a la variable string
            string = sys.argv[1]
            # Convierto el tercer argumento a un entero
            # lo asigno a la variable number
            number = int(sys.argv[2])
            # Uso la función ft_filter para filtrar las palabras de la cadena
            # string que tengan una longitud mayor que el número number.
            # La función lambda se usa para definir una función anónima que
            # comprueba la longitud de cada palabra.
            result = ft_filter(lambda word: len(word) > number, string.split())
            # Imprimo la lista de palabras filtradas.
            print(result)
        else:
            # Si el número de argumentos no es igual a 3, muestra un mensaje
            # de error indicando que solo se permiten tres argumentos.
            print("AssertionError: Only three arguments is allowed.")
    # Maneja una posible excepción ValueError que puede ocurrir si el
    # segundo argumento no se puede convertir a un entero.
    # Imprime un mensaje de error con el tipo de error.
    except ValueError as error:
        print("ValueError:", error)


if __name__ == "__main__":
    main()

# Resumen
# El código define una función main que verifica la cantidad de argumentos
# proporcionados al script. Si hay exactamente dos argumentos, convierte el
# segundo argumento a un número entero y utiliza la función ft_filter para
# filtrar las palabras de la primera cadena según su longitud.
# Si hay un error, muestra un mensaje de error apropiado.
'''
