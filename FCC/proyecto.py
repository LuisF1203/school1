e=input("ingresa la premisa")
p=[]
val=""
es=0
a=0
es2=[]
fn=""
for i in range(len(e)):
    if e[i]==" ":
        es2.append(i)
        es=es+1
        a= 0
        while a < es:
          a += 1
for n in range(0,es2[0]):
        print(e[n])
for i in range(len(es2)):
        print(f"hay un espacio en {es2[i]}")
        for a in range(es2[0],es2[i]):
            print(e[a])

print(f"El primer espacio esta en:{es2[0]}")





maxv=es2[len(es2)-1]

print(f"hay:{len(e)} caracteres")
print("-----------------------")
print("Los ultimos valores son")
for x in range(maxv+2,len(e)+1):
    print(f"{x}:{e[x-1]}")
print("-----------------------")


print(f"hay {es} espacios")
print(es2)
print(maxv)
#print(e)
#print(p)
