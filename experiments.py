# import pygame

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((640, 480))
#     clock = pygame.time.Clock()
    
#     radius = 15
#     x = 0
#     y = 0
#     mode = 'blue'
#     points = []
    
#     while True:
        
#         pressed = pygame.key.get_pressed()
        
#         alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
#         ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
#         for event in pygame.event.get():
            
#             # determin if X was clicked, or Ctrl+W or Alt+F4 was used
#             if event.type == pygame.QUIT:
#                 return
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_w and ctrl_held:
#                     return
#                 if event.key == pygame.K_F4 and alt_held:
#                     return
#                 if event.key == pygame.K_ESCAPE:
#                     return
            
#                 # determine if a letter key was pressed
#                 if event.key == pygame.K_r:
#                     mode = 'red'
#                 elif event.key == pygame.K_g:
#                     mode = 'green'
#                 elif event.key == pygame.K_b:
#                     mode = 'blue'
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1: # left click grows radius
#                     radius = min(200, radius + 1)
#                 elif event.button == 3: # right click shrinks radius
#                     radius = max(1, radius - 1)
            
#             if event.type == pygame.MOUSEMOTION:
#                 # if mouse moved, add point to list
#                 position = event.pos
#                 points = points + [position]
#                 points = points[-256:]
                
#         screen.fill((0, 0, 0))
        
#         # draw all points
#         i = 0
#         while i < len(points) - 1:
#             drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
#             i += 1
        
#         pygame.display.flip()
        
#         clock.tick(60)

# def drawLineBetween(screen, index, start, end, width, color_mode):
#     c1 = max(0, min(255, 2 * index - 256))
#     c2 = max(0, min(255, 2 * index))
    
#     if color_mode == 'blue':
#         color = (c1, c1, c2)
#     elif color_mode == 'red':
#         color = (c2, c1, c1)
#     elif color_mode == 'green':
#         color = (c1, c2, c1)
    
#     dx = start[0] - end[0]
#     dy = start[1] - end[1]
#     iterations = max(abs(dx), abs(dy))
    
#     for i in range(iterations):
#         progress = 1.0 * i / iterations
#         aprogress = 1 - progress
#         x = int(aprogress * start[0] + progress * end[0])
#         y = int(aprogress * start[1] + progress * end[1])
#         pygame.draw.circle(screen, color, (x, y), width)

# main()    
# import random

# import time


# def displayIntro():

#     print('You are in a land full of dragons. In front of you,')

#     print('you see two caves. In one cave, the dragon is friendly')

#     print('and will share his treasure with you. The other dragon')

#     print('is greedy and hungry, and will eat you on sight.')

#     print()

# def chooseCave():

#     cave = ''

#     while cave != '1' and cave != '2':

#         print('Which cave will you go into? (1 or 2)')

#         cave = input()


#     return cave



# def checkCave(chosenCave):

#     print('You approach the cave...')

#     time.sleep(2)

#     print('It is dark and spooky...')

#     time.sleep(2)

#     print('A large dragon jumps out in front of you! He opens his jaws and...')

#     print()

#     time.sleep(2)

#     friendlyCave = random.randint(1, 2)

#     if chosenCave == str(friendlyCave):

#         print('Gives you his treasure!')

#     else:

#         print('Gobbles you down in one bite!')



# playAgain = 'yes'

# while playAgain == 'yes' or playAgain == 'y':



#     displayIntro()


#     caveNumber = chooseCave()

#     checkCave(caveNumber)

#     print('Do you want to play again? (yes or no)')

#     playAgain = input()