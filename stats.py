class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """иницивлизирует статистику"""
        self.reset_stats()

    def reset_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.ships_left = 2