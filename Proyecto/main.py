import pygame, sys, time, random
from pygame.locals import *
import tkinter

print('BIENVEDIDO AL JUEGO')
preguntas=int(input('Ingrese la cantidad de preguntas: '))
userPreguntasA=[]
userRespuestasA=[]
for i in range(preguntas):
    userPreguntas=str(input(f'Ingrese la pregunta numero {i+1}:'))
    userRespuestas=str(input(f'Ingrese la respuesta numero {i+1}:'))
    userPreguntasA+=[userPreguntas]
    userRespuestasA+=[userRespuestas]
print(userPreguntasA,userRespuestasA)

pygame.init()

white=(255,255,255)
width = 500
height = 700
play_surface = pygame.display.set_mode((width, height))
background_image = pygame.image.load("back.png").convert()
background_image2 = pygame.image.load("back2.png").convert()
bird_image = pygame.image.load("superman}.png").convert_alpha()
top_pipe = pygame.image.load("pipe_top.png").convert_alpha()
bot_pipe = pygame.image.load("pipe_bot.png").convert_alpha()
fps = pygame.time.Clock()
question=0


lila=(204,153,255)
pink=(255,102,178)
green=(204,255,153)
blue=(102,178,255)
black=(0,0,0)
white=(255,255,255)


pygame.font.init()
font=pygame.font.SysFont('monospace',75)
#top pipe

def pipe_random_height():
    pipe_h = [random.randint(200,(height/2)-20), random.randint((height/2)+20, height-200)]
    return pipe_h
def Cerrar(c2):
    answer=str(respuesta.get())
    ventana.destroy()
    if answer!=userRespuestasA[c2]:
        main()


def main():
    global score
    global score2
    c=-1
    score2=0
    score = 1
    player_pos = [100, 350]
    gravity = 1.5
    speed = 1
    jump = -30
    #pipe
    pipe_pos = 700
    pipe_width = 50
    pipe_height = pipe_random_height()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        speed += jump
                        pygame.mixer.music.load('salto.mp3')
                        pygame.mixer.music.play(1)
        #Down Force
        speed += gravity
        speed *= 0.95
        player_pos[1] += speed

        #pipe
        if pipe_pos >= -20:
            pipe_pos -= 10
        else:
            pipe_pos = 700
            pipe_height = pipe_random_height()
            score += 1
        counter=0
        numero=3

        if score%5==0:

            if score2<len(userPreguntasA):
                pygame.mixer.music.load('Pregunta.mp3')
                pygame.mixer.music.play(1)
                global ventana
                global respuesta
                ventana=tkinter.Tk()
                ventana.geometry('500x200')
                ventana.title('StudyGame')
                pregunta=tkinter.Label(ventana,text=userPreguntasA[score2],fg='#fff',font='Times 13',bg='MediumPurple4').pack()
                respuesta=tkinter.Entry(ventana)
                respuesta.pack()
                cerrar=tkinter.Button(ventana,text="Revisar",command=lambda: Cerrar(c)).pack()
                c+=1
                score2+=1
                score+=1
                ventana.configure(bg='MediumPurple4')
                ventana.protocol('WM_DELETE_WINDOW', doSomething) # root is your root window
                ventana.mainloop()
                numero=numero+3
                gravity=0.2
                speed *= 0
                pipe_pos=0
                aceptar=600
                play_surface.fill((255,255,255))
                pygame.mixer.music.stop()
            else:
                gravity=0.2
                speed *= 0
                pipe_pos=0
                aceptar=600
                pygame.mixer.music.load('win.mp3')
                pygame.mixer.music.play(1)
                ventana=tkinter.Tk()
                ventana.title('StudyGame')
                ventana.geometry('500x200')
                Puntuacion=tkinter.Label(ventana,text=f'FELICIDADES, tu puntuación es de {score}',fg='#fff',font='Times 13',bg='MediumPurple4').pack()
                cerrar=tkinter.Button(ventana,text="Cerrar",command=lambda:ventana.destroy()).pack()
                run=False
                ventana.configure(bg='MediumPurple4')
                ventana.mainloop()
                with open("puntaje.txt") as archivo:
                    for linea in archivo:
                        print(linea)
                        if int(score)>int(linea):
                            pygame.mixer.music.load('Logro.mp3')
                            pygame.mixer.music.play(1)
                            ventanaScore=tkinter.Tk()
                            ventanaScore.title('StudyGame')
                            ventanaScore.geometry('500x200')
                            Felicidades=tkinter.Label(ventanaScore,text=f'FELICIDADES, tienes un nuevo record {score}, tenias un record de {linea}',fg='#fff',font='Times 13',bg='MediumPurple4').pack()
                            cerrarScore=tkinter.Button(ventanaScore,text="Cerrar",command=lambda:ventanaScore.destroy()).pack()
                            ventanaScore.configure(bg='MediumPurple4')
                            ventanaScore.mainloop()
                            with open("puntaje.txt", "w") as f:
                                f.write(str(score))
                        main()
                main()
        else:
            gravity = 1.5
            speed *= 0.95
            pipe_pos -=10
        #Surface
        play_surface.blit(background_image, [0, 0])
        if score>5 and score<10 or score>15 and score<20 or score>25 and score<30:
            play_surface.blit(background_image2, [0, 0])

        #drawpipe
        play_surface.blit(top_pipe, (pipe_pos, -pipe_height[0]))
        play_surface.blit(bot_pipe, (pipe_pos, pipe_height[1]))

        #player
        play_surface.blit(bird_image, (int(player_pos[0]), int(player_pos[1])))

        #Collision
        if player_pos[1] <= (-pipe_height[0]+500) or player_pos[1] >= pipe_height[1]:
            if player_pos[0] in list(range(pipe_pos, pipe_pos+pipe_width)):
                print(f"Game Over. Score: {score}")
                with open("puntaje.txt") as archivo:
                    for linea in archivo:
                        print(linea)
                        if int(score)>int(linea):
                            pygame.mixer.music.load('Logro.mp3')
                            pygame.mixer.music.play(1)
                            ventanaScore=tkinter.Tk()
                            ventanaScore.title('StudyGame')
                            ventanaScore.geometry('500x200')
                            Felicidades=tkinter.Label(ventanaScore,text=f'Felicidades tienes un nuevo record {score}, tenias un record de {linea}',fg='#fff',font='Times 13',bg='MediumPurple4').pack()
                            cerrarScore=tkinter.Button(ventanaScore,text="Cerrar",command=lambda:ventanaScore.destroy()).pack()
                            ventanaScore.configure(bg='MediumPurple4')
                            ventanaScore.mainloop()
                            with open("puntaje.txt", "w") as f:
                                f.write(str(score))
                pygame.mixer.music.load('perdiste.mp3')
                pygame.mixer.music.play(1)
                main()
        score_text=font.render(str(score),1,white)
        play_surface.blit(score_text,(width/2-score_text.get_width()/2,10))

        #Borders
        if player_pos[1] >= height:
            player_pos[1] = height
            speed = 0
        elif player_pos[1] <= 0:
            player_pos[1] = 0
            speed = 0
        pygame.display.flip()
        fps.tick(25)
def doSomething():
    print('No te puedes salir pa ;)')
main()
pygame.quit()
