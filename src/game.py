import time
import random
import platform
import os
from player.player import Player
from enimies.melee import Melee
from enimies.shielduser import ShieldUser
from enimies.slime import Slime
from utils.SoundEffects import SoundEffects as se
from enimies.enemy import Enemy


def set_enemies():
    return [[(Melee(15, 20, "Melee Grunt")), (ShieldUser(20, 5, "Shield Grunt"))],
            [Slime(200, 1, "Greg, The Slime")]]


def set_bosses():
    return [[Melee(50, 20, "Big Boy Slasher"), ShieldUser(50, 10, "Small Boy Hank")],
            [Melee(100, 15, "The Slashy Slasher")]]


def clear_screen():
    system = platform.system().lower()
    if system == "windows":
        os.system('cls')  # Windows
    else:
        os.system('clear')  # macOS/Linux

class Game:
    def __init__(self):
        self.se : se = se()
        self.player : Player = Player()
        self.running : bool = True
        self.playing : bool = False
        self.current_round : int = 1
        self.basic_groups : list[Enemy] = set_enemies()
        self.boss_groups : list[Enemy]  = set_bosses()
        self.enemies : list[Enemy] = None

    def enemies_round_select(self) -> Enemy:
        self.basic_groups = set_enemies()
        self.boss_groups = set_bosses()

        if self.current_round < 3:
            return random.choice(self.basic_groups)
        elif self.current_round == 3:
            return random.choice(self.boss_groups)

    def game_main_menu(self) -> None:
        while self.running:
            if not self.se.playing_music:
                self.se.playMenu()

            print("1. Play Game   2. Exit Game")
            user_option = self.get_valid_number()

            if user_option == 1:
                self.se.chime_sound()
                time.sleep(1)
                self.playing = True
                self.se.stop_menu_music()
                self.play_game()

            elif user_option == 2:
                print("Exiting Game...")
                time.sleep(0.5)
                self.se.stop_menu_music()
                self.running = False


    def print_enemies(self):
        for index, bad_guy in enumerate(self.enemies):
            print(f"{index + 1}. {bad_guy.get_name()}")

    def get_taunter(self):
        for enemy in self.enemies:
            if isinstance(enemy, ShieldUser):
                return enemy if enemy.is_taunting() else None

        return None

    def choose_enemy(self):
        if self.player.blocking:
            return

        self.print_enemies()
        chosen_bad_guy = self.get_valid_number()
        taunting_enemy = self.get_taunter()

        if taunting_enemy is not None:
            return taunting_enemy

        while True:
            if chosen_bad_guy > len(self.enemies) or chosen_bad_guy < 1:
                print("Not an option")
                chosen_bad_guy = self.get_valid_number()
            else:
                chosen_bad_guy -= 1
                break

        return self.enemies[chosen_bad_guy]

    def check_for_taunt(self, enemies: dict):
        for enemy in enemies:
            if isinstance(enemy, ShieldUser) and enemy.is_taunting():
                return enemy
            else:
                return self.choose_enemy()

    def potion_drop(self):
        potion_chance = random.randrange(100)
        if potion_chance <= 30:
            self.player.new_potion()

    def display_enemies(self):
        for enemy in self.enemies:
            print(f"""\n {enemy.name} 
               Health 💗      {enemy.health}
               Damage ⚔️   {enemy.damage}\n""")

    def remove_dead_enemies(self):
        for enemy in self.enemies:
            if enemy.is_dead():
                self.enemies.pop(self.enemies.index(enemy))

    def is_round_over(self):
        return True if len(self.enemies) <= 0 else False

    def get_valid_number(self):
        while True:
            try:
                user_option = int(input())
                self.se.ding_sound()
                break
            except ValueError:
                print("Can not enter nothing!!")
            except TypeError:
                print("Must be a valid number.")

        return user_option

    def enemies_phases(self):
        if self.player.health <= 0:
            return

        for enemy in self.enemies:
            if not enemy.is_dead():
                enemy.enemy_phase(self.player)
                time.sleep(1.5)

    def is_player_dead(self):
        return True if self.player.health <= 0 else False

    def display_all_displayables(self):
        self.display_enemies()
        self.player.display_player_stats()
        self.player.display_user_options()

    def new_round(self, current_round):
        current_round += 1
        self.enemies = self.enemies_round_select()

        if current_round > 2:
            self.playing = False

        return current_round

    def player_died(self):

        self.se.stop_battle_music()
        self.se.death_sound()

        time.sleep(4)

        print("\n\nYou Died!")

        self.playing = False

    def get_valid_player_option(self):
        while True:
            user_option = self.get_valid_number()
            if user_option < 1 or user_option > 4:
                print("Not a valid player option! Try Again.")
                continue

            if user_option == 2:
                self.player.blocking = True

            return user_option

    def play_game(self):

        self.player.reset_player()
        self.enemies = self.enemies_round_select()
        self.se.play_battle_music()
        current_round = 1

        while self.playing:
            clear_screen()
            self.remove_dead_enemies()

            if self.is_round_over():
                current_round = self.new_round(current_round)

            self.display_all_displayables()

            player_option = self.get_valid_player_option()
            chosen_enemy = self.choose_enemy()

            self.player.player_phase(player_option, chosen_enemy)
            self.enemies_phases()
            self.player.unblock()

            if self.is_player_dead():
                self.player_died()

        self.se.stop_battle_music()
        self.game_main_menu()


def main():
    game = Game()

    while game.running:
        game.game_main_menu()


if __name__ == "__main__":
    main()
