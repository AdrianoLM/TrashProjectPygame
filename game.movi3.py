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
        self.catch_bottle = 0 
        self.catch_can = 0
        self.catch_plastic = 0
        self.catch_organic = 0

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
        hit_list_can = pygame.sprite.spritecollide(self, can_list, True)
        
        for can in hit_list_can:
            print('PEEEEEEEEEEEEEEGOUUUUUUUUUUU A CAN')
            player.catch = 2
            print('player.catch = ', player.catch)
        
        if player.catch == 2:
            can_top = Trash(10,10,'can.bmp')
            can_list.add(can_top)

        hit_list_bottle = pygame.sprite.spritecollide(self, bottle_list, True)
            
        for bottle in hit_list_bottle:
            print('PEEEEEEEEEEEEEEGOUUUUUUUUUUU O BOTTLE')
            player.catch = 1

        if player.catch == 1:
            bottle_top = Trash(10,10,'bottle.bmp')
            bottle_list.add(bottle_top)
            
        # Collision with the red trashcan   
        hit_list_trashred = pygame.sprite.spritecollide(self,trashred_list, False)


        if self.catch == 1:
            for trashred in hit_list_trashred:
                print('ENCOSTOU NO LIXO COM O BOTTLE')
                player.catch = 0
                bottle_list.empty()

        # Collision with yellow trashcan
        hit_list_trashyellow = pygame.sprite.spritecollide(self,trashyellow_list, False)

        if self.catch == 2:
            for trashyellow in hit_list_trashyellow:
                self.catch = 0
                print('ENCOSTOU NO LIXO COM O CAN')
                player.catch = 0
                can_list.empty()
                print('player.catch = ', player.catch)

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
        if player.health <= 0:
            world.blit(text_lose, (300,190))
            world.blit(text_spawn, (210,220))
         
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

#player catched objects
#catch_can = 0
#catch_bottle = 0

#spawning enemies
enemy   = Enemy(200,500)# spawn enemy
enemy2   = Enemy(500,450)# spawn enemy
enemy_list = pygame.sprite.Group()   # create enemy group
enemy_list.add(enemy)                # add enemy to group

#spawning trash cans
trashred = Trashcan(10,420,'lixo_red.bmp')
trashred_list = pygame.sprite.Group()
trashred_list.add(trashred)

trashyellow = Trashcan(10,490,'lixo_yellow.bmp')
trashyellow_list = pygame.sprite.Group()
trashyellow_list.add(trashyellow)

#spawning trashes
bottle = Trash(350,470,'bottle.bmp')
bottle_list = pygame.sprite.Group()
bottle_list.add(bottle)

can = Trash(600,510,'can.bmp')
can_list = pygame.sprite.Group()
can_list.add(can)

#inicializando fontes
pygame.font.init()

font_default = pygame.font.get_default_font() #variable to store system default font
font_lose = pygame.font.SysFont(font_default, 45)
font_won = pygame.font.SysFont(font_default, 30)
text_lose = font_lose.render('Você Perdeu', 1, (255, 255, 255))
text_spawn = font_lose.render('Clique para recomeçar', 1, (255, 255, 255))

#COLORS
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

eloc = []
eloc = [200,500]
enemy_list = Level.bad( 1, eloc )

#AUDIOS 
bgsong = pygame.mixer.Sound('bgsong.wav')
hit = pygame.mixer.Sound('hit.ogg')
oof = pygame.mixer.Sound('oof.ogg')

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
                    player.rect.x = 10 #restore player position
                    player.rect.y = 500
                    player.health = 100 #restore health'''      

    world.blit(backdrop, backdropbox) #bliting the background in the game
    #world.blit(inventory, (10,10))#bliting bottle in the top pf the screen
    trashred_list.draw(world) #draw red trashcan
    trashyellow_list.draw(world) #draw blue trash can
    bottle_list.draw(world) #draw bottles
    can_list.draw(world) #draw cans
    enemy_list.draw(world)  #draw enemies
    for e in enemy_list:
        e.move()
    player.update() #update player position
    player_list.draw(world) #draw player
    pygame.display.flip() #refreshing the game
    clock.tick(fps) #advance the game's clock
