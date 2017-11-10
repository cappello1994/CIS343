import random
import Monster
from Observer import Observer
from Observable import Observable

class Home(Observer, Observable):
    def __init__(self):
        self.nummonstersinhome = random.randint(0, 5)
        self.totalhomehealth = 0
        self.monstersinhome = []
        for i in range(self.nummonstersinhome):
            monster = Monster.Monster(random.rand(0, 4)).addObserver(self)
            self.totalhomehealth += monster.health
            self.monstersinhome.append(monster)

    def checkhomehealth(self):
        for i in range(self.nummonstersinhome):
            self.totalhomehealth += self.monstersinhome[i].health
        return self.totalhomehealth