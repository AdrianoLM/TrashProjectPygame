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
        self.image = pygame.image.load(os.path.join('images','crab.png'))
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

player = Player()   # spawn player
player.rect.x = 10   # set position x
player.rect.y = 500   # set position y
player_list = pygame.sprite.Group() #add player to a sprite group
player_list.add(player)
steps = 1 #how many pixels the player move

enemy   = Enemy(200,500)# spawn enemy
enemy2   = Enemy(500,450)# spawn enemy
enemy_list = pygame.sprite.Group()   # create enemy group
enemy_list.add(enemy)                # add enemy to group

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
    enemy_list.draw(world)  #draw enemies
    for e in enemy_list:
        e.move()
    player.update() #update player position
    player_list.draw(world) #draw player
    pygame.display.flip() #refreshing the game
    clock.tick(fps) #advance the game's clock
