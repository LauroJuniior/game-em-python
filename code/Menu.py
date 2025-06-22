#!usr/bin/python
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')                      #carregando imagem
        self.rect = self.surf.get_rect(left=0, top=0)                            #traçando o quadrado para add a imagem

    def run(self):
        pygame.mixer_music.load('./asset/Menu.wav')  # passando os parametros da musica do menu
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # passando o destino
            self.menu_text(50, "JOGO DO", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, "TIRINHO", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 180 + 30 * i))

            pygame.display.flip()                               # atualizando a tela

            # (Check for all )events checando todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # (end pygame) fechando pygame

    #ESCREVENDO NO MENU
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text,True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf,dest=text_rect)



