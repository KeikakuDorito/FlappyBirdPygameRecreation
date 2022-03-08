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

The Main Menu/Runfile

THE GLORIOUS MESSY CODE BY NATHAN

I dont have any more time to make it more efficent at the moment.
It would be time consuming to compact the code and try not to break it at the same time.
'''
#Was gonna add some extra things like the bird falling on death and the wings flapping, but it is extra things and we didnt have time

from importlib import reload # Allow the reload module which lets us play the code for the rounds multiple times. VERY IMPORTANT, will pretty much break on removal.
                                #Learnt from https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
import pygame #pygame import
pygame.init()# Initiate the module

round1_firstrun = True #Checks for firstruns so that the reload module doesnt get messy and play the round twice in a row.
round2_firstrun = True


img = pygame.image.load("bg1flappy.png")  #Sets the background image
logo = pygame.image.load("logo.png") #Flappybird logo
screen = pygame.display.set_mode(img.get_size())  #Sets the window size to the background image's size+

class PlayButton(pygame.sprite.Sprite): # Sprite for both the buttons, except we can change the image!
    def __init__(self, image,pos):
        pygame.sprite.Sprite.__init__(self)  #constructing the parent components
        self.image = pygame.image.load(image).convert_alpha() #change the image of the sprite to 1 or 2 play button
        self.rect = self.image.get_rect()
        self.rect.center = pos #changable position

def countdown(single):
    for i in range(5,0,-1):
        if single == True:
            screen.blit(img, (0, 0))# blit backgrounds and delete trails
            instructions = pygame.image.load("instructions.png")
            screen.blit(instructions, (221, 150))
        if single == False:
            screen.blit(img, (0, 0))# blit backgrounds and delete trails
            instructions = pygame.image.load("multiplayer instructions.png") # load the instructions image
            screen.blit(instructions, (165.5, 150))
            instructiontext = font.render(str("Two Player Mode"), True, (255,255,255))
            screen.blit(instructiontext, (100, 10))
        countdown = font.render(str(i), True, (255,255,255))
        screen.blit(countdown, (265, 105))
        pygame.display.flip()
        pygame.time.wait(1000)

def round1(): #Singleplayer initiation sequence, some stuff are diff
    pygame.display.set_caption("Singleplayer!")
    global round1_firstrun
    countdown(True)
    if round1_firstrun == True: #If this is the first time, no need to reload, importing just runs it. After the first time running this becomes obsolete.
        import FlappyBirdRound1
        round1_firstrun = False
    else:
        global FlappyBirdRound1 #Can't import it again so we need to reload it to play it now. After the first time the previous
        reload(FlappyBirdRound1)

def round2(): #Multiplayer takes more time to explain since it's an original idea. Pretty much same structure as the last function.
    pygame.display.set_caption("Multiplayer! Move the mouse to change the height of the pipes!")
    global round2_firstrun
    countdown(False)
    if round2_firstrun == True:
        import FlappyBirdRound2
        round2_firstrun = False
    else:
        global FlappyBirdRound2
        reload(FlappyBirdRound2)

def endgame(): #Get the final score
    print("FINAL SCORE:", score) #Print in console so at least we know it works!
    background = pygame.Surface((553,500))#make a solid color surface so we can put our score in nice readable font
    background = background.convert()
    background.fill((222, 215, 152))
    screen.blit(background, (0, 0))
    finaltext = font.render("Final Score", True, (255,255,255)) #Make the two lines of score text
    screen.blit(finaltext, (150, 200))
    finaltext = font.render(str(score), True, (255,255,255))
    screen.blit(finaltext, (250, 250))
    pygame.display.flip()
    pygame.time.wait(5000) #just wait 5 seconds, so that they can read the score.
    
def menumusic():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("flowergarden.wav"))
    pygame.mixer.Channel(2).set_volume(0.5)

button1 = PlayButton("PlayRound1.png",(176.5,300)) #Button filenames + locations.Locations found using QUICK MATHS and the positional print below
button2 = PlayButton("PlayRound2.png",(376.5,300))
font = pygame.font.Font("flappyfont.TTF", 40) #Set the font for all the text, size 40

def menu(): #It's a function just in case we decide to make a more complex end screen.
    menumusic()
    clock = pygame.time.Clock()
    keep_going = True
    while keep_going:
        clock.tick(30)
        pygame.display.set_caption("Flappy Bird PY - Nathan Woo and Terry Qian")
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                keep_going = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos) #Testing where the mouse is in case it aint workin'. Also let me know if we got the positions right for the buttons
                if pos[0] < 228.5 and pos[0] > 124.5 and pos[1] > 271 and pos[1] < 329: #check if the mouse position when they lift the mouse button is inside the box of the Singleplayer Button
                    pygame.mixer.stop()
                    round1()
                    from FlappyBirdRound1 import score #get the score variable from it (round 1)
                    global score
                    endgame()
                    menumusic()
                elif pos[0] < 428.5 and pos[0] > 324.5 and pos[1] > 271 and pos[1] < 329: #check if the mouse position when they lift the mouse button is inside the box of the Multiplayer Button
                    pygame.mixer.stop()
                    round2()
                    from FlappyBirdRound2 import score #get the score variable from it (round 2)
                    global score
                    endgame() #end the game after you die
                    menumusic()
        
        #Blit the menu, will automatically blit after the score is displayed after all the functions have been displayed
        screen.blit(img, (0, 0))# blit backgrounds and delete trails
        screen.blit(logo, (190, 150))
        screen.blit(button1.image, button1.rect)
        screen.blit(button2.image, button2.rect)
        pygame.display.flip()

menu()
