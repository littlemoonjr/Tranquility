import pygame, sys, threading



class Game:
  def __init__(self):
    self.Screen = pygame.display.set_mode((1980,1080))

  def check_event(self) -> None:
    """
    Checks all current events and enters them within game loop
    """

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_over()

  def game_over(self) -> None:
    """
    Stops all events, closes the game.
    """

  pygame.quit()
  sys.exit()

Local_Game = Game()
