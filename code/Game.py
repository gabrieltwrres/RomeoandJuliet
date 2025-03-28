#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import time

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

        # Carregar imagem e som de Game Over
        self.game_over_img = pygame.image.load("./asset/game_over.jpg")
        self.game_over_sound = pygame.mixer.Sound("./asset/game_over.mp3")

        # Carregar imagens de início de fase
        self.level_images = {
            'Lvl1': pygame.image.load("./asset/level1.jpg"),
            'Lvl2': pygame.image.load("./asset/level2.jpg"),
            'Lvl3': pygame.image.load("./asset/level3.jpg"),
            'Lvl4': pygame.image.load("./asset/level4.jpg"),
            'Lvl5': pygame.image.load("./asset/level5.jpg"),
        }

    def show_game_over(self):
        """Exibe a tela de Game Over e toca um som."""
        self.window.fill((0, 0, 0))  # Preenche a tela de preto
        self.window.blit(self.game_over_img,
                         (WIN_WIDTH // 2 - self.game_over_img.get_width() // 2,
                          WIN_HEIGHT // 2 - self.game_over_img.get_height() // 2))
        pygame.display.flip()

        # Para qualquer música e som em execução
        pygame.mixer_music.stop()
        pygame.mixer.stop()

        # Toca o som de game over
        self.game_over_sound.play()

        # Espera 10 segundos antes de voltar ao menu
        time.sleep(10)

    def show_level_start(self, level_name):
        """Exibe uma tela de início da fase."""
        if level_name in self.level_images:
            self.window.fill((0, 0, 0))  # Preenche a tela de preto
            self.window.blit(self.level_images[level_name],
                             (WIN_WIDTH // 2 - self.level_images[level_name].get_width() // 2,
                              WIN_HEIGHT // 2 - self.level_images[level_name].get_height() // 2))
            pygame.display.flip()
            time.sleep(5)  # Exibe a tela por 5 segundos

    def run(self, ):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                self.show_level_start('Lvl1')
                level = Level(self.window, 'Lvl1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    self.show_level_start('Lvl2')
                    level = Level(self.window, 'Lvl2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        self.show_level_start('Lvl3')
                        level = Level(self.window, 'Lvl3', menu_return, player_score)
                        level_return = level.run(player_score)
                    if level_return:
                        self.show_level_start('Lvl4')
                        level = Level(self.window, 'Lvl4', menu_return, player_score)
                        level_return = level.run(player_score)
                    if level_return:
                        self.show_level_start('Lvl5')
                        level = Level(self.window, 'Lvl5', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

                # Se o jogador perder, exibe Game Over antes de voltar ao menu
                if not level_return:
                    self.show_game_over()


            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() #Close  Window
                quit() #End pygame
            else:
                pass


