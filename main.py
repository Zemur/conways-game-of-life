import pygame
import sys
from game_of_life import GameOfLife
import colors

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    WIDTH = 1920
    HEIGHT = 1080

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    conway = GameOfLife(screen, scale=13)

    clock = pygame.time.Clock()
    fps = 60

    while True:
        clock.tick(fps)
        screen.fill(colors.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        conway.run()

        pygame.display.update()
