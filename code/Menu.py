#!usr/bin/python
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')                      #carregando imagem
        self.rect = self.surf.get_rect(left=0, top=0)                            #traçando o quadrado para add a imagem

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')  # passando os parametros da musica do menu
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # passando o destino
            self.menu_text(50, "JOGO DO", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, "TIRINHO", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WINDOW_WIDTH / 2), 180 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 180 + 30 * i))

            # (Check for all )events checando todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # (end pygame) fechando pygame

                if event.type == pygame.KEYDOWN:   #SETA PARA BAIXO
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option +=1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:   #SETA PARA BAIXO
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    #ESCREVENDO NO MENU
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text,True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf,dest=text_rect)



