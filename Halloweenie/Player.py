import random
import Weapon


class Player:
    def __init__(self):
        self.health = random.randint(100, 125)
        self.inventory = []
        for i in range(10):
            weapon = Weapon.Weapon()
            self.inventory.append(weapon)
