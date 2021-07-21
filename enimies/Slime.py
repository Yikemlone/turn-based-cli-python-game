import random

from player import Player
from pythongame.enimies.Enemy import Enemy


class Slime(Enemy):

    angee_meter = 0

    def __init__(self, health: int, damage: int, name: str):
        super().__init__(health, damage, name)

    def check_if_angee(self):
        if self.angee_meter >= 5:
            return self.angee()

        elif self.angee_meter == 4:
            print("It looks like it's getting angry...")
            self.angee_meter += 1

        else:
            print("It's In Rhythm with it's surroundings")

        return 0

    def spit_slime(self):
        print(f"{self.get_name()} spat out slime...it does no damage")
        return 0

    def angee(self):
        self.angee_meter = 0

        print(f"{self.get_name()} is angee! He spits out acidic slime!")

        return self.damage * 100

    def damaged(self, damage: int):
        self.health -= damage
        self.angee_meter += 1
        if self.health <= 0:
            self.dead = True

    def enemy_phase(self, player: Player):
        enemy_option = random.randrange(1, 10)

        if self.angee_meter >= 5:
            player.damaged(self.check_if_angee())

        else:
            if enemy_option == 10:
                print(f"\n{self.get_name()} attacked!")
                player.damaged(self.attack())

            elif enemy_option <= 7:
                player.damaged(self.check_if_angee())

            elif enemy_option == 9:
                player.damaged(self.spit_slime())
