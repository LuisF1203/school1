import openpyxl
import pygame, sys, time, random
from pygame.locals import *
import tkinter
book=openpyxl.load_workbook('main.xlsx')
hoja=book.active
P=hoja['A1':'A29']
R=hoja['B1':'B29']
Preguntas=[]
Respuestas=[]
global userPreguntasA
global userRespuestasA
userPreguntasA=[]
userRespuestasA=[]
for fila in P:
        for celda in fila:
            if celda.value!=None:
                Preguntas.append(celda.value)
for fila2 in R:
        for celda2 in fila2:
            if celda2.value!=None:
                Respuestas.append(celda2.value)

for i in range(len(Preguntas)):
    userPreguntasA+=[Preguntas[i]]
    userRespuestasA+=[Respuestas[i]]
    print('preguntas:',userPreguntasA,'Respuestas:',userRespuestasA)


if len(Preguntas)>0:
    print('Ya tienees preguntas registradas, deseas continuar? [S]=Sí [N]=No')
    opt=input()
    while opt.lower()=='s' or opt.lower()=='n':
        if opt=='s':
            print(userPreguntasA)
            print(userRespuestasA)
        if opt=='n':
            exec(open("main.py").read())
    print(userPreguntasA,userRespuestasA)
else:
    exec(open("main.py").read())


book.save('main.xlsx')
