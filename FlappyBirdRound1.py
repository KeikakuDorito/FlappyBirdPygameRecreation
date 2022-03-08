'''
───────────▄██████████████▄───────
───────▄████░░░░░░░░█▀────█▄──────
──────██░░░░░░░░░░░█▀──────█▄─────
─────██░░░░░░░░░░░█▀────────█▄────
────██░░░░░░░░░░░░█──────────██───
───██░░░░░░░░░░░░░█──────██──██───
──██░░░░░░░░░░░░░░█▄─────██──██───
─████████████░░░░░░██────────██───
██░░░░░░░░░░░██░░░░░█████████████─
██░░░░░░░░░░░██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
██░░░░░░░░░░░██░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
─▀███████████▒▒▒▒█▓▓▓███████████▀─
────██▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓█──
─────██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓█──
──────█████▒▒▒▒▒▒▒▒▒▒██████████───
─────────▀███████████▀────────────


Flappy Bird: Python Recreation
Ms. Wun
ISC3U1-03
Nathan Woo, Terry Quan
'''


import pygame
import random

pygame.init()
#May 9
class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #constructing the parent components
        self.image = pygame.image.load("Floor Flappy Bird.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 500)

    def update(self):
        if self.rect.left <= -453: #put it back in a set location to make it look infinite
            self.rect.left = 0
            floorgroup.clear(screen, screen)
        self.rect.move_ip(obspeed, 0) #Move at an x amount of speed to the left, but when it hits an area it moves back to its original position so it's SPOOKY infinite.


class Bird(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)  #constructing the parent components
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (276, 250)
       
    def update(self):
        self.rect.move_ip(0,y_speed) #Bird just literally stays in place while everything else moves. It just changes the y value/speed
        
class TopPipe(pygame.sprite.Sprite):
    def __init__(self,pipe_x,pipe_y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load("toppipe.png").convert_alpha() #TRANSPARENCY
        self.rect = self.image.get_rect()
        self.rect.bottom = pipe_y - 50
        self.rect.left = pipe_x

    def update(self):
        self.rect.move_ip(obspeed,0)
        if self.rect.right == 0:
            self.kill()
            
        if self.rect.collidepoint(276,0) and count == 1: #Scorekeeping works by everytime it passes the center H4X, ONLY ON TOP PIPES!
            global score
            score += 1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("score.wav")) #PLAY THAT SWEET DINGING NOISE
            print("Score:",score)

            
class BotPipe(pygame.sprite.Sprite):
    def __init__(self,pipe_x,pipe_y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load("bottompipe.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = pipe_y + 50
        self.rect.left = pipe_x

    def update(self):
        self.rect.move_ip(obspeed,0)
        if self.rect.right == 0:
            self.kill()



    
#####################
##SETTING VARIABLES##                                                                                                                  OWO WHATS THIS
#####################

obspeed = -5
count = 0
pipe_delay = 60
gravityspeed = 6
y_speed = gravityspeed
space_pressed = False
flap_time = 0
pasttime = 0
score = 0
maxheight_pipes = 150
minheight_pipes = 257
passed = False
cheat = False
birdframe = 0
birdsprite = "Bird1.png"

# May 7
#set the bg
img = pygame.image.load("bg1flappy.png")  #Sets the background image
screen = pygame.display.set_mode(img.get_size())  #Sets the window size to the background image's size

font = pygame.font.Font("flappyfont.TTF", 40)

floor = Floor()
floorgroup = pygame.sprite.Group()
floorgroup.add(floor)


Pipes = pygame.sprite.Group()

bird = Bird(birdsprite)

clock = pygame.time.Clock()
keep_going = True
while keep_going:
    clock.tick(30)
    count += 1
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            keep_going = False
        if ev.type == pygame.KEYDOWN:
            now = pygame.time.get_ticks()
            if now - pasttime >= 34:
                if ev.key == pygame.K_SPACE: #When space key is pressed make it go up
                    print(now - pasttime)
                    y_speed = -15
                    pygame.mixer.music.load("flap.wav")
                    pygame.mixer.music.play()
                    space_pressed == True
        if  ev.type == pygame.KEYUP:
            if ev.key == pygame.K_SPACE:
                space_pressed == False
                y_speed = gravityspeed/3
                y_speed = gravityspeed
            if ev.key == pygame.K_f:
                if cheat == False:
                    cheattext = font.render("No-clip", True, (255,255,255))
                    cheat = True
                elif cheat == True:
                    cheat = False


    if cheat == False:
        if pygame.sprite.spritecollideany(bird, floorgroup) or pygame.sprite.spritecollideany(bird, Pipes): #END DA GAME
            
            if pygame.sprite.spritecollideany(bird, Pipes):
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("fall.wav"))
            if pygame.sprite.spritecollideany(bird,floorgroup):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("smack.wav"))
            keep_going = False # FOR NOW IT KILLS THE PROGRAM
    

    if count == pipe_delay: #Spawning of the pipes
        yloc = random.randint(maxheight_pipes,minheight_pipes) #Randomizes pipe entry hieghts
        top = TopPipe(553,yloc)
        bottom = BotPipe(553,yloc)
        Pipes.add(top)
        Pipes.add(bottom)
        count = 0

    scoretext = font.render(str(score), True, (255,255,255))

        
    pasttime = pygame.time.get_ticks()            
                
    
    floorgroup.clear(screen, screen) #UPDATE DA FLOORS, BLIT DA FLOORS
    Pipes.clear(screen,screen)
    screen.blit(img, (0, 0))# blit backgrounds and delete trails
    Pipes.draw(screen) #draw the pipes
    Pipes.update() #Get the pipes to move
    floorgroup.draw(screen)
    floorgroup.update()
    screen.blit(bird.image, bird.rect)
    
    bird.update()
    screen.blit(scoretext, (266.5, 10))
    
    if cheat == True:
        screen.blit(cheattext, (0, 0))
       
    pygame.display.flip()
