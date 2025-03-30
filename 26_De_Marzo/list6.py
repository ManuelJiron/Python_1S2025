"""Convertir a mayusculas"""

texto = "La uam es la mejor univeridad"
print(texto)

texto_mayuscula = texto.upper()
print(texto_mayuscula)

"""Convertir a minusculas"""

texto2 = "VAMOS JAGUARES"
texto_minuscula = texto2.lower()
print(texto_minuscula)

""""Convertir la primera letra a mayuscula"""
nombre = "fernando"
nombre = nombre.capitalize()
print(nombre)

"""Convetir la primera letra de cada palabra a mayuscula"""
nombre = "fernando jimenez"
nombre = nombre.title()
print(nombre)

"""Reemplazar texto"""
texto = "Hola mundo C#"
print(texto)

texto = texto.replace("C#", "Python")
print(texto)

"""Eliminar espacios en blanco"""

texto = "    Hola Mundo    "
print(texto)
texto = texto.strip()
print(texto)

"""Formato de numero"""
numero = 1500
print(numero)
numero = "{:,}".format(numero)
print(numero)

"""Formato de numero con decimales"""

numero = 1500.50
print(numero)
numero = "{:.2f}".format(numero)
print(numero)
