numero=eval(input('ingresa el numero\n'))
a=1
b=1
if numero ==1:
    print(a)
else:
    if numero==2:
        print(a,b,end=" ")
    else:
        counter=3
        print(a,b,end=" ")
        while counter<= numero:
            c=a+b
            print(c,end=" ")
            a=b
            b=c
            counter=counter+1
