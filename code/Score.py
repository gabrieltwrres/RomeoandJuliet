import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.locals import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, COLOR_WHITE, WIN_WIDTH
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect()
        pass

    def save(self, menu_return: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/ScoreMusic.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:

            self.window.blit(source=self.surf, dest=self.rect)

            self.score_text(48, 'YOU WIN!!!', C_YELLOW, SCORE_POS['Title'])
            if menu_return == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player 1 INSERT UR NAME:'
            if menu_return == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Team INSERT UR NAME:'
            if menu_return == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Player 1 INSERT UR NAME:'
                else:
                    score = player_score[1]
                    text = 'Player 2 INSERT UR NAME:'

            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 3:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    if event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 3:
                            name += event.unicode
            self.score_text(25, name, COLOR_WHITE, SCORE_POS['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/ScoreMusic.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_title(80, 'top 10 Score', COLOR_WHITE, SCORE_POS['Title'])
        self.score_text(20, 'NAME         SCORE        DATE        ', COLOR_WHITE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'    {name}          {score :05d}         {date}', COLOR_WHITE,
                            SCORE_POS[list_score.index(player_score)])
            self.score_text(10, 'Esc to EXIT', COLOR_WHITE, (WIN_WIDTH / 2, 310))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_title(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/QEWhy.ttf', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date} - {current_time}"
