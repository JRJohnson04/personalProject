import cardOBJ
import deck
from utils import loadSprite
import random

class character:
    myClass = ""
    myHP = 0
    myDef = 0
    outMult = 1
    def __init__(self, inClass, inHP):
        self.myClass = inClass
        self.myHP = inHP
        self.myDeck = deck.Deck()

class player(character):
    def __init__(self):
        super().__init__("Machine", 30)
    def fillDeck(self):
        if (self.myClass == "Machine"):
            sprite1 = loadSprite("SteelRend",False)
            baseAttack = cardOBJ.attack("SteelRend", "Lash out, doing damage.", 6, "Physical", sprite1)
            #print(baseAttack.name)
            sprite2 = loadSprite("MetalSkin", False)
            self.myDeck.addCard(baseAttack,5)
            baseDefense = cardOBJ.defense("MetalSkin", "Activate your metallic exoskeleton to mitigate damage.", 4,sprite2)
            #print(baseDefense.name)
            self.myDeck.addCard(baseDefense, 5)
            sprite3 = loadSprite("ImposedRust", False)
            baseDeuff=cardOBJ.debuff("ImposedRust", "Actively rust your adversary's weapons, making them do less damage.", 0, 3, 0.75,sprite3)
            #print(baseDeuff.name)
            self.myDeck.addCard(baseDeuff, 2)
            sprite4 = loadSprite("TemperSteel", False)
            baseBuff = cardOBJ.buff("TemperSteel", "Actively re-temper your blade, making it do more damage.", 0, 3, 1.25,sprite4)
            #print(baseBuff.name)
            self.myDeck.addCard(baseBuff, 2)
            sprite5 = loadSprite("AdaptiveConstruction", False)
            baseSpecial = cardOBJ.buff("AdaptiveConstruction", "Analyze incoming damage and become resistant to it.", 0, 2, 0.25,sprite5)
            #print(baseSpecial.name)
            self.myDeck.addCard(baseSpecial, 1)

        #elif(self.myClass=="Homonculus"):

        #elif(self.myClass=="Elemental"):

class enemy(character):
    def __init__(self, inClass):
        self.myClass=inClass
        super().__init__(inClass,15)

    def reset(self):
        self.myHP=15
    def fillEDeck(self):
        sprite6= loadSprite("Placeholder", False)
        if (self.myClass== "Melee"):
            meleeA=cardOBJ.attack("Slash", "Enemy swings at you, doing damage.", 5, "Physical",sprite6)
            self.myDeck.addCard(meleeA, 7)
            meleeD = cardOBJ.defense("Defend", "Enemy blocks your incoming strike, reducing damage taken", 3,sprite6)
            self.myDeck.addCard(meleeD,7)
            meleeS = cardOBJ.buff("Bleeding Strike","The next strike will bleed, dealing damage over time.", 0, 3 ,1.5,sprite6)
            self.myDeck.addCard(meleeS,1)
        elif(self.myClass =="Tank"):
            tankA=cardOBJ.attack("Bash", "Enemy bashes you with its shield, doing damage.", 3, "Physical",sprite6)
            self.myDeck.addCard(tankA, 5)
            tankD = cardOBJ.defense("Shield Raise", "Enemy raises its shield, reducing damage taken", 10,sprite6)
            self.myDeck.addCard(tankD,9)
            tankS = cardOBJ.debuff("Shield Wall","The enemy raises its shield, fully protecting itself.", 1, 1, 1.00,sprite6)
            self.myDeck.addCard(tankS,1)
        elif (self.myClass == "Dummy"):
                doNothing= cardOBJ.card("Does Nothing", "Does Nothing",sprite6)
                self.myDeck.addCard(doNothing, 15)