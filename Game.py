from player.Player import Player
from pythongame.enimies.Melee import Melee
from pythongame.enimies.ShieldUser import ShieldUser
from pythongame.enimies.BadGuy import BadGuy
from pythongame.enimies.Slime import Slime
from utils.SoundEffects import SoundEffects as se
import time
import random


def displayUserOptions():
    print("""
    Select an option:
        1. Attack    2. Block
        3. Special   4. Heal
            """)


def setBadGuys():
    return [[(Melee(15, 20, "Melee Grunt")), (ShieldUser(20, 5, "Shield Grunt"))],
            [Slime(200, 1, "Greg, The Slime")]]


def setBosses():
    return [[Melee(50, 20, "Big Boy Slasher"), ShieldUser(50, 10, "Small Boy Hank")],
            [Melee(100, 15, "The Slashy Slasher")]]


class Game:
    def __init__(self):
        self.se = se()
        self.player = Player()
        self.running, self.playing = True, False
        self.currentRound = 1
        self.basicGroups = setBadGuys()
        self.bossGroups = setBosses()
        self.badGuys = None
        # self.menu = Menu(self)

    def badGuyRoundSelect(self):

        self.basicGroups = setBadGuys()
        self.bossGroups = setBosses()

        if self.currentRound < 3:
            return random.choice(self.basicGroups)
        elif self.currentRound == 3:
            return random.choice(self.bossGroups)

    def mainMenu(self):
        while self.running:

            if not self.se.playingMusic:
                self.se.playMenu()

            print("1. Play Game   2. Exit Game")

            userOption = self.getValidOption()

            if userOption == 1:
                self.se.chime_sound()
                time.sleep(1)
                self.playing = True
                self.se.stopMenu()
                self.playGame()

            elif userOption == 2:
                print("Exiting Game...")
                time.sleep(1)
                self.se.stopMenu()
                self.playing = False
                self.running = False

    def chooseBadGuy(self):
        count = 1
        amountOfBadGuys = len(self.badGuys)

        for badGuy in self.badGuys:
            print(f"{count}. {badGuy.getName()}")
            count += 1

        chosenBadGuy = self.getValidOption()

        while True:
            if chosenBadGuy > amountOfBadGuys or chosenBadGuy <= 0:
                print("Not an option")
                chosenBadGuy = self.getValidOption()
            else:
                break

        chosenBadGuy -= 1

        if chosenBadGuy < 0:
            chosenBadGuy = 0

        badGuyChosen = self.badGuys[chosenBadGuy]

        return badGuyChosen

    def checkForTaunt(self, badGuys):
        for badGuy in badGuys:
            if isinstance(badGuy, ShieldUser) and badGuy.isTaunting():
                return badGuy
            else:
                return self.chooseBadGuy()

    def potionDrop(self, badGuy):
        if badGuy.health <= 0:
            potionChance = random.randrange(100)
            if potionChance <= 30:
                time.sleep(0.5)
                print("\nYou got a potion! 🧪🧪")
                self.player.getPotion()

    def playerPhase(self, userInput):
        valid = False

        while not valid:

            if userInput == 1:

                badGuySelected = self.checkForTaunt(self.badGuys)
                print(f"\nYou attacked {badGuySelected.getName()}!")
                self.se.attack_sound()

                badGuySelected.damaged(self.player.attack())
                self.potionDrop(badGuySelected)

            elif userInput == 2:
                print("You are now blocking!")
                self.player.block()

            elif userInput == 3:
                badGuySelected = self.chooseBadGuy()
                print("You tried using your special...")
                time.sleep(0.5)
                BadGuy.damaged(badGuySelected, self.player.special())

            elif userInput == 4:
                print("Attempting to heal...")
                time.sleep(0.5)
                self.player.heal()

            else:
                print("Not a valid option, try again.")
                displayUserOptions()
                userInput = self.getValidOption()
                continue

            valid = True

    def meleePhase(self, badGuy):
        enemyOption = random.randrange(1, 3)
        print(type(badGuy))
        if enemyOption == 1:
            print(f"\n{badGuy.getName()} attacked!")
            damage = Melee.attack(badGuy)
            self.player.damageReceived(damage)

        elif enemyOption == 2:
            print(f"\n{badGuy.getName()} tried using slash...")
            time.sleep(1.0)
            self.player.damageReceived(badGuy.slash())

    def shieldUserPhase(self, badGuy):
        badGuy.stopTauting()
        enemyOption = random.randrange(1, 4)
        if enemyOption == 1:
            print(f"\n{badGuy.getName()} attacked!")
            damage = ShieldUser.attack(badGuy)
            self.player.damageReceived(damage)

        elif enemyOption == 2:
            badGuy.block()
        elif enemyOption == 3:
            badGuy.taunt()

    def slimePhase(self, badGuy):
        enemyOption = random.randrange(1, 10)
        if badGuy.angeeMeter >= 5:
            damage = badGuy.bePeaceful()
            self.player.damageReceived(damage)
        else:
            if enemyOption == 10:
                print(f"\n{badGuy.getName()} attacked!")
                damage = Slime.attack(badGuy)
                self.player.damageReceived(damage)

            elif enemyOption <= 7:
                damage = badGuy.bePeaceful()
                self.player.damageReceived(damage)

            elif enemyOption == 9:
                self.player.damageReceived(badGuy.spitSlime())

    def badGuyPhase(self, badGuy):
        if self.player.health <= 0:
            return

        if isinstance(badGuy, Melee):
            self.meleePhase(badGuy)

        elif isinstance(badGuy, ShieldUser):
            self.shieldUserPhase(badGuy)

        elif isinstance(badGuy, Slime):
            self.slimePhase(badGuy)

        else:
            print("Error with Bad guy random option")

    def displayBadGuys(self):
        for badGuy in self.badGuys:
            print(f"""\n {badGuy.name} 
               Health 💗      {badGuy.health}
               Damage ⚔️   {badGuy.damage}\n""")

    def removeDead(self):
        for badGuy in self.badGuys:
            if badGuy.isDead():
                self.badGuys.pop(self.badGuys.index(badGuy))

    def checkIfRoundOver(self):
        roundOver = False
        if len(self.badGuys) <= 0:
            roundOver = True
        return roundOver

    def getValidOption(self):
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

    def badGuyTurn(self):
        for badGuy in self.badGuys:
            if not badGuy.isDead():
                self.badGuyPhase(badGuy)
                time.sleep(1.5)

    def isPlayerDead(self):
        if self.player.health <= 0:
            self.se.death_sound()
            time.sleep(4)
            print("\n\nYou Died!")
            time.sleep(1)
            self.playing = False
            self.se.battleMusicStop()

    def playGame(self):

        self.player.resetPlayer()

        time.sleep(1)
        self.currentRound = 1
        self.badGuys = self.badGuyRoundSelect()
        self.se.battleMusicPlay()

        while self.playing:

            self.player.unblock()
            self.removeDead()
            roundOver = self.checkIfRoundOver()

            if roundOver:
                self.currentRound += 1
                if self.currentRound > 3:
                    self.playing = False
                    self.se.battleMusicStop()
                    self.mainMenu()

                if not self.running:
                    break

                self.badGuys = self.badGuyRoundSelect()

            self.displayBadGuys()
            self.player.displayUser()
            displayUserOptions()

            userOption = self.getValidOption()
            self.playerPhase(userOption)

            time.sleep(1.5)

            self.badGuyTurn()
            self.isPlayerDead()


game = Game()

while game.running:

    game.mainMenu()
