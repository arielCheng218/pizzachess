import chess
from pygame.event import *
from pygame.locals import *
import pygame
from utils import *
from assets.colors import *
from classes.Chessboard import Chessboard
from search import *

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
  chessboard = Chessboard(BOARD_SIZE, SQUARE_SIZE, SQUARE_NAMES)
  # pygame setup
  pygame.init()
  pygame.display.set_caption("pizzachess")
  screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
  # chess setup
  setup_chessboard(chessboard, screen, SQUARE_NUMBERS, SQUARE_LETTERS)

  clicked_square = None
  prev_highlighted_square = None

  while running and not board.is_game_over():
    if board.turn == chess.BLACK:
      move_uci = choose_move(board, 2, -1)
      board.push_uci(move_uci)
      chessboard.make_move(screen, move_uci, get_en_passant(board))
      # highlight just moved square
      chessboard.get_square_from_name(move_uci[2:4]).draw(screen, SQUARE_SIZE, 'j')
      prev_highlighted_square = chessboard.get_square_from_name(move_uci[2:4])
    else:
      # input move
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
          clicked_square = chessboard.get_square(event.pos[0], event.pos[1])
        if event.type == MOUSEBUTTONUP:
          if prev_highlighted_square != None: 
            prev_highlighted_square.draw(screen, SQUARE_SIZE)
          if chessboard.selected_piece is None: square = clicked_square.name # handle cases after deselect
          else: square = chessboard.selected_piece.square.name
          if chessboard.handle_click(screen, clicked_square, get_legal_target_squares(square, board)):
            move_uci = chessboard.selected_piece.square.name + clicked_square.name
            move_uci += chessboard.handle_promotion(move_uci)
            board.push_uci(move_uci)
            chessboard.make_move(screen, move_uci[:4], get_en_passant(board))
            chessboard.selected_piece = None
    pygame.display.flip()
  else:
    print(board.outcome())

if __name__ == "__main__":
  main()