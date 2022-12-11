import cardOBJ
import character
import deck
import pygame as pygame
from game import Game


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player = character.player()
    storyDeck = Game()
    storyDeck.mainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
