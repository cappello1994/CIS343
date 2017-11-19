import random
import Monster
from Observer import Observer
from Observable import Observable


class Home(Observer, Observable):
    def __init__(self):
        super(Home, self).__init__()
        self.nummonstersinhome = random.randint(1, 5)
        self.totalhomehealth = 0
        self.monstersinhome = []
        humancount = 0
        for i in range(self.nummonstersinhome):
            monster = Monster.Monster(random.randint(0, 4))
            if monster.name == "Person":
                humancount += 1
            monster.add_observer(self)
            self.totalhomehealth += monster.health
            self.monstersinhome.append(monster)
        if humancount == len(self.monstersinhome):
            for neighborhood in self.observers:
                neighborhood.update()

    def update(self):
        humancount = 0
        for i in range(self.nummonstersinhome):
            if self.monstersinhome[i].health <= 0:
                self.monstersinhome.remove(i)
                self.monstersinhome.append(Monster.Monster(0)).addObserver(self)
        for i in range(self.nummonstersinhome):
            if self.monstersinhome[i].name == "Person":
                humancount =+ 1
        if humancount == self.nummonsterinhome:
            for neighborhood in self.observable:
                neighborhood.update()



