#!usr/bin/python
from code.Const import WINDOW_WIDTH, WIN_HEIGHT
from code.Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WIN_HEIGHT))  # criando janela


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass






