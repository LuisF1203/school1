import pygame,sys

pygame.init()
Clock=pygame.time.Clock()
screen=pygame.display.set_mode([800,800])
base_font=pygame.font.Font(None,32)
user_text=''
final_user_text=[]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                user_text=user_text[0:-1]
            else:
                user_text +=event.unicode
            if event.key==pygame.K_RETURN:
                user_text=user_text[0:-1]
                final_user_text.append(user_text)
                user_text=''
                print(final_user_text)
    screen.fill((0,0,0))
    text_suferce=base_font.render(user_text,True,(255,255,255))
    screen.blit(text_suferce,(0,0))

    pygame.display.flip()
    Clock.tick(60)

