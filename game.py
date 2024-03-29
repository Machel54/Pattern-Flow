import random,sys,time,pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
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
    
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    
    infoSurf = BASICFONT.render('Match the pattern by clicking on the button or using Q,W,A,S keys.',1,DRAKGREY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)
    
    #load sound files 
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')
    
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

def terminate():
    pygame.quit()
    sys.exit()
    
def checkForQuit():
    #get all the QUIT events
    for event in pygame.event.get(QUIT):
        #terminate any QUIT events if present
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)
        
def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT
        
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE,BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0,255,1),(255,0,-1)):#animation loop
        for alpha in range(start,end,animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf,(0,0))
            flashSurf.fill((r, g, b, alpha))
            DISPLAYSURF.blit(flashSurf,rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0,0))
    
def drawButtons():
    pygame.draw.rect(DISPLAYSURF,YELLOW,YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF,BLUE, BLUERECT)
    pygame.draw.rect(DISPLAYSURF,RED, REDRECT)
    pygame.draw.rect(DISPLAYSURF,GREEN, GREENRECT)
    
def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    
    newBgSurf = pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b =newBgColor
    for alpha in range(0,255, animationSpeed):#animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)
        
        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0,0))
        
        drawButtons()# redraw buttons on top of the tint

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor 
    
def gameOverAnimation(color=WHITE, animationSpeed=50):
    #plays all beeps at once then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play()
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color
    for i in range(4): # do the flash 4 times
        for start, end, step in ((0,255,1), (255,0,-1)):
            for alpha in range(start, end, animationSpeed * step): #animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf,(0,0))
                DISPLAYSURF.blit(flashSurf,(0,0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                
def getButtonClicked(x,y):
    if YELLOWRECT.collidepoint( (x, y) ):
        return YELLOW
    elif BLUERECT.collidepoint( (x, y) ):
        return BLUE
    elif REDRECT.collidepoint( (x, y) ):
        return RED
    elif GREENRECT.collidepoint( (x, y) ):
        return GREEN
    return None

if __name__ == '__main__':
    main()
    