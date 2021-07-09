import os
import pygame as pg


class SoundEffects:

    pg.mixer.init()

    print(os.getcwd())

    menuMusic = os.path.join("assets", "music", "menu_music.mp3")
    battleMusic = os.path.join("assets", "music", "keep_moving(Battle Music).mp3")

    def __init__(self):
        self.menuMusic = pg.mixer.Sound(SoundEffects.menuMusic)
        self.battleMusic = pg.mixer.Sound(SoundEffects.battleMusic)
        self.playingMusic = False

    def playMenu(self):
        self.menuMusic.play()
        self.playingMusic = True

    def stopMenu(self):
        self.menuMusic.stop()
        self.playingMusic = False

    def battleMusicPlay(self):
        self.battleMusic.play()
        self.playingMusic = True

    def battleMusicStop(self):
        self.battleMusic.stop()
        self.playingMusic = False

