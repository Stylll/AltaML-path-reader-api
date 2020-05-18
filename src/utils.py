import os.path

directionTypes = {
    'up': {
        'x': 0,
        'y': 1,
        'L': 'left',
        'R': 'right'
    },
    'left': {
        'x': -1,
        'y': 0,
        'L': 'down',
        'R': 'up'
    },
    'down': {
        'x': 0,
        'y': -1,
        'L': 'right',
        'R': 'left'
    },
    'right': {
        'x': 1,
        'y': 0,
        'L': 'up',
        'R': 'down'
    }
}

posX = 'x'
posY = 'y'

def readFile(filename):
    dirname = os.path.dirname(__file__)
    filePath = '../directions/{}.txt'.format(filename)
    file = open(os.path.join(dirname, filePath), 'r')
    pathStr = file.read()
    file.close()

    return pathStr

def generateBound(highestPos, lowestPos):
    posXBound = []
    posYBound = []

    for i in range(lowestPos[posX], highestPos[posX] + 1):
        posXBound.append(i)

    for j in range(lowestPos[posY], highestPos[posY] + 1):
        # inserting here because the Y axis bound has to start from the highest
        # array.reverse() doesn't handle reversing negative values well
        posYBound.insert(0, j)

    return {
        'posXBound': posXBound,
        'posYBound': posYBound
    }


def generateDirections(pathStr):
    highestPos = { 'x': 0, 'y': 0 }
    lowestPos = { 'x': 0, 'y': 0 }
    steps = [[0,0]]
    strSteps = ['0/0']
    startPos = [0,0]
    strStartPos = '0/0'
    currPos = [0,0]
    strCurrPos = '0/0'
    currDirection = directionTypes['up']
    strCurrDirection = 'up'
    multiOccurence = set()
    possibleActions = 'FLR'
    possibleTurns = 'LR'

    for s in pathStr:
        step = s.upper()
        if step not in possibleActions:
            continue

        if step in possibleTurns:
            strCurrDirection = currDirection.get(step)
            currDirection = directionTypes.get(strCurrDirection)
            continue

        # handle movement to next position
        nextPosX = currPos[0] + currDirection.get(posX)
        nextPosY = currPos[1] + currDirection.get(posY)
        currPos = [nextPosX, nextPosY]
        strCurrPos = '{}/{}'.format(nextPosX, nextPosY)

        # save multi occurences of positions
        if strCurrPos in strSteps:
            multiOccurence.add(strCurrPos)
        
        # add next position
        steps.append(currPos)
        strSteps.append(strCurrPos)

        #update highest and lowest bound
        if nextPosX > highestPos[posX]:
            highestPos[posX] = nextPosX
        elif nextPosX < lowestPos[posX]:
            lowestPos[posX] = nextPosX

        if nextPosY > highestPos[posY]:
            highestPos[posY] = nextPosY
        elif nextPosY < lowestPos[posY]:
            lowestPos[posY] = nextPosY

    return {
        'highestPosition': highestPos,
        'lowestPosition': lowestPos,
        'path': {
            'raw': steps,
            'string': strSteps,
        },
        'startPosition': {
            'raw': startPos,
            'string': strStartPos,
        },
        'endPosition': {
            'raw': currPos,
            'string': strCurrPos,
        },
        'multiOccurence': list(multiOccurence),
        'lastDirection': strCurrDirection,
        'bound': generateBound(highestPos, lowestPos)
    }
        

