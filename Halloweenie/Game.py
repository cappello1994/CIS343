import Neighborhood
import Player
import Weapon
from Observer import Observer
from threading import *
screen_lock = Semaphore(value=1)


class Game(Observer):
    def __init__(self):
        self.neighborhood = Neighborhood.Neighborhood()
        self.neighborhood.add_observer(self)
        self.player = Player.Player()
        self.player.add_observer(self)
        self.currenthome = 0
        self.gameover = False

    def attack(self, weapon, indexofweapon):
        home = self.neighborhood.houselist[self.currenthome]
        for monsters in home.monstersinhome:
            monsters.attackedupon(weapon)
        for monsters in home.monstersinhome:
            if monsters.name != "Person":
                monsters.attack(self.player)
            else:
                if len(self.player.inventory) < 10:
                    candygiven = Weapon.Weapon()
                    self.player.inventory.append(candygiven)
            screen_lock.acquire()
            print(monsters.name, monsters.health)
            screen_lock.release()
        if self.player.health <= 0:
            self.gameover = True
        self.player.inventory[indexofweapon].lifecycle -= 1
        if self.player.inventory[indexofweapon].lifecycle == 0:
            self.player.inventory.pop(indexofweapon)

    def update(self):
        self.gameover = True

    def run(self):
        screen_lock.acquire()
        print('Hi welcome to Halloweenie... The neighbor has been taken over by monsters '
              'and you need to help change everyone back with the help of candy!!')
        screen_lock.release()
        while not self.gameover:
            screen_lock.acquire()
            usercmd = raw_input('Type HELP for commands')
            screen_lock.release()
            if usercmd == "ATTACK":
                screen_lock.acquire()
                print("What would you like to attack with:")
                screen_lock.release()
                weaponcounter = 0
                for weapon in self.player.inventory:
                    screen_lock.acquire()
                    print(weaponcounter, weapon.name, weapon.lifecycle)
                    screen_lock.release()
                    weaponcounter += 1
                screen_lock.acquire()
                weaponchosen = input('Please enter number of weapon chosen:')
                screen_lock.release()
                self.attack(self.player.inventory[weaponchosen], weaponchosen)
                screen_lock.acquire()
                print ("My Health: ", self.player.health)
                screen_lock.release()
            elif usercmd == "CHECK NEIGHBORS":
                screen_lock.acquire()
                print("These are my neighbors")
                screen_lock.release()
                screen_lock.acquire()
                print(self.neighborhood.neighborlist[self.currenthome])
                screen_lock.release()
            elif usercmd == "GO TO NEIGHBORS":
                screen_lock.acquire()
                print("These are my neighbors")
                screen_lock.release()
                screen_lock.acquire()
                print(self.neighborhood.neighborlist[self.currenthome])
                screen_lock.release()
                screen_lock.acquire()
                neighborchosen = input("Please enter address of desired neighbor")
                screen_lock.release()
                for neighbors in self.neighborhood.neighborlist[self.currenthome]:
                    if neighbors == neighborchosen:
                        self.currenthome = neighborchosen
            elif usercmd == "HELP":
                print "ATTACK: to attack"
                print "CHECK NEIGHBORS: to check possible neighbors"
                print "GO TO NEIGHBORS: change house"
        if self.player.health <= 0:
            screen_lock.acquire()
            print("GAME OVER")
            screen_lock.release()
        else:
            screen_lock.acquire()
            print("Congrats you saved the neighborhood!")
            screen_lock.release()


g = Game()
g.run()
