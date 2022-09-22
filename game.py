import random, time

def deadState(width, height):
    return [[0 for _ in range(height)] for _ in range(width)]

def stateWidth(state):
    return len(state)

def stateHeight(state):
    return len(state[0])

def randomState(width, height):
    state = deadState(width, height)
    for i in range(stateWidth(state)):
        for j in range(stateHeight(state)):
            randomInt = random.random()
            if randomInt > 0.5:
                state[i][j] = 1
            else:
                state[i][j] = 0
    return state

def render(state):
    
    displayAs = {
        0 : ' ',
        1 : u"\u2588"
    }
    lines = []
    for y in range(0, stateHeight(state)):
        line = ''
        for x in range(0, stateWidth(state)):
            line += displayAs[state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))

def nextBoardState(board):
    width = stateWidth(board)
    height = stateHeight(board)
    nextState = deadState(width, height)
    for i in range(width):
        for j in range(height):
            nextState[i][j] = nextCellValue((i, j), board)
    return nextState
            

def nextCellValue(cell_coords, state):
    width = stateWidth(state)
    height = stateHeight(state)

    x = cell_coords[0]
    y = cell_coords[1]
    live = 0

    for a in range(x - 1, (x + 1) + 1):
        if a < 0 or a >= width:
            continue
        for b in range(y - 1, (y + 1) + 1):
            if b < 0 or b >= height:
                continue
            if a == x and b == y:
                continue
            if state[a][b] == 1:
                live += 1
    if state[x][y] == 1:
        if live <= 1:
            return 0
        elif live  <= 3:
            return 1
        else:
            return 0
    else:
        if live == 3:
            return 1
        else: 
            return 0

def runForever(init_state):
    
    next_state = init_state
    while True:
        render(next_state)
        next_state = nextBoardState(next_state)
        time.sleep(0.01)
                




init_state = randomState(500, 30)
runForever(init_state)
