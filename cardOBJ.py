from utils import loadSprite
class card:
    name = ""
    flavorText = ""
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

class defense(card):
    armor = 0
    def __init__(self, inName, inText, inArmor):
        self.name = inName
        self.flavorText = inText
        self.armor = inArmor



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
        self.buff = inBuff

class debuff(effect):
    debuff = 0
    def __init__(self,inName, inText,  inDOT, inDuration, inDebuff):
        self.name = inName
        self.flavorText = inText
        self.isDOT=inDOT
        self.duration=inDuration
        self.debuff = inDebuff