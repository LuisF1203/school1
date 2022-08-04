import openpyxl
book =openpyxl.load_workbook('ejemplo.xlsx',data_only=True)
hoja=book.active
user=hoja['A2':'A100']
password=hoja['C2':'C100']
usernames =[]
psw =[]
for fila in password:
    info=([celda.value for celda in fila])
    string=' '.join(map(str,info))
    if string =="None":
        string="0"
    if len(string)>2:
        psw +=[string]
#print(psw)
for fila in user:
    info=([celda.value for celda in fila])

    string=' '.join(map(str,info))
    if string =="None":
        string="0"
    if len(string)>2:
        usernames +=[string]
#print(usernames)

"""for n in usernames:
    print(n)
"""
usr = input("Ingresa tu usuario: ")
if usernames.index(usr)>=0:
    print('Bienvenido:',usr)
"""lista1 =[info]
lista1 += [info]
print(lista1)"""
