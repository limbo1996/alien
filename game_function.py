#创建一个game_function模块，来管理游戏运行函数，可以避免alien_invasion过长

import  sys
import pygame
from Bullet import Bullet
from alien import Alien
#管理事件，简化run_game

def check_keydown_evens(event, ai_settings, screen, ship, bullets):
    """检测键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)

    # 退出
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_evens(event, ship):
    """检测键盘松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """相应鼠标键盘事件"""
    for event in pygame.event.get():# pygame的event.get可以检测键盘事件
        # 退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 相应按下键盘的事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_evens(event, ai_settings, screen, ship, bullets)
        # 相应松开键盘的事件
        elif event.type == pygame.KEYUP:
            check_keyup_evens(event, ship)
        # 这样实现了长按键盘可以一直移动，只相应两个事件，按下和松开，按下时是T，松开为F，这样可以一直移动

def get_number_aliens(ai_settings, alien_width):
    """计算每行有多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    # 创建一个外星人是其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行最多多少个
    # 外星人的间距是外星人的宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕图像，切换到新图像"""
    #每次循环都会重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites(): # bullets.sprites会返回一个列表，含有所有子弹
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 让新绘制的屏幕可见
    pygame.display.flip()


def updata_bullets(bullets):
    # 更新子弹
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)



