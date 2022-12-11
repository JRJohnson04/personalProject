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
        if (self.played==0):
            self.played=1
            target.myHP-= self.damage
    def place(self, surface, position, sprite):
        surface.blit(sprite,position )


class defense(card):
    armor = 0
    def __init__(self, inName, inText, inArmor,inSprite):
        self.name = inName
        self.flavorText = inText
        self.armor = inArmor
        self.sprite = inSprite

    def play(self,target):
        if (self.played==0):
            self.played=1
            target.myDef += self.armor



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
        if (self.played==0):
            self.played=1
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
        if (self.played==0):
            self.played=1
            target.myDef -=(target.myDef * self.debuff)