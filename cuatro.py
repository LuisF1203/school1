#Entrada
Base=eval(input("introduce el valor de la base: ")) #eval(), analiza el tipo de entrada que se le haga a la variable
Altura=eval(input("introduce el valor de la base: "))
"""Base2=int(input("Dame el valor de la base"))
Altura2=int(input("Dame el valor de la base"))"""

#Proceso
Area=(Base*Altura)/2

print("\n La base es:",Base,"\n La altura es :",Altura,"\n El resultao es:",round(Area,2))

radio=eval( input('introduce el valor del radio: '))
altura=eval( input('introduce el valor de la altura: '))

area=round(3.141592654 *radio **2,2)
volumen=round(area*altura,2)

print(' El radio es: ',radio,'\nLa altura es:',altura,'\nel radio es:',radio,'\nel volumen es: ',volumen)
