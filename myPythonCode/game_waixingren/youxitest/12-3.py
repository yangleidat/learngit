import sys
import pygame

class Bsb():
    def __init__(self, screen):
        self.image = pygame.image.load(
            r'D:\myCode\myPythonCode\game_waixingren\images\bsb.bmp')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #定位初始位置
        self.rect.center = self.screen_rect.center
        #标记移动标签
        self.moving_r = False
        self.moving_l = False
        self.moving_u = False
        self.moving_d = False



    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.rect.left > 0:
                self.rect.centerx -= 1
            if event.key == pygame.K_RIGHT and self.rect.right < self.screen_rect.right:
                self.rect.centerx += 1
            if event.key == pygame.K_UP and self.rect.top > 0:
                self.rect.centery -= 1
            if event.key == pygame.K_DOWN and self.rect.bottom < self.screen_rect.bottom:
                self.rect.centery += 1
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption('篮球飞啊飞')
    screen.fill((255, 255, 255))
    bsb = Bsb(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            bsb.update(event)
        
        bsb.blitme()
        pygame.display.flip()



run_game()
