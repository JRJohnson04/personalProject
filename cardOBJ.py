from utils import loadSprite
class card:
    name = ""
    flavorText = ""
    played = 0
    drawn = 0
    sprite = ""
    def __init__(self, inName, inText, inSprite):
        self.name = inName
        self.flavorText = inText
        self.sprite = inSprite
    def __str__(self):
        return self.name
    def play(self,target):
        pass
class attack(card):
    damage = 0
    damageType = ""
    def __init__(self, inName, inText, inDamage, inType,inSprite):
        self.name = inName
        self.flavorText = inText
        self.damage = inDamage
        self.damageType = inType
        self.sprite = inSprite

    def play(self, target):
            target.myHP=target.myHP-self.damage



class defense(card):
    armor = 0
    def __init__(self, inName, inText, inArmor,inSprite):
        self.name = inName
        self.flavorText = inText
        self.armor = inArmor
        self.sprite = inSprite

    def play(self, target):
           target.myHP += self.armor



class effect(card):
    isDOT = 0
    duration = 0
    def __init__(self, inName, inText,inDOT, inDuration,inSprite):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
        self.sprite = inSprite
class buff(effect):
    buff = 0
    def __init__(self, inName, inText, inDOT, inDuration, inBuff,inSprite):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
        self.buff = inBuff
        self.sprite = inSprite


    def play(self,target):
            target.outMult = buff


class debuff(effect):
    debuff = 0
    def __init__(self,inName, inText,  inDOT, inDuration, inDebuff,inSprite):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
        self.debuff = inDebuff
        self.sprite = inSprite


    def play(self, target):
            target.myDef -=(target.myDef * self.debuff)