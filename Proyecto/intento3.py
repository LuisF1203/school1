import openpyxl

book =openpyxl.load_workbook('ejemplo.xlsx',data_only=True)
hoja=book.active
hoja.title = "DB Excel"

P={}
P2={}
Q=hoja['D2':'D100']
A=hoja['E2':'E100']

"""
preguntas=int(input('Cuantas preguntas quieres? '))

for i in range(preguntas):
    pregunta=input(f'ingrese la pregunta numero {i+1}: ')
    Respuesta=input((f'ingrese la respuesta de la pregunta {i+1}: '))
    P[pregunta]=Respuesta


print(P.values())
"""


Questions=[]
Answers=[]
for fila in Q:
    info=([celda.value for celda in fila])

    string=' '.join(map(str,info))
    if string =="None":
            string="0"
    if len(string)>1:
        Questions +=[string]

for fila2 in A:
    info2=([celda2.value for celda2 in fila2])
    string2=' '.join(map(str,info2))
    if string2 =="None":
            string2=""
    if len(string2)>0:
        Answers.append(string2)

for i in range(len(Answers)):
    P2[Questions[i]]=Answers[i]
print(Questions)
print(Answers)
print(P2)

