from player.Player import Player
from pythongame.enimies.Melee import Melee
from pythongame.enimies.ShieldUser import ShieldUser
from pythongame.enimies.Slime import Slime
from utils.SoundEffects import SoundEffects as se
import time
import random


def set_enemies():
    return [[(Melee(15, 20, "Melee Grunt")), (ShieldUser(20, 5, "Shield Grunt"))],
            [Slime(200, 1, "Greg, The Slime")]]


def set_bosses():
    return [[Melee(50, 20, "Big Boy Slasher"), ShieldUser(50, 10, "Small Boy Hank")],
            [Melee(100, 15, "The Slashy Slasher")]]


class Game:
    def __init__(self):
        self.se = se()
        self.player = Player()
        self.running, self.playing = True, False
        self.currentRound = 1
        self.basicGroups = set_enemies()
        self.bossGroups = set_bosses()
        self.enemies = None

    def enemies_round_select(self):
        self.basicGroups = set_enemies()
        self.bossGroups = set_bosses()

        if self.currentRound < 3:
            return random.choice(self.basicGroups)
        elif self.currentRound == 3:
            return random.choice(self.bossGroups)

    def game_options(self):
        while self.running:

            if not self.se.playingMusic:
                self.se.playMenu()

            print("1. Play Game   2. Exit Game")

            userOption = self.get_valid_option()

            if userOption == 1:
                self.se.chime_sound()
                time.sleep(1)
                self.playing = True
                self.se.stopMenu()
                self.play_game()

            elif userOption == 2:
                print("Exiting Game...")
                time.sleep(1)
                self.se.stopMenu()
                self.playing = False
                self.running = False

    def print_enemies(self):
        for index, badGuy in enumerate(self.enemies):
            print(f"{index + 1}. {badGuy.getName()}")

    def choose_enemy(self):

        total_enemies = len(self.enemies)
        self.print_enemies()
        chosenBadGuy = self.get_valid_option()

        while True:
            if chosenBadGuy > total_enemies or chosenBadGuy <= 0:
                print("Not an option")
                chosenBadGuy = self.get_valid_option()
            elif chosenBadGuy < 0:
                chosenBadGuy = 0
            else:
                chosenBadGuy -= 1
                break

        return self.enemies[chosenBadGuy]

    def checkForTaunt(self, badGuys):
        for badGuy in badGuys:
            if isinstance(badGuy, ShieldUser) and badGuy.isTaunting():
                return badGuy
            else:
                return self.choose_enemy()

    def potion_drop(self):
        potionChance = random.randrange(100)
        if potionChance <= 30:
            self.player.getPotion()

    def display_enemies(self):
        for badGuy in self.enemies:
            print(f"""\n {badGuy.name} 
               Health 💗      {badGuy.health}
               Damage ⚔️   {badGuy.damage}\n""")

    def remove_dead_enemies(self):
        for enemy in self.enemies:
            if enemy.isDead():
                self.enemies.pop(self.enemies.index(enemy))

    def is_round_over(self):
        return True if len(self.enemies) <= 0 else False

    def get_valid_option(self):
        while True:
            try:
                userOption = int(input())
                self.se.ding_sound()
                break
            except ValueError:
                print("Can not enter nothing!!")
            except TypeError:
                print("Must be a valid number.")

        return userOption

    def enemy_turn(self):
        if self.player.health <= 0:
            return

        for enemy in self.enemies:
            if not enemy.isDead():
                enemy.enemy_turn()
                time.sleep(1.5)

    def is_player_dead(self):
        if self.player.health <= 0:
            self.se.battleMusicStop()
            self.se.death_sound()
            time.sleep(4)
            print("\n\nYou Died!")
            time.sleep(1)
            self.playing = False

            return True

    def play_game(self):

        self.player.resetPlayer()

        currentRound = 1
        self.enemies = self.enemies_round_select()
        self.se.battleMusicPlay()

        while self.playing:

            self.player.unblock()
            self.remove_dead_enemies()
            roundOver = self.is_round_over()

            if roundOver:
                currentRound += 1

            if currentRound > 3:
                self.playing = False
                self.enemies = self.enemies_round_select()

            self.display_enemies()
            self.player.display_player_stats()
            self.player.display_user_options()

            user_option = self.get_valid_option()
            chosen_enemy = self.choose_enemy()

            self.player.player_phase(user_option, chosen_enemy)

            time.sleep(1.5)

            self.enemy_turn()

            if self.is_player_dead():
                self.playing = False

        self.se.battleMusicStop()
        self.game_options()


def main():
    game = Game()

    while game.running:
        game.game_options()


if __name__ == "__main__":
    main()
