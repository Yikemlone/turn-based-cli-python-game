import time

from pythongame.enimies.Enemies import Enemies
import random


class Melee(Enemies):

    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def slash(self):
        slashHitChance = random.randrange(0, 100)
        if slashHitChance < 30:
            print(f"{Enemies.getName(self)} used slash!")
            return self.damage * 2
        else:
            print("He missed!")
        return 0

    def enemy_turn(self):
        enemyOption = random.randrange(1, 3)

        if enemyOption == 1:
            print(f"\n{self.getName()} attacked!")
            damage = Melee.attack(self)
            return damage

        elif enemyOption == 2:
            print(f"\n{self.getName()} tried using slash...")
            time.sleep(1.0)
            return self.slash()
