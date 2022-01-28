import random
import chess
import chess.polyglot as book
from evaluate import *

searched_position_evals = {}

def choose_move(board, depth, color):
  # TODO: endgame database
  best_move = ""
  best_eval = float('inf') * -color
  if check_opening_book(board)[0]: return check_opening_book(board)[1].uci()
  for move in list(board.legal_moves):
    print(f"evaluating {move}")
    board.push_uci(move.uci())
    eval = minimax(board, depth, color)
    print(eval)
    if color == 1: 
      best_eval = max(best_eval, eval) 
    else: 
      best_eval = min(best_eval, eval)
    if best_eval == eval: 
      best_move = move
    board.pop()
  return best_move.uci()

def check_opening_book(board):
  with book.open_reader("assets/openings.bin") as reader:
    if len(list(reader.find_all(board))) == 0:
      return (False, "")
    else:
      return (True, list(reader.find_all(board))[random.choice(range(0, len(list(reader.find_all(board)))))].move)

def minimax(board, depth, color):
  if depth == 0: 
    return evaluate(board)
  elif board.fen in searched_position_evals: 
    return searched_position_evals[board.fen]
  else:
    value = -float('inf')
    for move in list(board.legal_moves):
      board.push_uci(move.uci())
      value = max(value, minimax(board, depth - 1, -color))
      board.pop()
    return value