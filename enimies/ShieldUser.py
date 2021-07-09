from pythongame.enimies.BadGuy import BadGuy


class ShieldUser(BadGuy):
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
        print(f"{BadGuy.getName(self)} is blocking!")
        self.focus += 5
        self.blocking = True

    def taunt(self):
        if self.focus >= 10:
            print(f"{BadGuy.getName(self)} is taunting!")
            self.taunting = True
        else:
            self.block()

    def isTaunting(self):
        self.focus -= 10
        return self.taunting

    def stopTauting(self):
        self.taunting = False
