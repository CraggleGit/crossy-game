# Import any external libraries or classes
import pygame
from game import Game

# Initialise pygame
pygame.init()

# Create a new instance of Game class and call the game_loop function
game = Game()
game.game_loop()

# Quit pygame and quit Python
pygame.quit()
quit()