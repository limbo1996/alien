#创建一个game_function模块，来管理游戏运行函数，可以避免alien_invasion过长

import  sys
import pygame
from Bullet import Bullet
from alien import Alien
#管理事件，简化run_game
"""
管理键盘事件
包括
键盘按下
键盘抬起
检测这些事件并作出反应，就是将moving_right | moving_left替换为，实现按住不动也能移动飞船的效果
"""
# 检测键盘按下
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

# 检测键盘抬起
def check_keyup_evens(event, ship):
    """检测键盘松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
# 检测事件
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

"""管理外星人事件
包括
计算一行能放下多少外星人
能放下几行外星人
创建外星人群
检测是否有外星人碰到了屏幕边缘，如果有，改变水平方向移动，并下降
"""
# 计算一行能放下多少外星人
def get_number_aliens(ai_settings, alien_width):
    """计算每行有多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

# 计算能放下几行外星人
def get_number_rows(ai_settings, ship_height, alien_height):
    #计算可以产生多少行外星人
    avalible_sapce_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avalible_sapce_y / (2 * alien_height))

    return number_rows

# 创建外星人
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人使其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
# 创建外星人群
def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人，并计算一行最多多少个
    # 外星人的间距是外星人的宽度
    alien = Alien(ai_settings, screen)
    # 得到一行能放几个外星人
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    # 得到能放几行
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
# 更改外星人方向并使其下移
def change_fleet_direction(ai_settings, aliens):
    """使外星人群，下移，并改变方向"""
    for alien in aliens.sprites():
        # 下移
        alien.rect.y += ai_settings.fleet_drop_speed
        # 改变方向
    ai_settings.fleet_direction *= -1


# 检测外星人群中是否有外星人碰到屏幕边缘，如果有调用change_fleet_direction
def check_fleet_edges(ai_settings, aliens):
    """当有外星人到达边缘的时候采取措施"""
    # 当有外星人到达边缘时，更改fleet_direction 的符号
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
# 更新外星人，应用check_fleet_edges更改外星人的方向，并下移
def update_aliens(ai_settings, aliens):
    """更行外星人群的位置"""
    check_fleet_edges(ai_settings, aliens)
    # 移动方向的更改最终在update里，因为update 乘了 fleet_direction
    aliens.update()
"""
子弹管理
创建子弹
删除消失的子弹
开火

"""
def updata_bullets(bullets):
    # 更新子弹
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

# 开火，限制子弹数量
def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)



"""
屏幕管理，更新屏幕
"""
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


