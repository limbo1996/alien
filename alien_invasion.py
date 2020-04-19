import pygame
from setting import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats

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

    # 创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)

    #主循环
    while True:
        #监视鼠标键盘事件

        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:

            # 更新飞船
            ship.update()

            # 更新子弹，并删除消失的子弹
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)

            # 更新外星人
            gf.update_aliens(ai_settings, screen, aliens, ship, stats, bullets)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
