import sys
import pygame

def check_keydown_events(event, ship):
    '''按下按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right =True
    elif event.key == pygame.K_LEFT:
        ship.moving_right = True


def check_keyup_events(event, ship):
    '''松开按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_right = False

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, *args):
    '''更新屏幕上的图像，并切换到新屏幕（刷新屏幕）'''
    #每次循环都会绘制屏幕,填充背景色
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for arg in args:
        arg.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
