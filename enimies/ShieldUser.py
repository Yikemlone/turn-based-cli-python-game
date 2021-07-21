import random

from pythongame.enimies.Enemy import Enemy


class ShieldUser(Enemy):

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
        print(f"{self.get_name()} is blocking!")
        self.focus += 5
        self.blocking = True

    def taunt(self):
        if self.focus >= 10:
            print(f"{self.get_name()} is taunting!")
            self.taunting = True
        else:
            self.block()

    def is_taunting(self):
        self.focus -= 10
        return self.taunting

    def stop_taunting(self):
        self.taunting = False

    def enemy_phase(self, player):

        self.stop_taunting()
        enemy_option = random.randrange(1, 4)

        if enemy_option == 1:
            print(f"\n{self.get_name()} attacked!")
            player.damaged(self.attack())

        elif enemy_option == 2:
            self.block()

        elif enemy_option == 3:
            self.taunt()
