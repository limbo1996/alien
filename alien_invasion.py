import sys
import pygame
from setting import Settings
from ship import Ship
# 创建一个pygame窗口
def run_game():
    #初始化一个游戏窗口并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color = (230, 230, 230)
    #创建飞船
    ship = Ship(screen)
    #主循环
    while True:
        #监视鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都会重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让新绘制的屏幕可见
        pygame.display.flip()

run_game()
