import pygame
import modules.manager as manager

pygame.init()

def start():
  Game = manager.Local_Game

  while True:
    Game.check_events()



if __name__ == "__main__":
  start()
