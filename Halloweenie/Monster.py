import random
from Observable import Observable


class Monster(Observable):
    def __init__(self, type):
        self.type = type
        if self.type == 0:
            self.name = "Person"
            self.health = 100
        elif self.type == 1:
            self.name = "Zombie"
            self.health = random.randint(50, 100)
        elif self.type == 2:
            self.name = "Vampire"
            self.health = random.randint(100, 200)
        elif self.type == 3:
            self.name = "Ghoul"
            self.health = random.randint(40, 80)
        elif self.type == 4:
            self.name = "Werewolf"
            self.health = 200

    def attack(self, player):
        if self.name == "Person":
            player.health = player.health + 1
        elif self.name == "Zombie":
            player.health = player.health - random.randint(0, 10)
        elif self.name == "Vampire":
            player.health = player.health - random.randint(10, 20)
        elif self.name == "Ghoul":
            player.health = player.health - random.randint(40, 80)
        elif self.name == "Werewolf":
            player.health = player.health - random.randint(0, 40)

    def attackedupon(self, weapon):
        if self.name != "Person":
            if weapon.name == "HersheyKisses":
                self.health = self.health - weapon.damage
            elif weapon.name == "SourStraws" and self.name != "Werewolf":
                if self.name == "Zombie":
                    self.health = self.health - weapon.damage*2
                else:
                    self.health = self.health - weapon.damage
            elif weapon.name == "ChocolateBars" and self.name != "Vampire" and self.name != "Werewolf":
                self.health = self.health - weapon.damage
            elif weapon.name == "NerdBombs":
                if self.name == "Ghoul":
                    self.health = self.health - weapon.damage*5
                else:
                    self.health = self.health - weapon.damage
        if self.health <= 0:
            self.remove_observer()
