class GameStat():

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stat()
        self.game_active = False

    def reset_stat(self):
        self.ship_left = self.ai_settings.ship_limit