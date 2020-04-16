
import pygame
from setting import Settings
from ship import Ship
import game_function as df
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
        df.check_events(ship)
        df.update_screen(ai_settings, screen, ship)

run_game()
