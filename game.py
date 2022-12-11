import random

import deck
import character
import cardOBJ
import pygame as pygame
from utils import loadSprite
BLACK = (0,0,0)
WHITE = (255,255,255)
class Label():
    def __init__(self, text, location, font_size=48, color=BLACK):
        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.rendered_text = self.font.render(text, True, color)
        self.text_rect = self.rendered_text.get_rect().move(location)

    def render(self, screen):
        screen.blit(self.rendered_text, self.text_rect)
    def updateLabel(self,text):
        self.rendered_text=self.font.render(text,True,BLACK)


class Button(Label):
    def __init__(self, text, location, value=0, font_size=36, text_color=BLACK, background_color=WHITE, border_color=BLACK):
        super().__init__(text, location, font_size, text_color)
        self.background_rect = self.text_rect.inflate(10, 10)
        self.border_rect = self.background_rect.inflate(2, 2)
        self.background_color = background_color
        self.border_color = border_color
        self.text = text
        self.value = value
    def render(self, screen):
        screen.fill(self.border_color, self.border_rect)
        screen.fill(self.background_color, self.background_rect)
        super().render(screen)
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
        self.enemyOnField=self.dummy
        self.dummyBTN = Button("Spawn Dummy",(0,20))
        self.meleeBTN = Button("Spawn Melee", (0,81))
        self.tankBTN = Button("Spawn Tank", (0,142))
        self.playerHPLBL = Label(f"Player HP: {self.player.myHP}", (230,100))
        self.enemyHPLBL = Label(f"Enemy HP: {self.enemyOnField.myHP}", (830,60))



    def mainLoop(self):
        self.player.fillDeck()
        self.player.myDeck.setDeck()
        self.dummy.fillEDeck()
        self.melee.fillEDeck()
        self.tank.fillEDeck()
        random.shuffle(self.player.myDeck.uDeck)
        self.player.myDeck.draw()
        while True:
            if(len(self.player.myDeck.hand)==0):
                self.player.myDeck.draw()
            self.screen.blit(self.background, (0,0))
            self.dummyBTN.render(self.screen)
            self.meleeBTN.render(self.screen)
            self.tankBTN.render(self.screen)
            self.playerHPLBL.render(self.screen)
            self.enemyHPLBL.render(self.screen)
            self.playerHPLBL.updateLabel(f"Player HP: {self.player.myHP}")
            self.enemyHPLBL.updateLabel(f"Enemy HP: {self.enemyOnField.myHP}")
            self.screen.blit(loadSprite("Machine", True), (100,120))
            if (self.enemyOnField==self.dummy):
                self.screen.blit(loadSprite("Dummy", True), (800, 100))
            elif (self.enemyOnField==self.melee):
                self.screen.blit(loadSprite("Melee", True), (800, 100))
            elif (self.enemyOnField==self.tank):
                self.screen.blit(loadSprite("Tank", True), (800, 100))
            for i in range(len(self.player.myDeck.hand)):
                self.screen.blit(getattr(self.player.myDeck.hand[i], 'sprite'), ((95 + (251 * i)), 600))
            if (self.enemyOnField.myHP<=0):
                self.enemyOnField.reset()
            self.handleInput()
            self.gameLogic()
            self.back()
    def doEnemyPlay(self, inType, inCard, inTarget):
        if (inType == cardOBJ.attack):
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.player)
        elif (inType == cardOBJ.defense):
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.enemyOnField)
        elif (inType == cardOBJ.buff):
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.enemyOnField)
        elif (inType == cardOBJ.debuff):
            inCard.play(self.enemyOnField)
            x = random.randint(0, 14)
            enemyTempCard = self.enemyOnField.myDeck.uDeck[x]
            enemyTempCard.play(self.player)
    def doCardPlay(self,inType,inCard):
        if (inType == cardOBJ.attack):
            inCard.play(self.enemyOnField)
            x = random.randint(0, 14)
            self.doEnemyPlay(type(self.enemyOnField.myDeck.uDeck[x]),self.enemyOnField.myDeck.uDeck[x],self.player)
        elif (inType == cardOBJ.defense):
            inCard.play(self.player)
            x = random.randint(0, 14)
            self.doEnemyPlay(type(self.enemyOnField.myDeck.uDeck[x]),self.enemyOnField.myDeck.uDeck[x],self.player)
        elif (inType == cardOBJ.buff):
            inCard.play(self.player)
            x = random.randint(0, 14)
            self.doEnemyPlay(type(self.enemyOnField.myDeck.uDeck[x]),self.enemyOnField.myDeck.uDeck[x],self.player)
        elif (inType == cardOBJ.debuff):
            inCard.play(self.enemyOnField)
            x = random.randint(0, 14)
            self.doEnemyPlay(type(self.enemyOnField.myDeck.uDeck[x]),self.enemyOnField.myDeck.uDeck[x],self.player)

    def handleInput(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    tempCard= self.player.myDeck.hand[0]
                    tempType = type(tempCard)
                    self.doCardPlay(tempType,tempCard)
                    self.player.myDeck.hand.pop(0)
                if event.key == pygame.K_2:
                    if (self.player.myDeck.getHandLength()>=2):
                        tempCard=self.player.myDeck.hand[1]
                        tempType = type(tempCard)
                        self.doCardPlay(tempType, tempCard)
                        self.player.myDeck.hand.pop(1)
                if event.key == pygame.K_3:
                    if (self.player.myDeck.getHandLength()>=3):
                        tempCard = self.player.myDeck.hand[2]
                        tempType = type(tempCard)
                        self.doCardPlay(tempType, tempCard)
                        self.player.myDeck.hand.pop(2)
                if event.key == pygame.K_4:
                    if(self.player.myDeck.getHandLength()>=4):
                        tempCard = self.player.myDeck.hand[3]
                        tempType = type(tempCard)
                        self.doCardPlay(tempType, tempCard)
                        self.player.myDeck.hand.pop(3)
                if event.key == pygame.K_5:
                    if (self.player.myDeck.getHandLength()>=5):
                        tempCard = self.player.myDeck.hand[4]
                        tempType = type(tempCard)
                        self.doCardPlay(tempType, tempCard)
                        self.player.myDeck.hand.pop(4)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.dummyBTN.border_rect.collidepoint(event.pos)):
                    self.enemyOnField = self.dummy
                elif (self.meleeBTN.border_rect.collidepoint((event.pos))):
                    self.enemyOnField=self.melee
                elif(self.tankBTN.border_rect.collidepoint(event.pos)):
                    self.enemyOnField=self.tank





    def gameLogic(self):
        pass



    def back(self):
        pygame.display.flip()
