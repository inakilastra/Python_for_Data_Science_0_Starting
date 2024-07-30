import math                                                # Libreria que proporciona funciones matemáticas (isnan)

def NULL_not_found(object: any) -> int:                    # Esta función identifica y clasifica diferentes tipos de objetos.
    if object is None:                                     # Si el objeto es exactamente None: Esto identifica claramente los objetos nulos
        type_name = "Nothing"                              # Se asigna el valor "Nothing" a type_name. 
    elif isinstance(object, float) and math.isnan(object): # Si el objeto es un número flotante (float) Y es NaN (Not a Number): Esta condición verifica si el objeto es un número flotante y si además es un valor especial NaN.
        type_name = "Cheese"                               # Se asigna el valor "Cheese" a type_name.
    elif isinstance(object, bool):                         # Si el objeto es de tipo booleano (bool): Esto identifica los valores True y False.
        type_name = "Fake"                                 # Se asigna el valor "Fake" a type_name.
    elif object == 0:                                      # Si el objeto es exactamente igual a 0: Esto identifica el número cero.
        type_name = "Zero"                                 # Se asigna el valor "Zero" a type_name.
    elif object == '':                                     # Si el objeto es una cadena vacía: Esto identifica cadenas vacías.
        type_name = "Empty"                                # Se asigna el valor "Empty" a type_name 
    else:                                                  # Si no se encuentra una coincidencia
        print("Type not Found")                            # Imprimo "Type not Found"
        return 1                                           
    print(f"{type_name}: {object} {type(object)}")         # Imprimo el nombre del tipo, el objeto y su tipo real
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