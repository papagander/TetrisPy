lShape = [
    [(0,1), (1,1), (2,1), (3,1)],
    [(3,0), (3,1), (3,2), (3,3)],
    [(0,2), (1,2), (2,2), (3,2)],
    [(1,0), (1,1), (1,2), (1,3)]
]
oShape = [
    [(1,0), (2,0), (1,1), (2,1)],
    [(1,0), (2,0), (1,1), (2,1)],
    [(1,0), (2,0), (1,1), (2,1)],
    [(1,0), (2,0), (1,1), (2,1)]
]
tShape = [
    [(1,1), (0,2), (1,2), (2,2)],
    [(1,0), (1,1), (2,1), (1,2)],
    [(0,1), (1,1), (2,1), (1,2)],
    [(1,0), (0,1), (1,1), (1,2)]
]



def getShape(shapeNum, rot):
    match shapeNum:
        case 1: return lShape[rot]
        case 2: return oShape[rot]
        case 3: return tShape[rot]
        case 4: return lShape[rot]
        case 5: return oShape[rot]
        case 6: return tShape[rot]
        case 7: return lShape[rot]



