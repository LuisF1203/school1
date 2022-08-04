sueldo=eval(input('introduce el sueldo\n'))
if sueldo>10000:
    aumento=sueldo*1.12
else:
    aumento=sueldo*1.15
print("Su nuevo sueldo es:",aumento," pesos")
