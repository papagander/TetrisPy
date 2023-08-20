#! /~/Projects/TetrisPy/bin/python
import random
import pygame
import pieces as p
import graphics as graphics
import game as game
pygame.init()


def HandleKey(key):
    if key == pygame.K_q:
        pygame.quit


clock = pygame.time.Clock()
board = game.emptyBoard()
running = True
graphics.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            HandleKey(event.key)

    graphics.update(board)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
