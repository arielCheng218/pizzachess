# TODO: Evaluation function genetic algorithms to fine-tune parameters
import chess

def evaluate(pos):
  if not pos.is_game_over():
    material = get_material_points(pos.fen())
    king_safety = get_king_safety(pos)
    center_control = get_center_control(pos)
    return 2 * material + king_safety + center_control
  elif pos.is_checkmate():
    if pos.turn == chess.WHITE:
      return -float('inf')
    else:
      return float('inf')
  elif pos.is_stalemate():
    return 0

piece_values = {
    "P": 10,
    "N": 30,
    "B": 40,
    "R": 50,
    "Q": 80,
    "p": -10,
    "n": -30,
    "b": -40,
    "r": -50,
    "q": -80,
  }

def get_material_points(fen):
  value = 0
  global piece_values
  for char in fen:
    if char in piece_values:
      value += piece_values[char]
  return value

def get_king_safety(pos):
  if pos.turn == chess.WHITE and pos.is_check():
    return -1
  elif pos.turn == chess.BLACK and pos.is_check():
    return 1
  else:
    return 0

def get_center_control(pos):
  return len(list(pos.legal_moves)) * 0.1