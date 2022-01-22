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
  # state
  select = False
  selected_piece = None
  start_square = None
  target_square = None

  # main loop
  while running and not board.is_game_over():
    if board.turn == chess.BLACK:
      # generate move
      # make move
      # display move
      pass
    else:
      # chessboard.squares[0].draw(screen, LIGHT_LEGAL_SQUARE, SQUARE_SIZE)
      # input move
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
          if not select:
            start_square = chessboard.get_square(event.pos[0], event.pos[1])
          if not start_square.piece is None:
            select = not select
            selected_piece = start_square.piece
            print(selected_piece.name)
        if event.type == MOUSEBUTTONUP:
          if select:
            for square_name in get_legal_target_squares(start_square, board):
              i = SQUARE_NAMES.index(square_name)
              square = chessboard.squares[i]
              if square.is_light:
                square.draw(screen, LIGHT_LEGAL_SQUARE, SQUARE_SIZE)
              else:
                square.draw(screen, DARK_LEGAL_SQUARE, SQUARE_SIZE)
          else:
            for square_name in get_legal_target_squares(start_square, board):
              i = SQUARE_NAMES.index(square_name)
              square = chessboard.squares[i]
              if square.is_light:
                square.draw(screen, LIGHT, SQUARE_SIZE)
              else:
                square.draw(screen, DARK, SQUARE_SIZE)

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