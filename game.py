import random as rand

class Bag:
    QUEUELENGTH = 14
    bag = [0] * QUEUELENGTH
    first = 0
    last = 0
    count = 0

    def __init__(self):
        self.drawBag()
        self.drawBag()


    def printBag(self):
        print(f'[ {bag[0]}')
        for i in range(1, self.QUEUELENGTH):
            print(f', {bag[i]}')
            print(' ]')


    def drawBag(self):
        newBag = [1, 2, 3, 4, 5, 6, 7]
        for i in reversed(range(1,7)):
            j = rand.randint(0, i)
            #print(f'swapping {newBag[i]} at {i} with {newBag[j]} at {j}')
            temp = newBag[i]
            newBag[i] = newBag[j]
            newBag[j] = temp
        for p in newBag:
            print(f'inserting at {self.last}')
            self.bag[self.last] = p
            self.last = self.last + 1 if self.last + 1 < self.QUEUELENGTH else 0
        self.count += 7


    def nextPiece(self):
        piece = self.bag[self.first]
        self.first = self.first + 1 if self.first + 1 < self.QUEUELENGTH else 0
        self.count -= 1
        if self.count < 7: self.drawBag()
        return piece

class Board:
    bag = Bag()
    cursor = (2,0)
    selectedPiece = 0
    rotation = 0
    curBlockCoords = [(0,0), (0,0), (0,0), (0,0)]




def randomBoard():
    board = emptyBoard()
    for i in range(len(board)):
        row = board[i]
        for n in range(len(row)):
            board[i][n] = rand.randint(1,7)
    return board


def emptyBoard():
    board = []
    for i in range(0, 22):
        row = []
        for j in range(0, 10):
            row.append(0)
        board.append(row)
    return board


