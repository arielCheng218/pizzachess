from utils import *
from assets.colors import *
from classes.Chessboard import Chessboard
import chess
import pygame
from pygame.locals import *

# constants
BOARD_SIZE = 600
SQUARE_SIZE = int(BOARD_SIZE / 8)
SQUARE_NUMBERS = [str(x) for x in range(8, 0, -1)]
SQUARE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
SQUARE_NAMES = get_square_names(SQUARE_NUMBERS, SQUARE_LETTERS)

def main():
  # globals
  running = True
  board = chess.Board()
  chessboard = Chessboard(BOARD_SIZE, SQUARE_SIZE, SQUARE_NAMES, board.fen)
  # pygame setup
  pygame.init()
  pygame.display.set_caption("pizzachess")
  screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
  # chess setup
  chessboard.draw_board(screen)
  chessboard.init_pieces()
  chessboard.init_squares(SQUARE_NUMBERS, SQUARE_LETTERS)
  chessboard.draw_starting_pieces(screen)

  clicked_square = None

  # main loop
  while running and not board.is_game_over():
    if board.turn == chess.BLACK:
      # generate move
      # make move
      # display move
      pass
    else:
      # input move
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
          clicked_square = chessboard.get_square(event.pos[0], event.pos[1])
        if event.type == MOUSEBUTTONUP:
          if chessboard.selected_piece is None: square = clicked_square.name
          else: square = chessboard.selected_piece.square.name
          chessboard.handle_click(screen, clicked_square, get_legal_target_squares(square, board))
      # make move
      # display move
      
      # generate move
      # make move
      # display move
    pygame.display.flip()
  else:
    print(board.outcome())

if __name__ == "__main__":
  main()