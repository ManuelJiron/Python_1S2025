"""7. Escribe un programa que recorra una lista de cadenas y divida cada cadena
en subcadenas utilizando un delimitador específico (por ejemplo, una coma
o un espacio)"""

lista = ["Hola, Estudiantes, de, Ingeneria, Sistemas, Uam"]
nueva_lista = []
for cadena in lista:
    nueva_lista.append(cadena.split(","))
print(nueva_lista)

