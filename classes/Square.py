import pygame

class Square:
  def __init__(self, name, x, y, is_light, piece):
    self.name = name
    self.x = x
    self.y = y 
    self.is_light = is_light
    self.piece = piece

  def draw(self, screen, color, SQUARE_SIZE):
    print(f"draw over {self.name}")
    pygame.draw.rect(screen, color, pygame.Rect((self.x, self.y, self.x + SQUARE_SIZE, self.y + SQUARE_SIZE)))
    if not self.piece is None:
      self.piece.draw(screen, self.x, self.y)
    pygame.display.update()