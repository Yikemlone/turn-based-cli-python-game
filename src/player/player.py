import time
from enimies.enemy import Enemy

class Player():
    health: int
    damage: int
    focus: int
    potion: int
    blocking = False

    def attack(self):
        self.focus += 10
        return self.damage

    def damaged(self, damage):
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

    def reset_player(self):
        self.health = 200
        self.damage = 50
        self.focus = 0
        self.blocking = False
        self.potion = 0

    def block(self):
        print("You are now blocking!")
        self.blocking = True

    def unblock(self):
        self.blocking = False

    def heal(self):
        print("Attempting to heal...")
        time.sleep(0.5)

        if self.potion > 0:
            print("You healed 20 health!")
            self.health += 20
            if self.health > 200:
                self.health = 200
        else:
            print("Don't have any potions!")

    def display_player_stats(self):
        print(f"Player Health 💗 {self.health}\t" f"Player Damage ⚔ {self.damage}\n"
              f"Player Focus *** {self.focus}\t\t"  f"Potions 🧪 {self.potion}\n")

    def buffDamage(self):
        if self.focus == 100:
            self.damage += 15

    def magic(self):
        pass

    def new_potion(self):
        print("\nYou got a potion! 🧪🧪")
        time.sleep(0.5)
        self.potion += 1

    @staticmethod
    def display_user_options():
        print("""
        Select an option:
            1. Attack    2. Block
            3. Special   4. Heal
                """)

    def player_phase(self, user_turn_choice, enemy : Enemy):

        if user_turn_choice == 1:
            print(f"You attacked {enemy.get_name()}!")
            time.sleep(1.5)
            enemy.damaged(self.attack())

        elif user_turn_choice == 2:
            self.block()
            time.sleep(1.5)

        elif user_turn_choice == 3:
            print("You tried using your special...")
            time.sleep(0.5)
            enemy.damaged(self.special())
            time.sleep(1.5)

        elif user_turn_choice == 4:
            self.heal()
            time.sleep(1.5)
