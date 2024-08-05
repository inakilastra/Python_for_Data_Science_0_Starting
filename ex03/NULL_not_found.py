import math


def NULL_not_found(object: any) -> int:
    if object is None:
        type_name = "Nothing"
    elif isinstance(object, float) and math.isnan(object):
        type_name = "Cheese"
    elif isinstance(object, bool):
        type_name = "Fake"
    elif object == 0:
        type_name = "Zero"
    elif object == '':
        type_name = "Empty"
    else:
        print("Type not Found")
        return 1
    print(f"{type_name}: {object} {type(object)}")
    return 0


'''  tester.py
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
'''

'''
# Libreria que proporciona funciones matemáticas (isnan)
import math

# Esta función identifica y clasifica diferentes tipos de objetos.
def NULL_not_found(object: any) -> int:
    # Si el objeto es exactamente None: Esto identifica claramente los
    # objetos nulos
    if object is None:
        # Se asigna el valor "Nothing" a type_name.
        type_name = "Nothing"
    # Si el objeto es un número flotante (float) Y es NaN (Not a Number):
    # Esta condición verifica si el objeto es un número flotante y si además
    # es un valor especial NaN.
    elif isinstance(object, float) and math.isnan(object):
        # Se asigna el valor "Cheese" a type_name.
        type_name = "Cheese"
    # Si el objeto es de tipo booleano (bool):
    # Esto identifica los valores True y False.
    elif isinstance(object, bool):
        # Se asigna el valor "Fake" a type_name.
        type_name = "Fake"
    # Si el objeto es exactamente igual a 0: Esto identifica el número cero.
    elif object == 0:
        # Se asigna el valor "Zero" a type_name.
        type_name = "Zero"
    # Si el objeto es una cadena vacía: Esto identifica cadenas vacías.
    elif object == '':
        # Se asigna el valor "Empty" a type_name
        type_name = "Empty"
    # Si no se encuentra una coincidencia
    else:
        # Imprimo "Type not Found"
        print("Type not Found")
        return 1
    # Imprimo el nombre del tipo, el objeto y su tipo real
    print(f"{type_name}: {object} {type(object)}")
    return 0
'''
