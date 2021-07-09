# import os
# import pygame
# from discordbot.textgame.SoundEffects import SoundEffects
#
# class Menu:
#
#     def __init__(self, game):
#         pygame.init()
#         self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
#         self.DISPLAY_W, self.DISPLAY_H = 480, 270
#         self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
#         self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
#         self.menu = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
#         self.font_name = os.path.join("assets/fonts/digital-7 (mono).ttf")
#         self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
#         self.game = game
#         self.se = SoundEffects()
#         self.FPS = 60
#
#     def gameLoop(self):
#         while self.game.running:
#             self.checkEvents()
#             if self.START_KEY:
#                 self.START_KEY = False
#             self.display.fill(self.BLACK)
#             self.mainMenu()
#             self.window.blit(self.display, (0, 0))
#             pygame.display.update()
#             self.reset_keys()
#
#     def checkEvents(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.game.running, self.game.playing = False, False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     self.START_KEY = True
#                 if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
#                     self.BACK_KEY = True
#                 if event.key == pygame.K_DOWN or event.key == pygame.K_s:
#                     self.DOWN_KEY = True
#                 if event.key == pygame.K_UP or event.key == pygame.K_w:
#                     self.UP_KEY = True
#
#     def reset_keys(self):
#         self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
#
#     def draw_text(self, text, size, x, y):
#         font = pygame.font.Font(self.font_name, size)
#         text_surface = font.render(text, True, self.WHITE)
#         text_rect = text_surface.get_rect()
#         text_rect.center = (x, y)
#         self.display.blit(text_surface, text_rect)
#
#     def mainMenu(self):
#         if not self.se.playingMusic:
#             self.se.playMenu()
#
#         self.draw_text('Play Game', 30, self.DISPLAY_W / 2 - 5, self.DISPLAY_H / 2 - 30)
#         self.draw_text('Exit Game', 30, self.DISPLAY_W / 2 - 5, self.DISPLAY_H / 2 + 30)
#
#         """   if userOption == 1:
#             self.se.chimeSound()
#             time.sleep(1)
#             self.playing = True
#             self.se.stopMenu()
#             self.playGame()
#
#         elif userOption == 2:
#             print("Exiting Game...")
#             time.sleep(1)
#             self.se.stopMenu()
#             self.playing = False
#             self.running = False"""