import pygame
WIDTH = 600
HEIGHT = 800
MIDWIDTH = WIDTH / 2
MIDHEIGHT = HEIGHT / 2
CELLSIZE = 28
BOARDWIDTH = CELLSIZE * 10
BOARDHEIGHT = CELLSIZE * 22
FRAMEWIDTH = BOARDWIDTH + 10
FRAMEHEIGHT = BOARDHEIGHT + 10
frameOrigin = (MIDWIDTH -FRAMEWIDTH/2, MIDHEIGHT -FRAMEHEIGHT/2) 
boardOrigin = (FRAMEWIDTH/2 -BOARDWIDTH/2, FRAMEHEIGHT/2 -BOARDHEIGHT/2)
cellOrigin = (frameOrigin[0] + boardOrigin[0], frameOrigin[1] + boardOrigin[1])
frameSurface = pygame.Surface((FRAMEWIDTH, FRAMEHEIGHT))
boardSurface = pygame.Surface((BOARDWIDTH, BOARDHEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill('skyblue')

def init():
    global screen
    frameSurface.fill('brown')
    boardSurface.fill('gray')
    frameSurface.blit(boardSurface, boardOrigin)
    screen.blit(frameSurface, frameOrigin)


def getColor(num):
    match num:
        case 1: return pygame.Color(26, 163, 212)
        case 2: return pygame.Color(251, 242, 54)
        case 3: return pygame.Color(118, 66, 138)
        case 4: return pygame.Color(73, 193, 72)
        case 5: return pygame.Color(223, 113, 38)
        case 6: return pygame.Color(91, 110, 225)
        case 7: return pygame.Color(228, 104, 19)


def update(board):
    global screen
    for i in range(len(board)) :
        row = board[i]
        for n in range(len(row)):
            color = getColor(board[i][n])
            if color is not None:
                curCellOrigin = CELLSIZE * n + cellOrigin[0], CELLSIZE * i + cellOrigin[1]
                cellSurface = pygame.Surface((CELLSIZE, CELLSIZE))
                cellSurface.fill(color)
                screen.blit(cellSurface, curCellOrigin)



