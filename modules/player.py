import pygame
from pygame.math import Vector2


class Player:
  def __init__(self):
    self.Position = Vector2(0,0)
    self.Coins = 0
    self.Sprite = pygame.image.load("placehold").convert_alpha()

