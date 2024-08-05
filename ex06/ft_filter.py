def ft_filter(function, iterable):
    '''
        Filters elements of an iterable.

        Args:
        function: A function that returns a boolean value.
        iterable: An iterable object.

        Returns:
        A list of elements for which the function returned True.
    '''
    return [item for item in iterable if function(item)]


'''
# Descripción: Esta función actúa como un filtro personalizado para iterables.

# Toma dos argumentos:
    # function: Una función que acepta un elemento del iterable y devuelve un
    # valor booleano (True o False).
    # iterable: Cualquier objeto iterable (como una lista, tupla o cadena) que
    # se desea filtrar.

# Comportamiento:
    Iteración: Recorre cada elemento item del iterable.
    Aplicación: Aplica la función function al elemento actual item.
    Filtrado: Si el resultado de aplicar function a item es True, el elemento
    item se incluye en la nueva lista.
    Retorno: Devuelve la lista de elementos que pasaron el filtro.

# Ejemplo:
    numbers = [1, 2, 3, 4, 5]

    def is_even(num):
        return num % 2 == 0

    even_numbers = ft_filter(is_even, numbers)
    print(even_numbers)  # Output: [2, 4]

En este ejemplo:

numbers es el iterable.
is_even es la función que determina si un número es par.
ft_filter devuelve una nueva lista con los números pares.

# Resumen:

La función ft_filter proporciona una forma flexible de filtrar elementos de un
iterable basado en una condición definida por la función function.
Utiliza una comprensión de lista para crear eficientemente la lista filtrada.
'''
