import sys
import pygame

# 创建一个pygame窗口
def run_game():
    #初始化一个游戏窗口并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color = (230, 230, 230)
    #主循环
    while True:
        #监视鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都会重新绘制屏幕
        screen.fill(bg_color)

        # 让新绘制的屏幕可见
        pygame.display.flip()

run_game()
