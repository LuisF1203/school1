#ciclos anidados, consiste en un ciclo externo y uno o varios ciclos internos
#cada vez que el ciclo externo completa una iteración, el ciclo interno se reinicia


"""
for i in range(9):

    for i in range(10):
        print(i,end=" ")
    print("\n")
"""






"""
for i in range(1,10,1):
    for j in range(1,10,1):
        print(j,end=' ')

    print("\n")
"""

"""
for i in range(11):
    for j in range(1,i,1):
        print(i-1,end=" ")
    print("\n")

"""
"""
for i in range(1,10,1):
    for j in range(1,i+1,1):
        print(i,end="")
    print("\n")   """

num=int(input('ingresa 1 numero'))

for i in range(1,num+1,1):
    for j in range(1,i+1,1):
        print(i,end="")
    print("\n")
