import random

from pythongame.enimies.Enemies import Enemies


class Slime(Enemies):

    angeeMeter = 0

    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def bePeaceful(self):
        if self.angeeMeter >= 5:
            return self.angee()
        elif self.angeeMeter == 4:
            print("It looks like it's getting angry...")
        else:
            print("It's In Rhythm with it's surroundings")
        return 0

    def spitSlime(self):
        print(f"{self.getName()} spat out slime...it does no damage")
        return 0

    def angee(self):
        self.angeeMeter = 0
        print(f"{self.getName()} is angee! He spits out acidic slime!")
        return self.damage * 100

    def damaged(self, userDamage):
        self.health -= userDamage
        self.angeeMeter += 1
        if self.health <= 0:
            self.dead = True

    def enemy_turn(self):
        enemyOption = random.randrange(1, 10)

        if self.angeeMeter >= 5:
            return self.bePeaceful()

        else:
            if enemyOption == 10:
                print(f"\n{self.getName()} attacked!")
                return self.attack()

            elif enemyOption <= 7:
                return self.bePeaceful()

            elif enemyOption == 9:
                return self.spitSlime()
