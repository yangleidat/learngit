import sys
import pygame

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #飞船右移
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False

def update_screen(ai_settings, screen, ship, *args):
    '''更新屏幕上的图像，并切换到新屏幕（刷新屏幕）'''
    #每次循环都会绘制屏幕,填充背景色
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for arg in args:
        arg.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
