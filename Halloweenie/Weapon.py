import random


class Weapon:
    def __init__(self):
        self.type = random.randint(0,3)
        if self.type == 0:
            self.name = "HersheyKisses"
            self.damage = 1
            self.lifecycle = -1
        elif self.type == 1:
            self.name = "SourStraws"
            self.damage = (random.randint(100, 175)/100)
            self.lifecycle = 2
        elif self.type == 2:
            self.name = "ChocolateBars"
            self.damage = (random.randint(20, 24)/10)
            self.lifecycle = 4
        elif self.type == 3:
            self.name = "NerdBombs"
            self.damage = (random.randint(35, 50)/10)
            self.lifecycle = 1
