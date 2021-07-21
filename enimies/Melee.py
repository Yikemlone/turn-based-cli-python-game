import time

from player import Player
from pythongame.enimies.Enemy import Enemy
import random


class Melee(Enemy):

    def __init__(self, health: int, damage: int, name: str):
        super().__init__(health, damage, name)

    def slash(self):
        slashHitChance = random.randrange(0, 100)
        if slashHitChance < 30:
            print(f"{self.get_name()} used slash!")
            return self.damage * 2
        else:
            print("He missed!")
        return 0

    def enemy_phase(self, player: Player):
        enemyOption = random.randrange(1, 3)

        if enemyOption == 1:
            print(f"\n{self.get_name()} attacked!")
            player.damaged(self.attack)

        elif enemyOption == 2:
            print(f"\n{self.get_name()} tried using slash...")
            time.sleep(0.5)
            player.damaged(self.slash())
