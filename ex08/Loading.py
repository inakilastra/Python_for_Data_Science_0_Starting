import sys


def ft_tqdm(lst: range) -> None:
    """
    Muestra una barra de progreso similar a tqdm para un rango dado.

    Args:
        lst: Un objeto range o cualquier iterable.
    """
    total = len(lst)
    width = 42
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        filled_length = int(width * progress)
        bar = '█' * filled_length + '░' * (width - filled_length)
        sys.stdout.write(f'\r{int(progress * 100)}%|{bar}| {i + 1}/{total}')
        sys.stdout.flush()
        yield item
    sys.stdout.write('\n')


'''
# Importa el módulo sys que proporciona acceso a variables y funciones
# utilizadas o mantenidas por el intérprete de Python.
import sys:

# Función que toma un rango como entrada y no devuelve ningún valor explícito
# (aunque internamente usa yield).
def ft_tqdm(lst: range) -> None:
    """
    Muestra una barra de progreso similar a tqdm para un rango dado.

    Args:
        lst: Un objeto range o cualquier iterable.
    """
    # Calcula el número total de elementos en el rango.
    total = len(lst)
    # Establece el ancho de la barra de progreso.
    width = 42
    # Itera sobre cada elemento del rango, obteniendo el índice (i)
    # y el valor (item).
    for i, item in enumerate(lst):
        # Calcula el progreso actual como un porcentaje.
        progress = (i + 1) / total
        # Calcula la longitud de la parte llena de la barra de progreso.
        filled_length = int(width * progress)
        # Construye la barra visual utilizando caracteres de bloque (█)
        # y espacio (░).
        bar = '█' * filled_length + '░' * (width - filled_length)
        # Escribe en la salida estándar (terminal) el porcentaje de progreso,
        # la barra y el número de iteración actual.
        # El carácter \r mueve el cursor al inicio de la línea,
        # sobreescribiendo la barra anterior.
        sys.stdout.write(f'\r{int(progress * 100)}%|{bar}| {i + 1}/{total}')
        # Fuerza a que la salida se muestre inmediatamente en la terminal.
        sys.stdout.flush()
        # Devuelve el elemento actual del iterador, permitiendo que el bucle
        # que llama a ft_tqdm continúe.
        yield item
    # Al finalizar el bucle, se añade un salto de línea para dejar una
    # línea en blanco.
    sys.stdout.write('\n')

# En Resumen
La función ft_tqdm proporciona una forma sencilla de crear una barra de
progreso personalizada en Python. Al entender cómo funciona, puedes adaptarla
a tus necesidades específicas y crear visualizaciones más informativas para
tus procesos.
'''

'''
tqdm es un pequeño módulo que permite crear una barra de progreso basada
en texto, que es desplegada en pantalla a partir de un bucle.

Además de la barra de progreso, incluye porcentaje, tiempo transcurrido
y remanente, y el número de iteraciones por segundo.

Su implementación es sumamente sencilla.
Se utiliza la función tqdm como envoltura para cualquier objeto iterable.

for i in tqdm(iterable):
    pass

El siguiente código de ejemplo simula una operación en un bucle de
20 iteraciones al bloquear por una cantidad de segundos aleatorios
entre 1 y 5 utilizando la función time.sleep.

from tqdm import tqdm
from time import sleep
from random import randint
for i in tqdm(range(20)):
    sleep(randint(1, 5))
Texto en pantalla al 40%:

|####------| 8/20 40% [elapsed: 00:23 left: 00:34, 0.35 iters/sec]


yield funciona suspendiendo la ejecución de la función para retornar un valor.
La siguiente vez que se llama a la misma función, la ejecución continúa desde
donde se había dejado.

yield es útil para evitar cargar en memoria grandes cantidades de datos que se
deban iterar.
'''
