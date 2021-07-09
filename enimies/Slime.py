from pythongame.enimies.BadGuy import BadGuy


class Slime(BadGuy):

    angeeMeter = 0

    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def bePeaceful(self):
        if self.angeeMeter >= 5:
            return self.angee()
        elif self.angeeMeter == 4:
            self.angeeMeter += 1
            print("It looks like it's getting angry...")
        else:
            print("It's In Rhythm with it's surroundings")
        return 0

    def spitSlime(self):
        print("It spat out slime...it does no damage")
        return 0

    def angee(self):
        self.angeeMeter = 0
        print("Greg is angee! He spits out acidic slime!")
        return self.damage * 100

    def damaged(self, userDamage):
        self.health -= userDamage
        self.angeeMeter += 1
        if self.angeeMeter <= 4:
            print("")

        if self.health <= 0:
            self.dead = True
