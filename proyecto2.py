from tabulate import tabulate
print("Proyecto --------- TABLA DE VERDAD --------- " )
"""
V=int(input("ingresa la cantidad de valores: "))
VA=[]
VV={}
for i in range(V):
    Vi=input(f"Ingresa el valor {i+1}: ")
    VFV=input("ingresa si es verdadero o falso [V,F]")
    VV[Vi]=VFV
    VA.append(Vi)
print(VV)
table = [['First Name', 'Last Name', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
print(tabulate(VA))
"""
E=input("ingresa la expresión:")
Ex=[];
Ad=["p","q","r","s","~","v","^","↔","→"]
Pr=0
Pra=[]
Val={}

for i in E:
    if (i not in Ad):
        print("datos invalidos")
        break
    else:
        Ex.append(i)

for i in range(len(Ex)):
    if Ex[i]=="p":
        Val[Ex[i]]=True
        if Ex[i] not in Pra:
            Pr=Pr+1
            Pra.append(Ex[i])
    if Ex[i]=="q":
        Val[Ex[i]]=True
        if Ex[i] not in Pra:
            Pr=Pr+1
            Pra.append(Ex[i])
    if Ex[i]=="r":
        Val[Ex[i]]=True
        if Ex[i] not in Pra:
            Pr=Pr+1
            Pra.append(Ex[i])

    if Ex[i] =="^":
        print(f"conjunción {Ex[i+1]}")
    if Ex[i] =="v":
        print(f"disyunción {Ex[i+1]}")
    if Ex[i] =="→":
        print(f"condicional {Ex[i+1]}")
    if Ex[i] =="↔":
        print(f"bicondicional {Ex[i+1]}")
for i in range(len(Ex)):
    print(Ex[i])
    if Ex[i]=="~":
        print("negación")
        Val[Ex[i+1]]=="negación"
print(Val)
F=pow(2,Pr)
print("------")
for i in Pra:
    print(f"|{i}|",end="")
for a in range(F):
    print(a)
print("\n------")





"""

def conjuncion(V1, V2):
  return (V1 and V2)

def disyuncion(V1, V2):
  return (V1 or V2)

def negacion(V):
  return not(V)

def condicional(V1, V2):
  if (V1 == 1 and V2 == 0):
    return 0
  else:
    return 1

def bicondicional(V1, V2):
  return (condicional(V1, V2) and condicional(V2, V1))

def main():
  print ('conjuncion(condicional(negacion(C),B) , condicional(C,negacion(A)))')
  print ('a b c\tS')
  for A in range(2):
    for B in range(2):
      for C in range(2):
        formula = int(conjuncion(condicional(negacion(C),B) , condicional(C,negacion(A))))
        print (A,B,C,'\t',formula)

main()
"""
