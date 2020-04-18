import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并使其获得外部矩阵
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

