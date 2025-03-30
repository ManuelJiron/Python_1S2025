"""10.Escribe un programa que recorra una lista de cadenas y cuente cuántas
veces aparece un carácter específico en cada cadena. Al final, muestra el
conteo para cada cadena."""

lista = ["Hola", "Estudiantes", "de", "Ingeneria", "Sistemas", "Uam"]
caracter = "a"
conteo = []
for cadena in lista:
    conteo.append(cadena.count(caracter))
print(conteo)
