# 每次给游戏添加功能， 就要引入新的设置，设置一个setting模块
# 将设置储存在Setting类里

class Settings():
    """储存此游戏所有的设置"""
    def __init__(self):
        """初始化屏幕设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
