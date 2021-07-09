from pythongame.enimies.BadGuy import BadGuy
import random


class Melee(BadGuy):

    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def slash(self):
        slashHitChance = random.randrange(0, 100)
        if slashHitChance < 30:
            print(f"{BadGuy.getName(self)} used slash!")
            return self.damage * 2
        else:
            print("He missed!")
        return 0
