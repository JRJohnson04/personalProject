
import character
import deck
import pygame as pygame
from utils import loadSprite
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("A Deck of Many Stories")
        self.screen = pygame.display.set_mode((1440, 1000))
        self.background = loadSprite("Background", False)
    def mainLoop(self):
        while True:
            self.handleInput()
            self.gameLogic()
            self.back()
            ypos = 95
            player = character.player()
            player.fillDeck()
            player.myDeck.draw()
            for i in range(len(player.myDeck.hand)):
                self.screen.blit(player.myDeck.hand[i].sprite, ((95 + (250 * i)), 1040))
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    def gameLogic(self):
        pass
    def back(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()
