"""9. Escribe un programa que recorra una lista de cadenas y elimine aquellas
que estén vacías. Imprime la lista resultante."""

lista = ["Hola", "", "Estudiantes", "de", "Ingeneria", "Sistemas", "Uam", ""]
nueva_lista = []
for cadena in lista:
    if cadena != "":
        nueva_lista.append(cadena)
print(nueva_lista)

