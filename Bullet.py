# 创建子弹的类
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹类型的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所在位置创建子弹"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 先在原点创建一个子弹，然后根据飞船位置更新子弹

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #储存子弹位置
        self.y = float(self.rect.y)

        # 设置子弹的颜色，速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 减少子弹y轴左边来向上移动子弹
        self.y -= self.speed_factor
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)