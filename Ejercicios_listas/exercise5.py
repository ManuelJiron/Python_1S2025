"""5. Escribe un programa que recorra una lista de cadenas y reemplace todas
las apariciones de un carácter específico con otro carácter, luego imprime la
lista modificada"""

lista = ["Hola", "Estudiantes", "de", "Ingeneria", "Sistemas", "Uam"]
caracter = "a"
nuevo_caracter = "4"
nueva_lista = []
for cadena in lista:
    nueva_lista.append(cadena.replace(caracter, nuevo_caracter))
print(nueva_lista)
