"""Escribe un programa que recorra una lista de cadenas y convierta cada
cadena a mayúsculas o minúsculas dependiendo de un criterio. Si la
longitud de la cadena es par, se convertirá a mayúsculas; si es impar, a
minúsculas"""

lista = ["Hola", "Estudiantes", "de", "Ingeneria", "Sistemas", "Uam"]
nueva_lista = []
for cadena in lista:
    if len(cadena) % 2 == 0:
        nueva_lista.append(cadena.upper())
    else:
        nueva_lista.append(cadena.lower())
print(nueva_lista)