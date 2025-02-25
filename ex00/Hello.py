"""
Ejercicio 00: Primer script de Python

Este script modifica las siguientes estructuras de datos para mostrar saludos específicos:
- Lista: ft_list
- Tupla: ft_tuple
- Conjunto: ft_set
- Diccionario: ft_dict

Objetivo: Modificar las cadenas de texto dentro de cada estructura para
         mostrar los saludos esperados según el enunciado del ejercicio.
"""

# 1. Definición de la lista inicial llamada 'ft_list'
#    Contiene dos elementos de tipo cadena de texto: "Hello" y "tata!"
ft_list = ["Hello", "tata!"]  # Lista inicial

# 2. Definición de la tupla inicial llamada 'ft_tuple'
#    Contiene dos elementos de tipo cadena de texto: "Hello" y "toto!"
#    Las tuplas son inmutables, no se pueden modificar directamente sus elementos
ft_tuple = ("Hello", "toto!") # Tupla inicial

# 3. Definición del conjunto inicial llamado 'ft_set'
#    Contiene dos elementos de tipo cadena de texto: "Hello" y "tutu!"
#    Los conjuntos son colecciones desordenadas de elementos únicos
ft_set = {"Hello", "tutu!"}   # Conjunto inicial

# 4. Definición del diccionario inicial llamado 'ft_dict'
#    Contiene un par clave-valor: la clave es "Hello" (cadena) y el valor es "titi!" (cadena)
#    Los diccionarios almacenan pares de clave-valor, donde las claves deben ser únicas
ft_dict = {"Hello": "titi!"}  # Diccionario inicial

# 5. Modificando la lista 'ft_list'
#    Las listas son mutables, podemos cambiar sus elementos directamente
#    Accedemos al segundo elemento de la lista (índice 1, recordando que el índice empieza en 0)
#    y le asignamos el nuevo valor "World!"
ft_list[1] = "World!"

# 6. Modificando la tupla 'ft_tuple' (de forma indirecta)
#    Como las tuplas son inmutables, no podemos modificar directamente ft_tuple[1]
#    Para modificarla, seguimos estos pasos:
#    a) Convertimos la tupla 'ft_tuple' a una lista temporal llamada 'temp_list'
#       Usamos la función list() para hacer la conversión
temp_list = list(ft_tuple)
#    b) Modificamos el segundo elemento de la lista 'temp_list' (índice 1)
#       Le asignamos el nuevo valor "Bizkaia!"
temp_list[1] = "Bizkaia!"
#    c) Convertimos la lista modificada 'temp_list' de vuelta a una tupla
#       y la asignamos de nuevo a la variable 'ft_tuple'
#       Usamos la función tuple() para hacer la conversión
ft_tuple = tuple(temp_list)

# 7. Modificando el conjunto 'ft_set'
#    Para modificar un conjunto, podemos eliminar elementos existentes y agregar nuevos
#    a) Eliminamos el elemento "tutu!" del conjunto 'ft_set'
#       Usamos el método discard() para eliminar un elemento (si existe) del conjunto
ft_set.discard("tutu!")
#    b) Agregamos el nuevo elemento "Urduliz!" al conjunto 'ft_set'
#       Usamos el método add() para añadir un nuevo elemento al conjunto
ft_set.add("Urduliz!")

# 8. Modificando el diccionario 'ft_dict'
#    Los diccionarios son mutables, podemos cambiar los valores asociados a las claves
#    Accedemos al valor asociado a la clave "Hello" en el diccionario 'ft_dict'
#    y le asignamos el nuevo valor "42Urduliz!"
ft_dict["Hello"] = "42Urduliz!"

# 9. Imprimiendo las estructuras de datos modificadas
#    Usamos la función print() para mostrar en la consola el contenido de cada estructura
#    Cada print() mostrará una estructura diferente en una línea separada
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)