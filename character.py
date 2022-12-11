import cardOBJ
from deck import Deck
from utils import loadSprite

class character:
    myDeck = Deck()
    myClass = ""
    myHP = 0
    myDef = 0
    outMult = 1
    def __init__(self, inClass, inHP):
        self.myClass = inClass
        self.myHP = inHP
class player(character):
    def __init__(self):
        super().__init__("Machine", 30)
    def fillDeck(self):
        if (self.myClass == "Machine"):
            baseAttack = cardOBJ.attack("SteelRend", "Lash out, doing damage.", 6, "Physical", "SteelRend")
            #print(baseAttack.name)
            self.myDeck.addCard(baseAttack,5)
            baseDefense = cardOBJ.defense("MetalSkin", "Activate your metallic exoskeleton to mitigate damage.", 4,"MetalSkin")
            #print(baseDefense.name)
            self.myDeck.addCard(baseDefense, 5)
            baseDeuff=cardOBJ.debuff("ImposedRust", "Actively rust your adversary's weapons, making them do less damage.", 0, 3, 0.75,"ImposedRust")
            #print(baseDeuff.name)
            self.myDeck.addCard(baseDeuff, 2)
            baseBuff = cardOBJ.buff("TemperSteel", "Actively re-temper your blade, making it do more damage.", 0, 3, 1.25,"TemperSteel")
            #print(baseBuff.name)
            self.myDeck.addCard(baseBuff, 2)
            baseSpecial = cardOBJ.buff("AdaptiveConstruction", "Analyze incoming damage and become resistant to it.", 0, 2, 0.25,"AdaptiveConstruction")
            #print(baseSpecial.name)
            self.myDeck.addCard(baseSpecial, 1)

        #elif(self.myClass=="Homonculus"):

        #elif(self.myClass=="Elemental"):

class enemy(character):
    def __init__(self, inClass):
        self.myClass=inClass
        self.myHP = 15
    def fillEDeck(self):
        if (self.myClass== "Melee"):
            meleeA=cardOBJ.attack("Slash", "Enemy swings at you, doing damage.", 5, "Physical","Placeholder")
            self.myDeck.addCard(meleeA, 7)
            meleeD = cardOBJ.defense("Defend", "Enemy blocks your incoming strike, reducing damage taken", 3,"Placeholder")
            self.myDeck.addCard(meleeD,7)
            meleeS = cardOBJ.buff("Bleeding Strike","The next strike will bleed, dealing damage over time.", 1, 3 ,"Placeholder")
            self.myDeck.addCard(meleeS,1)
            self.myDeck.shuffle()
        elif(self.myClass =="Tank"):
            tankA=cardOBJ.attack("Bash", "Enemy bashes you with its shield, doing damage.", 3, "Physical","Placeholder")
            self.myDeck.addCard(tankA, 5)
            tankD = cardOBJ.defense("Shield Raise", "Enemy raises its shield, reducing damage taken", 10,"Placeholder")
            self.myDeck.addCard(tankD,9)
            tankS = cardOBJ.debuff("Shield Wall","The enemy raises its shield, fully protecting itself.", 1, 1, 1.00,"Placeholder")
            self.myDeck.addCard(tankS,1)
            self.myDeck.shuffle()
        elif (self.myClass == "Dummy"):
                doNothing= cardOBJ.card("Does Nothing", "Does Nothing","Placeholder")
                self.myDeck.addCard(doNothing, 15)