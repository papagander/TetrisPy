#! /~/Projects/TetrisPy/bin/python
import random
import pygame

pygame.init()
WIDTH = 600
HEIGHT = 800
MIDWIDTH = WIDTH / 2
MIDHEIGHT = HEIGHT / 2
CELLSIZE = 28
BOARDWIDTH = CELLSIZE * 10
BOARDHEIGHT = CELLSIZE * 20
FRAMEWIDTH = BOARDWIDTH + 10
FRAMEHEIGHT = BOARDHEIGHT + 10
frameOrigin = (MIDWIDTH -FRAMEWIDTH/2, MIDHEIGHT -FRAMEHEIGHT/2) 
boardOrigin = (FRAMEWIDTH/2 -BOARDWIDTH/2, FRAMEHEIGHT/2 -BOARDHEIGHT/2)
frameSurface = pygame.Surface((FRAMEWIDTH, FRAMEHEIGHT))
boardSurface = pygame.Surface((BOARDWIDTH, BOARDHEIGHT))

def getColor(num):
    match num:
        case 1: return pygame.Color(26, 163, 212)
        case 2: return pygame.Color(251, 242, 54)
        case 3: return pygame.Color(118, 66, 138)
        case 4: return pygame.Color(73, 193, 72)
        case 5: return pygame.Color(223, 113, 38)
        case 6: return pygame.Color(91, 110, 225)
        case 7: return pygame.Color(228, 104, 19)

def HandleKey(event):
    if event.key == pygame.K_q:
        pygame.quit


def renderBoard(board, surface: pygame.Surface):
    frameSurface.fill('brown')
    boardSurface.fill('black')

    for i in range(len(board)) :
        row = board[i]
        for n in range(len(row)):
            color = getColor(board[i][n])
            if color is not None:
                cellOrigin = CELLSIZE * n, CELLSIZE * i
                cellSurface = pygame.Surface((CELLSIZE, CELLSIZE))
                cellSurface.fill(color)
                boardSurface.blit(cellSurface, cellOrigin)
    
    frameSurface.blit(boardSurface, boardOrigin)
    surface.blit(frameSurface, frameOrigin)


def randomBoard():
    board = emptyBoard()
    for i in range(len(board)):
        row = board[i]
        for n in range(len(row)):
            board[i][n] = random.randint(1,7)
    return board


def emptyBoard():
    return \
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0],\
    [0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0,0o0]


print(randomBoard())
screen = pygame.display.set_mode(( WIDTH, HEIGHT))
clock = pygame.time.Clock()
#board = emptyBoard()
board = randomBoard()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill((60, 140, 180))
    renderBoard(board, screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

