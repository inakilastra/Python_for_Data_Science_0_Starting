#!/usr/bin/env python3
"""
Ejercicio 01: Primer uso del paquete

Este script muestra la fecha y hora actual en dos formatos diferentes:
1. Segundos transcurridos desde el 1 de enero de 1970 (epoch), en formato decimal y notación científica.
2. Fecha actual en formato "Mes Día Año" (ej: Oct 21 2022).

Nombre del archivo a entregar: format_ft_time.py
Funciones permitidas: time, datetime o cualquier otra biblioteca para obtener la fecha.

Salida esperada: (similar a)
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
Oct 21 2022
"""

# Importamos los módulos necesarios:
# - 'time' para trabajar con el tiempo en segundos desde el epoch
# - 'datetime' para trabajar con fechas y horas de forma más completa
import time
import datetime

# 1. Obtener el tiempo actual en segundos desde el "epoch" (1 de enero de 1970)
seconds_since_epoch = time.time()

# 2. Formatear el número de segundos en formato decimal completo
#    Usamos una f-string para crear una cadena formateada
#    No especificamos formato especial, así que se muestra con muchos decimales
decimal_format = f"{seconds_since_epoch}"

# 3. Formatear el número de segundos en notación científica
#    De nuevo, usamos una f-string, pero ahora con el especificador de formato ':e'
#    ':e' indica a Python que formatee el número en notación científica (ej: 1.67e+09)
scientific_format = f"{seconds_since_epoch:e}"

# 4. Obtener la fecha y hora actual usando el módulo 'datetime'
#    datetime.datetime.now() devuelve un objeto que representa la fecha y hora actual
now = datetime.datetime.now()

# 5. Formatear el objeto de fecha y hora 'now' a un formato específico: "Mes Día Año"
#    Usamos el método strftime() del objeto datetime para formatear la fecha como cadena
#    strftime() necesita un código de formato para saber cómo formatear la fecha
#    En este caso, "%b %d %Y" significa:
#       - %b: Nombre abreviado del mes (ej: Oct, Nov)
#       - %d: Día del mes (en número, ej: 21, 08)
#       - %Y: Año con 4 dígitos (ej: 2022, 2023)
formatted_date = now.strftime("%b %d %Y")

# 6. Imprimir la primera línea de salida: los segundos desde epoch en dos formatos
#    Usamos una f-string para construir la cadena de salida, incluyendo las variables formateadas
print(f"Seconds since January 1, 1970: {decimal_format} or {scientific_format} in scientific notation")

# 7. Imprimir la segunda línea de salida: la fecha actual en formato "Mes Día Año"
print(formatted_date)