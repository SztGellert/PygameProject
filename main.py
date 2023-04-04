import pygame
from sys import exit




if __name__ == '__main__':
   pygame.init()
   screen = pygame.display.set_mode((800, 400))

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            exit()

      pygame.display.update()