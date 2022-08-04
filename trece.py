#estructuras de desicion anidada
uno=eval(input('introduce el numero 1: '))
dos=eval(input('introduce el numero 2: '))
tres=eval(input('introduce el numero 3: '))
"""
if uno>dos:
    if uno>tres:
        print(uno,'es mayor')
if dos>uno:
    if dos>tres:
        print(dos,'es mayor')
if tres>uno:
    if tres>dos:
        print(tres,'es mayor')
"""
#uno>tres else dos>tres
"""if uno>tres:
    if uno>dos:
        print(uno,"es mayor")
elif dos>tres:
    if dos>uno:
        print(dos,"es mayor")
else:
    print(tres,'es mayor')"""
if uno>dos:
    if uno>tres:
        print(uno,"es mayor")
else:
    if dos>tres:
        print(dos,'es el mayor')
    else:
        print(tres,'es el mayor')
