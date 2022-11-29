import cardOBJ
import character
import deck
import pygame as pygame
from utils import loadSprite
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("A Deck of Many Stories")
        self.screen = pygame.display.set_mode((1000, 800))
        self.background = loadSprite("test.jpg", False)
    def mainLoop(self):
        while True:
            self.handleInput()
            self.gameLogic()
            self.draw()
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    def gameLogic(self):
        pass
    def draw(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()