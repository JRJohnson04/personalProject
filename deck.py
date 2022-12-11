import numpy
import cardOBJ
from utils import loadSprite
import random
import pygame
class Deck():
    uDeck = []
    discard = []
    hand = []
    def __init__(self):
        self.uDeck = []
        self.discard = []
        self.hand = []
    def getLength(self):
        return len(self.uDeck)
    def getHandLength(self):
        return len(self.hand)
    def getSprite(self, i ):
        myType= type(self.uDeck[i])
        if (myType== cardOBJ.card):
            return cardOBJ.card.name
    def addCard(self,aCard, count):
        for i in range(count):
            self.uDeck.append(aCard)
    def getIndex(self, search):
        for i in range(len(self.hand)):
            if(self.hand[i]==search):
                return i
    def removeFromHand(self, i):
        self.hand.pop(i)
    def render(self,screen, i, x,y):
        sprite = loadSprite(getattr(self.hand[i], 'name'), False)
        screen.blit(sprite, (x,y))

    def draw(self):
        for i in range(5):
            self.discard.append(self.uDeck[i])
            self.hand.append(self.uDeck[i])
            self.uDeck[i].drawn = 1
            self.uDeck.pop(i)
            if (numpy.size(self.uDeck) == 0):
                self.uDeck=self.discard
                #random.shuffle(self.uDeck)
                for j in self.uDeck:
                    self.uDeck[j].drawn = 0