import pygame
from setting import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

# 创建一个pygame窗口
def run_game():
    #初始化一个游戏窗口并创建一个屏幕对象
    pygame.init()

    # 将设置储存在一个对象里
    ai_settings = Settings()

    # 初始化一个屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color = (230, 230, 230)

    #创建飞船
    # 获得他的速度，移动方式
    ship = Ship(ai_settings, screen)

    # 创建group管理所有打出去的子弹
    bullets = Group()

    # 外星人
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    #主循环
    while True:
        #监视鼠标键盘事件

        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船
        ship.update()
        # 更新子弹，并删除消失的子弹
        gf.updata_bullets(bullets)

        # 更新外星人
        gf.update_aliens(aliens)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
