import os
import pygame as pg


def get_sound_and_music_path(asset, folder, file_name):
    return os.path.join(asset, folder, file_name)


def get_sound_effects():
    sounds = []
    for sound in os.listdir(os.path.join("assets", "sounds")):
        sound_path = get_sound_and_music_path("assets", "sounds", sound)
        sounds.append(sound_path)

    return sounds


def get_songs():
    songs = []
    for song in os.listdir(os.path.join("assets", "music")):
        song_path = get_sound_and_music_path("assets", "sounds", song)
        songs.append(song_path)

    return songs


class SoundEffects:

    pg.mixer.init()

    soundEffects = get_sound_effects()
    songs = get_songs()

    def __init__(self):
        self.menuMusic = pg.mixer.Sound(os.path.join("assets", "music", "menu_music.mp3"))
        self.battleMusic = pg.mixer.Sound(os.path.join("assets", "music", "keep_moving(Battle Music).mp3"))
        self.playing_music = False

    def playMenu(self):
        self.menuMusic.play()
        self.playing_music = True

    def stop_menu_music(self):
        self.menuMusic.stop()
        self.playing_music = False

    def play_battle_music(self):
        self.battleMusic.play()
        self.playing_music = True

    def stop_battle_music(self):
        self.battleMusic.stop()
        self.playing_music = False

    @staticmethod
    def ding_sound():
        pg.mixer.Sound(SoundEffects.soundEffects[0]).play()

    @staticmethod
    def attack_sound():
        pg.mixer.Sound(SoundEffects.soundEffects[1]).play()

    @staticmethod
    def death_sound():
        pg.mixer.Sound(SoundEffects.soundEffects[4]).play()

    @staticmethod
    def chime_sound():
        pg.mixer.Sound(SoundEffects.soundEffects[5]).play()

    @staticmethod
    def song_transition(currentSong, nextSong):
        currentSong.stop()
        nextSong.play()
