import chess

# main.py

# setup
def get_square_names(SQUARE_NUMBERS, SQUARE_LETTERS):
  square_names = []
  for n in SQUARE_NUMBERS:
    for char in SQUARE_LETTERS:
        square_names.append(char + n)
  return square_names

# logic
def get_legal_target_squares(square, board):
  legal_target_squares = []
  for legal_move in list(board.legal_moves):
    if str(legal_move.uci())[:2] == square.name[:2]:
      legal_target_squares.append(str(legal_move.uci())[2:4])
  return legal_target_squares