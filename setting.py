# 每次给游戏添加功能， 就要引入新的设置，设置一个setting模块
# 将设置储存在Setting类里

class Settings():
    """储存此游戏所有的设置"""
    def __init__(self):
        """初始化屏幕设置"""
    # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    # 飞船设置
        #速度为1.5
        self.ship_speed_factor = 1.5


    # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 限制子弹数量
        self.bullets_allowed = 50

    # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
