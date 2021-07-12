import random

from pythongame.enimies.Enemies import Enemies


class ShieldUser(Enemies):

    focus = 0
    blocking = False
    taunting = False

    def __init__(self, health, damage, name):
        super(ShieldUser, self).__init__(health, damage, name)

    def damaged(self, userDamage):
        if self.blocking:
            self.health -= (userDamage / 2)
        elif self.taunting:
            self.health -= (userDamage / 3)
        else:
            self.health -= userDamage

        if self.health <= 0:
            self.dead = True

    def block(self):
        print(f"{Enemies.getName(self)} is blocking!")
        self.focus += 5
        self.blocking = True

    def taunt(self):
        if self.focus >= 10:
            print(f"{Enemies.getName(self)} is taunting!")
            self.taunting = True
        else:
            self.block()

    def isTaunting(self):
        self.focus -= 10
        return self.taunting

    def stopTauting(self):
        self.taunting = False

    def enemy_turn(self):

        self.stopTauting()
        enemyOption = random.randrange(1, 4)

        if enemyOption == 1:
            print(f"\n{self.getName()} attacked!")
            return self.attack()

        elif enemyOption == 2:
            self.block()

        elif enemyOption == 3:
            self.taunt()
