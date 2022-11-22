import cardOBJ as cardOBJ

class deck():
    uDeck = []
    def __init__(self, inDeck):
        self.uDeck = inDeck
    def addCard(self,aCard, count):
        for i in count:
            self.uDeck.append(aCard)