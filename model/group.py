# создаем класс в котором будут находиться вспомогательные методы.

class Group:

    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer