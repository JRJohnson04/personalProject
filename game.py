import random

import deck
import character
import cardOBJ
import pygame as pygame
from utils import loadSprite
class Game:
    turns = 0
    numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("A Deck of Many Stories")
        self.screen = pygame.display.set_mode((1440, 1000))
        self.background = loadSprite("Background", False)
        self.player = character.player()
        self.dummy = character.enemy("Dummy")
        self.melee = character.enemy("Melee")
        self.tank = character.enemy("Tank")



    def mainLoop(self):
        self.screen.blit(self.background, (0,0))
        self.player.fillDeck()
        self.dummy.fillEDeck()
        self.melee.fillEDeck()
        self.tank.fillEDeck()
        self.enemyOnField = self.dummy
        print(self.player.myDeck.getLength())
        random.shuffle(self.player.myDeck.uDeck)
        self.player.myDeck.draw()
        print(self.player.myDeck.getHandLength())
        while True:
            self.handleInput()
            self.gameLogic()
            self.back()

    def doCardPlay(self,inType,inCard):
        if (inType == cardOBJ.attack):
            inCard.attack.play(self.enemyOnField)
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.player)
        elif (inType == cardOBJ.defense):
            inCard.defense.play(self.player)
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.player)
        elif (inType == cardOBJ.buff):
            inCard.buff.play(self.player)
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.player)
        elif (inType == cardOBJ.debuff):
            inCard.debuff.play(self.enemyOnField)
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.player)

    def handleInput(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    tempCard= self.player.myDeck.hand[0]
                    tempType = type(tempCard)
                    self.doCardPlay(tempType,tempCard)
                if event.key == pygame.K_2:
                    tempCard=self.player.myDeck.hand[1]
                    tempType = type(tempCard)
                    self.doCardPlay(tempType, tempCard)
                if event.key == pygame.K_3:
                    tempCard = self.player.myDeck.hand[2]
                    tempType = type(tempCard)
                    self.doCardPlay(tempType, tempCard)
                if event.key == pygame.K_4:
                    tempCard = self.player.myDeck.hand[3]
                    tempType = type(tempCard)
                    self.doCardPlay(tempType, tempCard)
                if event.key == pygame.K_5:
                    tempCard = self.player.myDeck.hand[4]
                    tempType = type(tempCard)
                    self.doCardPlay(tempType, tempCard)





    def gameLogic(self):
        pass



    def back(self):
        if self.turns ==0:
            for i in range(5):
                print(getattr(self.player.myDeck.hand[i], 'sprite'))
                self.screen.blit(getattr(self.player.myDeck.hand[i], 'sprite'), ((95+(251*i)), 600))

        self.turns+=1
        pygame.display.flip()
