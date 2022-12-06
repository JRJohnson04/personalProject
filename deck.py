import cardOBJ as cardOBJ
import random
from utils import loadSprite
import numpy
class deck():
    uDeck = []
    discard = []
    def __init__(self, inDeck):
        self.uDeck = inDeck
    def addCard(self,aCard, count):
        for i in count:
            self.uDeck.append(aCard)
    def shuffle(self):
        self.uDeck.shuffle()
    def draw(self):
        for i in range(5):
            self.discard.append(self.uDeck[i])
            self.uDeck.del(i)
            if (numpy.size(self.uDeck) == 0):
                self.uDeck=self.discard
                self.uDeck.shuffle()
