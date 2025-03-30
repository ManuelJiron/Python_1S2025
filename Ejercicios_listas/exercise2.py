"""2. Escribe un programa que recorra una lista de cadenas y calcule la longitud
de cada cadena, almacenando el resultado en una nueva lista.
"""
# Crea una lista de cadenas de texto
lista = ["Hola", "Estudiantes", "de", "Ingeneria", "Sistemas", "Uam"]
longitud = []
for cadena in lista:
     longitud.append(len(cadena))
print(longitud)
