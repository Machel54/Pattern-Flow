import random,sys,time,pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 280
FLASHSPEED = 500 #in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200 
BUTTONGAPSIZE = 20
TIMEOUT = 4 # seconds before game over if no button is pushed

# R G B
WHITE =(255,255,255)
BLACK =(0,0,0)
BRIGHTRED =(255,0,0)
RED =(155,0,0)
BRIGHTGREEN =(0,255,0)
GREEN =(0,155,0)
BRIGHTBLUE =(0,0,255)
BLUE =(0,0,155)
BRIGHTYELLOW =(255,255,0)
YELLOW =(155,155,0)
DRAKGREY =(40,40,40)
bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

YELLOWRECT = pygame.Rect(XMARGIN,YMARGIN,BUTTONSIZE,BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE,YMARGIN,BUTTONSIZE,BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE,BUTTONSIZE,BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE,BUTTONSIZE,BUTTONSIZE)

def main():
    global FPSCLOCK,DISPLAYSURF,BASICFONT,BEEP1,BEEP2,BEEP3,BEEP4
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Flow')
    
    BASICFONT = pygame.font.Font('Bubbler One', 16)
    
    infoSurf = BASICFONT.render('Match the pattern by clicking on the button or using Q,W,A,S keys.',1,DRAKGREY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)
    
    #load sound files
    BEEP1 = pygame.mixer,Sound('beep1.ogg')
    BEEP2 = pygame.mixer,Sound('beep2.ogg')
    BEEP3 = pygame.mixer,Sound('beep3.ogg')
    BEEP4 = pygame.mixer,Sound('beep4.ogg')
    
    # Initialize some variables for a new game
    pattern = [] # stores the pattern of colors
    currentStep = 0 #the color the player must push next
    lastClickTime = 0 #timestamp of the player's last button push
    score = 0   
    #when False the pattern is playing. when True waiting for player to click a colored button:
    waitingForInput = False
    
    while True:#main game loop
        clickedButton = None
        DISPLAYSURF.fill(bgColor)
        drawButtons()
        
        scoreSurf = BASICFONT.render('Score:' + str(score),1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)
        
        DISPLAYSURF.blit(infoSurf, infoRect)
        
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                clickedButton = getButtonClicked(mousex,mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN   
        if not waitingForInput: #play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW,BLUE,RED,GREEN)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else: #waiting for player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()
                
                if currentStep == len(pattern):
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0 #reset to step one
            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                #pushed the incorrect button, or has timed out
                gameOverAnimation()
                #reset the variables for a new game
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0 
                pygame.time.wait(1000)
                changeBackgroundAnimation()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
                