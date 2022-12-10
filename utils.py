from pygame.image import load
from pathlib import Path

def loadSprite(name, with_Alpha= True):
    filename=Path("assets/sprites/" + name + ".png")
    sprite = load(filename.resolve())
    if with_Alpha:
        return sprite.convert_alpha()
    return sprite.convert()