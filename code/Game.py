#!usr/bin/python
from code.Const import WINDOW_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WIN_HEIGHT))  # criando janela


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = level
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()  # (end pygame) fechando pygame

            else:
                pass







