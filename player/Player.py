class Player:
    health = 0
    damage = 0
    focus = 0
    blocking = False
    potion = 0

    def attack(self):
        self.focus += 10
        return self.damage

    def damageReceived(self, damage):
        if self.blocking:
            self.health -= (damage / 2)
        else:
            self.health -= damage

    def special(self):
        if self.focus >= 50:
            self.focus -= 50
            print("You used your special!")
            return self.damage * 3
        else:
            print("You don't have enough focus")
            return 0

    def resetPlayer(self):
        self.health = 200
        self.damage = 100000
        self.focus = 0
        self.blocking = False
        self.potion = 0

    def block(self):
        self.blocking = True

    def unblock(self):
        self.blocking = False

    def heal(self):
        if self.potion > 0:
            print("You healed 20 health!")
            self.health += 20
            if self.health > 200:
                self.health = 200
        else:
            print("Don't have any potions!")

    def displayUser(self):
        print(f"Player Health 💗 {self.health}\t" f"Player Damage ⚔ {self.damage}\n"
              f"Player Focus *** {self.focus}\t\t"  f"Potions 🧪 {self.potion}\n")

    def buffDamage(self):
        if self.focus == 100:
            self.damage += 15

    def magic(self):
        pass

    def getPotion(self):
        self.potion += 1
