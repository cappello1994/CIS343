import Home
import random


class Neighborhood:
    def __init__(self):
        self.x = random.randint(1, 5)
        self.y = random.randint(1, 5)
        self.houselist = []
        self.totalhousecount = 0
        for i in xrange(self.x):
            for j in xrange(self.y):
                house = Home.Home()
                self.houselist.append(house)
                self.totalhousecount = self.totalhousecount + 1

    def neighbors(self):
        neighborlist = []
        for i in xrange(self.totalhousecount):
            north = i - self.y
            east = i + 1
            south = i + self.y
            west = i - 1
            if north < 0:
                north = None
            if east > self.totalhousecount or east%self.y == 0:
                east = None
            if west < 0 or west%self.y == (self.totalhousecount - 1):
                west = None
            if south > self.totalhousecount:
                south = None
        neighbor = [north, east, south, west]
        neighborlist.append(neighbor)

    def checkneighborhoodhealth(self):
        totalneighborhoodhealth = 0
        for i in xrange(self.totalhousecount):
            totalneighborhoodhealth += self.houselist[i].checkhomehealth()
        return totalneighborhoodhealth