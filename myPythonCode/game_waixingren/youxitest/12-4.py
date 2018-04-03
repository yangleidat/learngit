import sys
import pygame

def mian_window():
    pygame.init()
    screen = pygame.display.set_mode((100, 80))
    pygame.display.set_caption('event.key')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
        
        pygame.display.flip()

mian_window()
