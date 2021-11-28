class GameStats:
    def __init__(self,g_setting):
        self.g_setting = g_setting
        self.reset_stats()

    def reset_stats(self):
        self.life_left = self.g_setting.lifes