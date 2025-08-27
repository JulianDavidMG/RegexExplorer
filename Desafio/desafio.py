import re

texto = input("Ingrese su texto entre ' ':")


#Para Enteros
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto)
print("Enteros hallados:", enteros)


#Para Flotantes
patron_flotantes = r"-?\b\d+\.\d+\b"
flotantes = re.findall(patron_flotantes, texto)
print("Flotantes hallados:", flotantes)


#Para Boleanos
patron_boleanos = r"\b(True|False)\b"
boleanos = re.findall(patron_boleanos, texto)
print("Boleanos hallados:", boleanos)


#Para Srings
patron_strings = r'"\b(.*?)\b"'
strings = re.findall(patron_strings, texto)
print("Strings hallados:", strings)


#Para lista de números
patron_listas = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
lista = re.findall(patron_listas, texto)
print("Listas halladas:", lista)