import pygame


def main():
  #As definições do objeto
        pygame.init()
        tela = pygame.display.set_mode([600, 450])
        pygame.display.set_caption("Jogo Iniciante")
        relogio = pygame.time.Clock()
        cor_branco = (255,255,255)
        cor_azul = (108,194,236)
        cor_verde = (152,231,114)
        cor_vermelho = (227,57,9)
        sup = pygame.Surface((600,450))
        sup.fill(cor_azul)

        #variavél recebendo imagem do player

        player = pygame.image.load('player.png').convert()

        #Carrega a imagem de fundo
        fundo = pygame.image.load("imagem_fundo.jpg")

        # Declara o vetor que controla a posicao X e Y do player
        posicaoPlayer = [400, 300]

        # Armazena num vetor a Velocidade de movimentacao do circulo 
        velocidadePapaBolinhas = [5, 5]

        #sup2 = pygame.Surface((100,100))
        #sup2.fill(cor_verde)

        #criando retangilos (left, top, width, height)
        ret = pygame.Rect(310,310,45,45)
        ret2 = pygame.Rect(50,50,100,60)
        pos = (30,30)
        x = 30
        y = 30
        

        
        sair = False

        #inicializando fontes
        pygame.font.init()
        #criando variavei para armazenar a fonte padrao do sistema
        font_padrao = pygame.font.get_default_font()
        font_perdeu = pygame.font.SysFont(font_padrao, 45)
        font_ganhou = pygame.font.SysFont(font_padrao, 30)

        #variavel para armazenar arquivo de audio 
        audio_explosao = pygame.mixer.Sound('explosion-02.ogg')
        

        while sair != True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  
                  sair = True 

                #if event.type == pygame.MOUSEBUTTONDOWN:
                #  pygame.mouse.set_pos(150, 150)
                #if event.type == pygame.MOUSEMOTION:
                  #ret = ret.move(-10,-10)

                # Verifica se alguma tecla foi pressionada, e captura o evento
                pressed = pygame.key.get_pressed()

                
                #Verifica qual tecla (seta) foi pressionada e atualiza o vetor Posicao de acordo com a Velocidade
                if pressed[pygame.K_UP]: posicaoPlayer[1] -= velocidadePapaBolinhas[1]
                if pressed[pygame.K_DOWN]: posicaoPlayer[1] += velocidadePapaBolinhas[1]
                if pressed[pygame.K_LEFT]: posicaoPlayer[0] -= velocidadePapaBolinhas[0]
                if pressed[pygame.K_RIGHT]: posicaoPlayer[0] += velocidadePapaBolinhas[0]
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                        x = -10
                  if event.key == pygame.K_RIGHT:
                        x = +10
                  if event.key == pygame.K_UP:
                        y = -10
                  if event.key == pygame.K_DOWN:
                        y = 10

          relogio.tick(60)
          tela.fill(cor_branco)
          tela.blit(sup, [0,0])
          tela.blit(fundo, (0, 0))
          tela.blit(player, x, y)
          
          

          (xant, yant) = (ret.left, ret.top)
          
          

          #Desenha o player na tela 
          pygame.draw.rect(tela, cor_vermelho, (20,20,45,45))
          
          pygame.draw.rect(tela, (253,147,226), ret2)

          pygame.draw.circle(tela, cor_branco, posicaoPlayer, 20)
          
          pygame.display.update()

          #if pos < (200,200):
          #      y = 30
          #      y += 1
          #      pos = (y,30)
                        
                           
                
        

        pygame.quit() 

main()

