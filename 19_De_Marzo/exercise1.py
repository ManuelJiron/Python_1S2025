nombre = input("Ingresa tu nobre:")
edad = int(input("Ingresa tu edad:"))

if edad >= 0 and edad <= 12:
    print("Eres niño")
elif edad >= 13 and edad <= 17:
    print("Eres adolescente")
elif edad >= 18 and edad <= 29:
    print("Eres joven")
elif edad >= 30 and edad <= 59:
    print("Eres adulto")
elif edad >= 60:
    print("Eres adulto mayor")
else:
    print("Edad no valida")