"""6. Escribe un programa que recorra una lista de cadenas y elimine los
espacios en blanco al principio y al final de cada cadena."""

lista = [" Hola ", " Estudiantes ", " de ", " Ingeneria ", " Sistemas ", " Uam "]
nueva_lista = []
for cadena in lista:
    nueva_lista.append(cadena.strip())
print(nueva_lista)
