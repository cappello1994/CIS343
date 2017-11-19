import random
import Weapon
from Observable import Observable


class Player(Observable):
    def __init__(self):
        super(Player, self).__init__()
        self.health = random.randint(400, 425)
        self.inventory = []
        for i in range(10):
            weapon = Weapon.Weapon()
            self.inventory.append(weapon)

    def checkplayer(self):
        for game in self.observable:
            game.update()
