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

