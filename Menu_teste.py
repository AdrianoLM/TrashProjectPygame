import pygame
import time
import random

pygame.init()
x=800
y=600
size = (x, y)
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



pygame.display.set_caption("Restoring The World")
clock = pygame.time.Clock()

#Background Image
tela_img1 = pygame.image.load("Nivel_1.png").convert()
tela_instru = pygame.image.load("instruções.png").convert()
background_images = pygame.image.load("imagem.png").convert()
screen.blit(background_images, [0,0])
#Background Music
pygame.mixer.music.load('Musica_intro.mpeg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()
pygame.display.update()
clock.tick(30)

#BUTTONS

pos_mouse = [x ,y]
pos_botao_1 = [343, 338]
pos_botao_2 = [320, 400]
pos_botao_3 = [367, 458]


altura_botao_1 = 40
largura_botao_1 = 100

altura_botao_2 = 40
largura_botao_2 = 170

altura_botao_3 = 40
largura_botao_3 = 70

def clicou(pos_mouse):
      if (pos_mouse[0] >= pos_botao_1[0]) and (pos_mouse[0] <= (pos_botao_1[0] + largura_botao_1)) and (pos_mouse[1] >= pos_botao_1[1]) and (pos_mouse[1] <= (pos_botao_1[1] + altura_botao_1)):
            print ("clicou 1")
            return 1

      elif (pos_mouse[0] >= pos_botao_2[0]) and (pos_mouse[0] <= (pos_botao_2[0] + largura_botao_2)) and (pos_mouse[1] >= pos_botao_2[1]) and (pos_mouse[1] <= (pos_botao_2[1] + altura_botao_2)):
            print ("clicou 2")
            return 2
      
      elif (pos_mouse[0] >= pos_botao_3[0]) and (pos_mouse[0] <= (pos_botao_3[0] + largura_botao_3)) and (pos_mouse[1] >= pos_botao_3[1]) and (pos_mouse[1] <= (pos_botao_3[1] + altura_botao_3)):
            print ("clicou 3")
            return 3


#GAME INTRO

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                  pos_mouse = pygame.mouse.get_pos()

                  if clicou(pos_mouse) ==1:
                        screen.blit(tela_img1,(0,0))
                  elif clicou(pos_mouse)==2:
                        screen.blit(tela_instru,(0,0))
                  elif clicou(pos_mouse)==3:
                        quit()



            pygame.display.update()
                    

pygame.display.flip()

#Quit Pygame
game_intro()
pygame.quit
