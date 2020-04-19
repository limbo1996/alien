"""
追踪游戏统计信息
"""

class GameStats():
    """跟踪游戏的统计信息，
    相应飞船的碰撞
    追踪飞船碰撞次数等
    """
    def __init__(self, ai_setting):
        """初始化统计信息"""
        self.ai_setting = ai_setting
        self.reset_stats()
        # 使游戏处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化此游戏运行期间的可能变化的统计信息"""
        self.ships_left = self.ai_setting.ship_limit

