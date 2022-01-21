from utils import *
from assets.colors import *
import chess
import pygame

# constants
BOARD_SIZE = 600
SQUARE_SIZE = int(BOARD_SIZE / 8)
SQUARE_NUMBERS = [str(x) for x in range(8, 0, -1)]
SQUARE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
SQUARE_NAMES = [get_square_names(SQUARE_NUMBERS, SQUARE_LETTERS)]

board = chess.Board()

def main():
  # pygame setup
  pygame.init()
  screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
  # main loop
  while True:
    screen.fill(BLACK)
    pygame.display.flip()

if __name__ == "__main__":
  main()