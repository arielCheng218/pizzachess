import pygame
from classes.Piece import Piece
from classes.Square import Square
from assets.colors import *

class Chessboard:

  def __init__(self, BOARD_SIZE, SQUARE_SIZE, SQUARE_NAMES, fen):
    self.BOARD_SIZE = BOARD_SIZE
    self.SQUARE_SIZE = SQUARE_SIZE
    self.SQUARE_NAMES = SQUARE_NAMES
    self.pieces = []
    self.squares = []
    self.square_colors = []
    self.selected_piece = None
    self.fen = fen

  def draw_board(self, screen):
    light = True
    for y in range(0, self.BOARD_SIZE, self.SQUARE_SIZE):
      light = not light
      for x in range(0, self.BOARD_SIZE, self.SQUARE_SIZE):
        light = not light
        if light: color = LIGHT; self.square_colors.append(True)
        else: color = DARK; self.square_colors.append(False)
        pygame.draw.rect(screen, color, pygame.Rect((x, y, x + self.SQUARE_SIZE, y + self.SQUARE_SIZE)))
    pygame.display.flip()

  def init_pieces(self):
    id = 0
    for piece_name in ["R", "N", "B", "Q", "K", "B", "N", "R"] + ["P"] * 8:
      self.pieces.append(Piece(f"b{piece_name}{id}", "b", f"assets/pieces/b{piece_name}.png", None))
      id += 1
    for piece_name in ["P"] * 8 + ["R", "N", "B", "Q", "K", "B", "N", "R"]:
      self.pieces.append(Piece(f"w{piece_name}{id}", "w", f"assets/pieces/w{piece_name}.png", None))
      id += 1
  
  def init_squares(self, SQUARE_NUMBERS, SQUARE_LETTERS):
    for square_name in self.SQUARE_NAMES:
      i = self.SQUARE_NAMES.index(square_name)
      x = SQUARE_LETTERS.index(square_name[0]) * self.SQUARE_SIZE
      y = SQUARE_NUMBERS.index(square_name[1]) * self.SQUARE_SIZE
      self.squares.append(Square(square_name, x, y, self.square_colors[i], None))

  def draw_starting_pieces(self, screen):
    i = 0
    for square in self.squares:
      if "8" in square.name or "7" in square.name or "2" in square.name or "1" in square.name:
        piece = self.pieces[i]
        piece.draw(screen, square.x, square.y, square)
        square.piece = piece
        i += 1

  def get_square(self, x, y):
    for square in self.squares:
      if x >= square.x and y >= square.y and x <= square.x + self.SQUARE_SIZE and y <= square.y + self.SQUARE_SIZE:
        return square
  
  def get_square_from_name(self, name):
    i = self.SQUARE_NAMES.index(name)
    return self.squares[i]

  def draw_legal_squares(self, screen, legal_squares, reverse):
    type = None
    if not reverse: type = 'l'
    for square in legal_squares:
      square.draw(screen, self.SQUARE_SIZE, type)

  def handle_click(self, screen, square, legal_square_names):
    legal_squares = [self.get_square_from_name(x) for x in legal_square_names]
    if self.selected_piece is None and not square.piece is None and square.piece != self.selected_piece:
      self.selected_piece = square.piece
      square.draw(screen, self.SQUARE_SIZE, 's')
      self.draw_legal_squares(screen, legal_squares, reverse=False)
    elif square.name in legal_square_names:
      print(square.name, " is legal move")
      pass
    else:
      self.selected_piece.square.draw(screen, self.SQUARE_SIZE)
      self.draw_legal_squares(screen, legal_squares, reverse=True)
      self.selected_piece = None