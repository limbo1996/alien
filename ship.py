# 创建飞船
#选择好图像后，将其显示在屏幕上
#创建ship模块管理飞船的大部分行为

import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船并显示初始位置"""
        self.screen = screen

        #加载飞船图像并使其获得外部矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)