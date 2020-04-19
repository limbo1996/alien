# 创建飞船
#选择好图像后，将其显示在屏幕上
#创建ship模块管理飞船的大部分行为
# 屏幕左上角坐标为（0， 0）
import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并显示初始位置"""
        self.screen = screen
        # 可以使得飞船获取他的信息
        self.ai_settings = ai_settings
        #加载飞船图像并使其获得外部矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 储存centerx的值
        self.center = float(self.rect.centerx)
        #移动标记
        # 将moving_right标记为F，当按下时为T，松开为F
        self.moving_right = False
        # 往左移动同理
        self.moving_left = False

    def update(self):
        """根据移动标记飞船的位置"""
        # moving_right 为T时，往右移动
        # 且判断飞船右侧左边小于屏幕最右侧坐标
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # 左移动同理
        # 判断飞船左侧坐标大于0
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据center更新centerx的值
        self.rect.centerx = self.center
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """在检测到碰撞后重新让飞船居中"""
        self.center = self.screen_rect.centerx