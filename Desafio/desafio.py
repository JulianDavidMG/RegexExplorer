import re

texto = input("Ingrese su texto entre ' ': ")


# -------------------------------
# Para Enteros (números sin decimales, positivos o negativos)
# -?      → opcionalmente un signo negativo
# \b\d+\b → un número entero delimitado por palabra
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto)
print("Enteros hallados:", enteros, "| Total:", len(enteros))


# -------------------------------
# Para Flotantes (números con decimales)
# -?          → opcionalmente un signo negativo
# \b\d+\.\d+\b → un número con parte entera y decimal
patron_flotantes = r"-?\b\d+\.\d+\b"
flotantes = re.findall(patron_flotantes, texto)
print("Flotantes hallados:", flotantes, "| Total:", len(flotantes))


# -------------------------------
# Para Booleanos (True o False con mayúscula inicial)
patron_boleanos = r"\b(True|False)\b"
boleanos = re.findall(patron_boleanos, texto)
print("Booleanos hallados:", boleanos, "| Total:", len(boleanos))


# -------------------------------
# Para Strings entre comillas dobles
# "(.*?)" → captura cualquier cosa dentro de comillas dobles
patron_strings = r'"(.*?)"' 
strings = re.findall(patron_strings, texto)
print("Strings hallados:", strings, "| Total:", len(strings))


# -------------------------------
# Para listas de números enteros
# \[              → abre corchete
# \s*\d+          → número entero con posibles espacios
# (?:\s*,\s*\d+)* → más números separados por comas
# \s*\]           → cierra corchete
patron_listas = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
lista = re.findall(patron_listas, texto)
print("Listas halladas:", lista, "| Total:", len(lista))


# -------------------------------
# Nota:
# re.findall() = busca TODAS las coincidencias y devuelve una lista.
# len()        = cuenta cuántos elementos hay en esa lista.

#Texto de prueba: '"Hola mundo" 123 -45 3.14 -2.718 True False "Python es genial" [1, 2, 3, 4] [10,20,30] "12345" 0 -0.99'
