import chess
import random

# setup
def get_square_names(SQUARE_NUMBERS, SQUARE_LETTERS):
  square_names = []
  for n in SQUARE_NUMBERS:
    for char in SQUARE_LETTERS:
        square_names.append(char + n)
  return square_names

def setup_chessboard(chessboard, screen, SQUARE_NUMBERS, SQUARE_LETTERS):
  chessboard.draw_board(screen)
  chessboard.init_pieces()
  chessboard.init_squares(SQUARE_NUMBERS, SQUARE_LETTERS)
  chessboard.draw_starting_pieces(screen)

# logic
def get_legal_target_squares(square, board):
  legal_target_squares = []
  for legal_move in list(board.legal_moves):
    if str(legal_move.uci())[:2] == square[:2]:
      legal_target_squares.append(str(legal_move.uci())[2:4])
  return legal_target_squares

def get_en_passant(board):
  if board.has_legal_en_passant():
    return chess.square_name(board.ep_square)

def get_random_move(board):
  move = random.choice([x.uci() for x in list(board.legal_moves)])
  return move