import pygame

class Piece:

  def __init__(self, name, color, image_path, square):
    self.name = name
    self.color = color
    self.image = pygame.image.load(image_path)
    self.square = square

  def draw(self, screen, x, y, square = None):
    screen.blit(self.image, (x, y))
    if square != None:
      self.square = square
    pygame.display.update()