import deck
import character
import cardOBJ
import pygame as pygame
from utils import loadSprite
class Game:
    turns = 0
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("A Deck of Many Stories")
        self.screen = pygame.display.set_mode((1440, 1000))
        self.background = loadSprite("Background", False)
        self.player = character.player()
    def mainLoop(self):
        self.player.fillDeck()
        print(self.player.myDeck.getLength())
        self.player.myDeck.draw()
        print(self.player.myDeck.getHandLength())
        while True:
            self.handleInput()
            self.gameLogic()
            self.back()

    def handleInput(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    def gameLogic(self):
        pass



    def back(self):
        self.screen.blit(self.background, (0,0))
        if self.turns ==0:
            for i in range(5):
                self.player.myDeck.render(self.screen, i, (95+(200*i)), 1040)
        self.turns+=1
        pygame.display.flip()
