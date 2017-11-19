import Home
import random
from Observer import Observer
from Observable import Observable


class Neighborhood(Observer, Observable):
    def __init__(self):
        super(Neighborhood, self).__init__()
        self.x = random.randint(2, 5)
        self.y = random.randint(2, 5)
        self.houselist = []
        self.housesdefeated = 0
        self.totalhousecount= self.x*self.y
        for i in xrange(self.y):
            for j in xrange(self.x):
                house = Home.Home()
                self.houselist.append(house)
                house.add_observer(self)
        self.neighborlist = []
        for i in xrange(self.totalhousecount):
            south = i - self.y
            east = i + 1
            north = i + self.y
            west = i - 1
            if south < 0:
                south = None
            if east > self.totalhousecount or east % self.x == 0:
                east = None
            if west < 0 or west % self.x == (self.x - 1):
                west = None
            if north > self.totalhousecount:
                north = None
        neighbor = [north, east, south, west]
        self.neighborlist.append(neighbor)

    def update(self):
        self.housesdefeated += 1
        if self.housesdefeated == self.totalhousecount:
            for game in self.observable:
                game.update()
