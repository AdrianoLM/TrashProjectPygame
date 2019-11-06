import pygame
import sys
import os

'''
OBJECTS
'''
class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 100
        self.images = []

        #Variables to set if the player is with some item or not
        #catch 0=Nothing 1=Bottle 2=Can 3=Paper 4=Organic 
        self.catch = 0

        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha() #optimise alpha
            img.set_colorkey(ALPHA) #set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        update sprite position
        '''   
        # Collision with the trash
        
        # Collision with can
        if player.catch == 0:
            hit_list_can = pygame.sprite.spritecollide(self, can_list, True)
        
            for can in hit_list_can:
                print('PEEEEEEEEEEEEEEGOUUUUUUUUUUU A CAN')
                canpick.play()
                player.catch = 2
                print('player.catch = ', player.catch)
        
            if player.catch == 2:
                can_top = Trash(10,10,'can.bmp')
                can_list.add(can_top)
        else:
            hit_list_can = pygame.sprite.spritecollide(self, can_list, False)
            
            for can in hit_list_can:
                world.blit(text_ocupada,(290,340)) 

        # Collision with bottle
        if player.catch == 0:
            hit_list_bottle = pygame.sprite.spritecollide(self, bottle_list, True)
            
            for bottle in hit_list_bottle:
                print('PEEEEEEEEEEEEEEGOUUUUUUUUUUU O BOTTLE')
                bottlepick.play()
                player.catch = 1
            
            if player.catch == 1:
                bottle_top = Trash(10,10,'bottle.bmp')
                bottle_list.add(bottle_top)
        else:
            hit_list_bottle = pygame.sprite.spritecollide(self, bottle_list, False)
            
            for bottle in hit_list_bottle:
                world.blit(text_ocupada,(290,340))   

        # Collision with paper
        if player.catch == 0:
            hit_list_paper = pygame.sprite.spritecollide(self, paper_list, True)
            
            for paper in hit_list_paper:
                print('PEEEEEEEEEEEEEEGOUUUUUUUUUUU O PAPER')
                paperpick.play()
                player.catch = 3

            if player.catch == 3:
                paper_top = Trash(10,10,'paper.bmp')
                paper_list.add(paper_top)
        else:
            hit_list_paper = pygame.sprite.spritecollide(self, paper_list, False)
            
            for paper in hit_list_paper:
                world.blit(text_ocupada,(290,340)) 

        # Collision with organic
        if player.catch == 0:
            hit_list_organic = pygame.sprite.spritecollide(self, organic_list, True)
            
            for organic in hit_list_organic:
                print('PEEEEEEEEEEEEEEGOUUUUUUUUUUU O ORGANIC')
                print(player.movex)
                applepick.play()
                player.catch = 4

            if player.catch == 4:
                organic_top = Trash(10,10,'organic.bmp')
                organic_list.add(organic_top)
        else:
            hit_list_organic = pygame.sprite.spritecollide(self, organic_list, False)
            
            for organic in hit_list_organic:
                world.blit(text_ocupada,(290,340)) 
            
        # Collision with red trashcan   
        hit_list_trashred = pygame.sprite.spritecollide(self,trashred_list, False)

        for trashred in hit_list_trashred:
            if self.catch == 1:
                print('ENCOSTOU NO LIXO COM O BOTTLE')
                coin.play()
                player.catch = 0
                bottle_list.empty()
            elif self.catch > 1:
                world.blit(text_errado, (300,340))
                print('LIXO ERRADO')
            else:
                print('PEGUE UM LIXO')
                world.blit(text_pegue, (300,340))

        # Collision with yellow trashcan
        hit_list_trashyellow = pygame.sprite.spritecollide(self,trashyellow_list, False)

        for trashyellow in hit_list_trashyellow:
            if self.catch == 2:
                self.catch = 0
                print('ENCOSTOU NO LIXO COM O CAN')
                coin.play()
                player.catch = 0
                can_list.empty()
                print('player.catch = ', player.catch)
            elif self.catch > 2 or self.catch == 1:
                world.blit(text_errado, (300,340))
                print('LIXO ERRADO')
            else:
                print('PEGUE UM LIXO')
                world.blit(text_pegue, (300,340))

        # Collision with blue trashcan
        hit_list_trashblue = pygame.sprite.spritecollide(self,trashblue_list, False)

        for trashblue in hit_list_trashblue:
            if self.catch == 3:    
                self.catch = 0
                print('ENCOSTOU NO LIXO COM O PAPER')
                coin.play()
                player.catch = 0
                paper_list.empty()
                print('player.catch = ', player.catch)
            elif self.catch > 3 or self.catch == 1 or self.catch == 2:
                world.blit(text_errado, (300,340))
                print('LIXO ERRADO')
            else:
                print('PEGUE UM LIXO')
                world.blit(text_pegue, (300,340))

        # Collision with grey trashcan
        hit_list_trashgrey = pygame.sprite.spritecollide(self,trashgrey_list, False)

        for trashgrey in hit_list_trashgrey:
            if self.catch == 4:
                self.catch = 0
                print('ENCOSTOU NO LIXO COM O ORGANIC')
                coin.play()
                player.catch = 0
                organic_list.empty()
                print('player.catch = ', player.catch)
            elif self.catch < 4 and self.catch > 0:
                world.blit(text_errado, (300,340))
                print('LIXO ERRADO')
            else:
                print('PEGUE UM LIXO')
                world.blit(text_pegue, (300,340))

        # Collision woth the enemies
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)

        for enemy in hit_list:
            self.health -= 1
            hit.play()
            oof.play()
            print(self.health)
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey 

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 1
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 1
            self.image = self.images[self.frame//ani]
        
        # moving up
        if self.movey < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 1
            self.image = self.images[self.frame//ani]
        
        # moving down
        if self.movey > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 1
            self.image = self.images[self.frame//ani]

        # player dying
        if player.rect.top < 340:
            player.health = 0

        if player.health <= 0:
            player.movex = 0
            player.movey = 0
            world.blit(text_lose, (300,320))
            world.blit(text_spawn, (225,355))
         
class Enemy(pygame.sprite.Sprite):
    '''
    Spawn an enemy
    '''
    def __init__(self,x,y):
        ALPHA = (0,255,0)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images','crab.bmp'))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 # counter move variable
    def move(self):
        '''
        enemy movement
        '''
        distance = 40
        speed = 1

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x = self.rect.x + 1
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x = self.rect.x - 1
        else:
            self.counter = 1

        self.counter += 1

class Trashcan(pygame.sprite.Sprite):
    '''
    spawn trash can
    '''
    def __init__(self,x,y,img):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Trash(pygame.sprite.Sprite):
        '''
        spawn trash can
        '''
        def __init__(self,x,y,img):
        
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join('images',img))
            self.image.set_colorkey(ALPHA)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

class Balloon(pygame.sprite.Sprite):
        '''
        spawn text balloon
        '''
        def __init__(self,x,y,img):
        
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join('images',img))
            self.image.set_colorkey(ALPHA)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

class Level():
    def bad(lvl,eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0],eloc[1]) # spawn enemy
            enemy_list = pygame.sprite.Group() # create enemy group
            enemy_list.add(enemy)
            enemy_list.add(enemy2)                # add enemy to group
        if lvl == 2:
            print("Level " + str(lvl) )

        return enemy_list
'''
Setup
'''
ALPHA = (0,255,0) #chromakey color


worldx = 800
worldy = 600

fps   = 45  # frame rate
ani   = 5   # animation cycle
clock = pygame.time.Clock()
pygame.init()
main = True

world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropbox = world.get_rect()

inventory_x=900
inventory_y=900
inventory = pygame.image.load(os.path.join('images','bottle.bmp')).convert()

#spawning player
player = Player()   # spawn player
player.rect.x = 70   # set player position x
player.rect.y = 490   # set player position y
player_list = pygame.sprite.Group() #add player to a sprite group
player_list.add(player)
steps = 1 #how many pixels the player move

#spawning enemies
enemy   = Enemy(250,500)# spawn enemy
enemy2   = Enemy(500,450)# spawn enemy
enemy_list = pygame.sprite.Group()   # create enemy group
enemy_list.add(enemy)                # add enemy to group

#spawning trash cans
trashred = Trashcan(10,380,'lixo_red.bmp')
trashred_list = pygame.sprite.Group()
trashred_list.add(trashred)

trashyellow = Trashcan(10,435,'lixo_yellow.bmp')
trashyellow_list = pygame.sprite.Group()
trashyellow_list.add(trashyellow)

trashblue = Trashcan(10,490,'lixo_blue.bmp')
trashblue_list = pygame.sprite.Group()
trashblue_list.add(trashblue)

trashgrey = Trashcan(10,545,'lixo_grey.bmp')
trashgrey_list = pygame.sprite.Group()
trashgrey_list.add(trashgrey)

#spawning trashes
bottle = Trash(350,470,'bottle.bmp')
bottle_list = pygame.sprite.Group()
bottle_list.add(bottle)

can = Trash(600,510,'can.bmp')
can_list = pygame.sprite.Group()
can_list.add(can)

paper = Trash(650,450,'paper.bmp')
paper_list = pygame.sprite.Group()
paper_list.add(paper)

organic = Trash(190,550,'organic.bmp')
organic_list = pygame.sprite.Group()
organic_list.add(organic)

#spawning text balloons
balloon1 = Balloon(10,10,'balloon1.png')
balloon2 = Balloon(10,10,'balloon2.png')
balloon_list1 = pygame.sprite.Group()
balloon_list1.add(balloon1)
balloon_list2 = pygame.sprite.Group()
balloon_list2.add(balloon2)


welcome = 1

#inicializando fontes
pygame.font.init()

font_default = pygame.font.get_default_font() #variable to store system default font
font_lose = pygame.font.SysFont(font_default, 45)
font_won = pygame.font.SysFont(font_default, 30)
text_lose = font_lose.render('Você Perdeu', 1, (255, 255, 255))
text_spawn = font_lose.render('Clique para recomeçar', 1, (255, 255, 255))
text_errado = font_lose.render('Lixeira Errada', 1,(255,255,255))
text_pegue = font_lose.render('Pegue um Lixo',1,(255,255,255))
text_ocupada = font_lose.render('Mãos ocupadas',1,(255,255,255))

#COLORS
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

eloc = []
eloc = [220,500]
enemy_list = Level.bad( 1, eloc )

#AUDIOS 
bgsong = pygame.mixer.Sound('bgsong.wav')
hit = pygame.mixer.Sound('hit.ogg')
oof = pygame.mixer.Sound('oof.ogg')
coin = pygame.mixer.Sound('coin.ogg')
paperpick = pygame.mixer.Sound('paperpick.ogg')
applepick = pygame.mixer.Sound('applepick.ogg')
canpick = pygame.mixer.Sound('canpick.ogg')
bottlepick = pygame.mixer.Sound('bottlepick.ogg')

#WELCOME IMAGES

balloon1 = pygame.image.load('images\crab.bmp').convert()

balloon2 = pygame.image.load('balloon2.png').convert()

#BACKGROUND MUSIC START 
bgsong.play()

'''
Game-Loop
'''
while main == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
                player.control(0,-steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('down')
                player.control(0,steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left_stop')
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right_stop')
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up_stop')
                player.control(0,steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('down_stop')
                player.control(0,-steps)

    if player.health <= 0:
        world.blit(text_lose, (215,190))
    while player.health <= 0: #player dying
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('mouse button down')
                    
                    player.catch = 0
                    can_list.empty() #limpando inventário
                    bottle_list.empty()
                    paper_list.empty()
                    organic_list.empty()

                    player.rect.x = 70 #restore player position
                    player.rect.y = 490
                    player.health = 100 #restore health'''

                    bottle = Trash(350,470,'bottle.bmp')
                    bottle_list = pygame.sprite.Group()
                    bottle_list.add(bottle)    

                    can = Trash(600,510,'can.bmp')
                    can_list = pygame.sprite.Group()
                    can_list.add(can)

                    paper = Trash(650,450,'paper.bmp')
                    paper_list = pygame.sprite.Group()
                    paper_list.add(paper)

                    organic = Trash(190,550,'organic.bmp')
                    organic_list = pygame.sprite.Group()
                    organic_list.add(organic)
    
    if welcome == 1:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('BUTTON DOWN')
            balloon_list1.empty()
        elif event.type == pygame.MOUSEBUTTONUP:
            print('BUTTONUP')
            welcome = 2
            
    elif welcome == 2:

        if event.type == pygame.MOUSEBUTTONDOWN:
            balloon_list2.empty()
                        

    world.blit(backdrop, backdropbox) #bliting the background in the game
    
    trashred_list.draw(world) #draw red trashcan
    trashyellow_list.draw(world) #draw blue trash can
    trashblue_list.draw(world) #draw blue trashcan
    trashgrey_list.draw(world) #draw grey trash can

    bottle_list.draw(world) #draw bottles
    can_list.draw(world) #draw cans
    paper_list.draw(world) #draw paper
    organic_list.draw(world) #draw organic waste

    enemy_list.draw(world)  #draw enemies
    for e in enemy_list:
        e.move()
    player.update() #update player position
    player_list.draw(world) #draw player
    balloon_list2.draw(world)
    balloon_list1.draw(world) #draw the welcoming balloon
    pygame.display.flip() #refreshing the game
    clock.tick(fps) #advance the game's clock
    
