litros=eval(input("introduce la cantidad de litros: ")) #eval(), analiza el tipo de entrada que se le haga a la variable
precio=eval(input("introduce el precio por galón: "))
galones=litros/3.785
ganancia=round(galones*precio,2)
print("La ganancia de",litros,"litros es: ",ganancia,'$')
