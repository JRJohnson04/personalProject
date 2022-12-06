from utils import loadSprite
import character
class card:
    name = ""
    flavorText = ""
    played = 0
    def __init__(self, inName, inText, inSprite):
        self.name = inName
        self.flavorText = inText
        self.sprite = loadSprite(inSprite, True)

class attack(card):
    damage = 0
    damageType = ""
    def __init__(self, inName, inText, inDamage, inType):
        self.name = inName
        self.flavorText = inText
        self.damage = inDamage
        self.damageType = inType
    def play(self, target):
        if (self.played==0):
            self.played=1
            target.myHP-= self.damage

class defense(card):
    armor = 0
    def __init__(self, inName, inText, inArmor):
        self.name = inName
        self.flavorText = inText
        self.armor = inArmor
    def play(self,target):
        if (self.played==0):
            self.played=1
            target.myDef += self.armor



class effect(card):
    isDOT = 0
    duration = 0
    def __init__(self, inName, inText,inDOT, inDuration):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
class buff(effect):
    buff = 0
    def __init__(self, inName, inText, inDOT, inDuration, inBuff):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
        self.buff = self.inBuff
    def play(self,target):
        if (self.played==0):
            self.played=1
            target.outMult = buff


class debuff(effect):
    debuff = 0
    def __init__(self,inName, inText,  inDOT, inDuration, inDebuff):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
        self.debuff = self.inDebuff
    def play(self, target):
        if (self.played==0):
            self.played=1
            target.myDef -=(target.myDef * self.debuff)