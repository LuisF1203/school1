alumnos=eval(input('ingresa la cantidad de alumnos: '))

if alumnos<=30:
    print('menor o igual a 30 alumnos precio: ',4000/alumnos)
else:
    if alumnos>=30:
        if alumnos>=49:
            if alumnos>=50:
                if alumnos>=99:
                    print('mayor o igual a 99 precio: ',alumnos*65)
                else:
                    print('mayor o igual a 50 alumnos pero menos de 99 precio:',alumnos*70)
        else:
            print('menor o igual a 30 alumnos precio: ',alumnos*96)





#100 65 pesos, 50 a 99 70 pesos, 30 a 49 96 pesos y si son menos de 30 por 4000
