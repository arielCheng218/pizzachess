from assets.colors import DARK, DARK_JUST_MOVED, DARK_LEGAL_SQUARE, DARK_START_SQUARE, LIGHT, LIGHT_JUST_MOVED, LIGHT_LEGAL_SQUARE, LIGHT_START_SQUARE
import pygame

class Square:
  def __init__(self, name, x, y, is_light, piece):
    self.name = name
    self.x = x
    self.y = y 
    self.is_light = is_light
    self.piece = piece

  def draw(self, screen, SQUARE_SIZE, color_type=None):
    if color_type == 's':
      if self.is_light: color = LIGHT_START_SQUARE
      else: color = DARK_START_SQUARE
    elif color_type == 'l':
      if self.is_light: color = LIGHT_LEGAL_SQUARE
      else: color = DARK_LEGAL_SQUARE
    elif color_type == 'j':
      if self.is_light: color = LIGHT_JUST_MOVED
      else: color = DARK_JUST_MOVED
    else:
      if self.is_light: color = LIGHT
      else: color = DARK
    pygame.draw.rect(screen, color, pygame.Rect((self.x, self.y, SQUARE_SIZE, SQUARE_SIZE)))
    if not self.piece is None:
      self.piece.draw(screen, self.x, self.y)