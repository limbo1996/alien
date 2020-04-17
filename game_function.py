#创建一个game_function模块，来管理游戏运行函数，可以避免alien_invasion过长

import  sys
import pygame
#管理事件，简化run_game

def check_keydown_evens(event, ship):
    """检测键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_evens(event, ship):
    """检测键盘松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ship):
    """相应鼠标键盘事件"""
    for event in pygame.event.get():# pygame的event.get可以检测键盘事件
        # 退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 相应按下键盘的事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_evens(event, ship)
        # 相应松开键盘的事件
        elif event.type == pygame.KEYUP:
            check_keyup_evens(event, ship)
        # 这样实现了长按键盘可以一直移动，只相应两个事件，按下和松开，按下时是T，松开为F，这样可以一直移动


def update_screen(ai_settings, screen, ship):
    """更新屏幕图像，切换到新图像"""
    #每次循环都会重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()

    # 让新绘制的屏幕可见
    pygame.display.flip()