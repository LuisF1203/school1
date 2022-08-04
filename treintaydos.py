#solicitar al usuario que ingrese su direccióm email. imprimir un mensaje indicando si la dirección es válida o no, valiendose de si tiene un @

def email(correo):
    for i in range(len(correo)):
        if correo[i] == "@":
            return True
    return False
correo=str(input('ingrese su correo electrónico: '))
"""if email(correo):
    print(f'el correo {correo} ees valido')
else:
    print(f'el correo {correo} es invalido')
"""
while email(correo)==False:
    print('vuelve a escribir tu email')
    correo=input('dame tu email: ')
print(f'correo {correo} valido')
