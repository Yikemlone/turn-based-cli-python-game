class BadGuy:

    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        self.dead = False

    def attack(self):
        return self.damage

    def damaged(self, userDamage):
        self.health -= userDamage

        if self.health <= 0:
            self.dead = True

    def getName(self):
        return self.name

    def isDead(self):
        return self.dead

