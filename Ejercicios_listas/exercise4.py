"""4. Escribe un programa que busque si una sub cadena está presente en cada
una de las cadenas de una lista. El programa debe devolver una lista con
valores booleanos que indiquen si la sub cadena fue encontrada en cada
cadena."""

lista = ["Hola", "Estudiantes", "de", "Ingeneria", "Sistemas", "Uam"]
subcadena = "de"
encontrado = []
for cadena in lista:
    encontrado.append(subcadena in cadena)
print(encontrado)
