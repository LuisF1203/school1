salario=eval(input('introduce tu salario nominal'))
limite1=0
limite1sup1=0
cuotaFija=0
excedente=0
if salario<0.01:
   print('entre 0.01 y 496.07')
   cuotaFija=0.00
   exendete=1.92
   limite1=0.0149
if salario>496.08:
   print('entre 496.08 y 4210.42')
   excedente=6.40
   limite1=496.08
   if salario>4210.42:
       print('entre 4210.42 y 7399.43')
       cuotaFija=247.23
       excedente=10.88
       limite1=4210.42
       if salario>7399.43:
          print('entre 7399.43 y 8601.51')
          cuotaFija=594.24
          excedente=16.00
          limite1=7399.43
          if salario>8601.51:
             print('entre 8601.51 y 10298.36')
             cuotaFija=786.55
             excedente=17.92
             limite1=8601.51
             if salario>10298.36:
                print('entre 10298.36 y 20770.30')
                cuotaFija=1090.62
                excedente=21.36
                limite1=10298.36
                if salario>20770.30:
                   print('entre 20770.30 y 32776.84')
                   cuotaFija=3327.42
                   excedente=23.52
                   limite1=20770.30
                   if salario>32736.84:
                      print('entre 32736.84 y mayor')
                      cuotaFija=6141.95
                      excedente=30
                      limite1=32736.84
ISR= ((cuotaFija+(salario-limite1))*(excedente%2))/100
print(f'Sueldo {salario}, Límite inferior{limite1},cuota fija {cuotaFija}, excedente {excedente} El ISR es:{ISR}')
