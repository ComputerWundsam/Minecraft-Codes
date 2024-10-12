leglength = 18
startpos = pos(0, 0, 0)
stationsize = 40
platesizeincrease = 1
platecut = 6
stationpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    loops.pause(5000)
    createmirrors()
    createstation(positions.add(startpos, pos(0, -26, 2)))
    

player.on_chat("run", on_on_chat)

def creategoldplates(setpos):
    for i in range(4):
        blocks.fill(OCHRE_FROGLIGHT, positions.add(setpos, pos(4-i, -i, 0)), positions.add(setpos, pos(-3+i, i, 0)), FillOperation.REPLACE)
        blocks.fill(BLACK_CONCRETE, positions.add(setpos, pos(5-i, -i-1, -1)), positions.add(setpos, pos(-4+i, i+1, -1)), FillOperation.REPLACE)

def createmirrors():
    for i in range(3):
        creategoldplates(positions.add(startpos, pos(-14, 10-9*i, 0)))
        creategoldplates(positions.add(startpos, pos(14, 10-9*i, 0)))
    for i in range(4):
        creategoldplates(positions.add(startpos, pos(-7, 14-9*i, 0)))
        creategoldplates(positions.add(startpos, pos(7, 14-9*i, 0)))
    for i in range(2):
        creategoldplates(positions.add(startpos, pos(0, -18+9*i, 0)))
        creategoldplates(positions.add(startpos, pos(0, 18-9*i, 0)))
    createtelescopecenter()
    createlegs()

def createtelescopecenter():
    blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(-3, -3, 0)), positions.add(startpos, pos(4, 3, 4)), FillOperation.REPLACE)
    blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(-4, -2, 0)), positions.add(startpos, pos(5, 2, 3)), FillOperation.REPLACE)
    blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(-2, -4, 0)), positions.add(startpos, pos(3, 4, 3)), FillOperation.REPLACE)
    blocks.fill(REDSTONE_LAMP, positions.add(startpos, pos(-1, -1, 4)), positions.add(startpos, pos(1, 1, 3)), FillOperation.REPLACE)
    blocks.fill(REDSTONE_BLOCK, positions.add(startpos, pos(-1, -1, 3)), positions.add(startpos, pos(1, 1, 3)), FillOperation.REPLACE)

def createlegs():
    for i in range(leglength):
        blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(0, 21-i, 2*i)), positions.add(startpos, pos(0, 21-i, 2+2*i)), FillOperation.REPLACE)
        blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(7-(5*(i/leglength)), -17+i, 2*i)), positions.add(startpos, pos(7-(5*(i/leglength)), -18+i, 2+2*i)), FillOperation.REPLACE)
        blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(-7+(5*(i/leglength)), -17+i, 2*i)), positions.add(startpos, pos(-7+(5*(i/leglength)), -18+i, 2+2*i)), FillOperation.REPLACE)
    blocks.fill(BLACK_CONCRETE, positions.add(startpos, pos(2, -1, leglength*2+1)), positions.add(startpos, pos(-2, 3, leglength*2)), FillOperation.REPLACE)
    blocks.fill(OCHRE_FROGLIGHT, positions.add(startpos, pos(1, 0, leglength*2)), positions.add(startpos, pos(-1, 2, leglength*2)), FillOperation.REPLACE)

def createstation(setpos):
    global stationpos
    stationpos = setpos
    createstairs(stationpos)
    for j in range(4):
        for i in range(stationsize+j - platecut):
            blocks.fill(WHITE_CONCRETE, positions.add(stationpos, pos(stationsize-i+platesizeincrease*j, -3*j, i)), positions.add(stationpos, pos(-stationsize+i-platesizeincrease*j, -3*j, -i)), FillOperation.REPLACE)
    for i in range(6):
        blocks.replace(VERDANT_FROGLIGHT, WHITE_CONCRETE, positions.add(stationpos, pos(-stationsize-platesizeincrease, 0, i*6)), positions.add(stationpos, pos(stationsize+platesizeincrease, -12, i*6)))
        for j in range(2):
            blocks.replace(VERDANT_FROGLIGHT, WHITE_CONCRETE, positions.add(stationpos, pos(-stationsize-platesizeincrease, 0, -i*6-j*3)), positions.add(stationpos, pos(stationsize+platesizeincrease, -12, -i*6-j*3)))
    createfeet(positions.add(stationpos, pos(stationsize-1, 0, 0)), 0, 1)
    createfeet(positions.add(stationpos, pos(-(stationsize)+1, 0, 0)), 0, -1)

    createfeet(positions.add(stationpos, pos(-platecut, 0, -(stationsize-platecut)+2)), -1, 0)
    createfeet(positions.add(stationpos, pos(platecut, 0, -(stationsize-platecut)+2)), -1, 0)
    createfeet(positions.add(stationpos, pos(-platecut, 0, (stationsize-platecut)-2)), 1, 0)
    createfeet(positions.add(stationpos, pos(platecut, 0, (stationsize-platecut)-2)), 1, 0)

def createstairs(stationpos):
    for i in range(4):
        blocks.fill(WHITE_CONCRETE, positions.add(stationpos, pos(-12, i, -i)), positions.add(stationpos, pos(12, i, -i)), FillOperation.REPLACE)

def createfeet(setpos, front, left):
    blocks.fill(BLACK_CONCRETE, positions.add(setpos, pos(1, 1, 1)), positions.add(setpos, pos(-1, -1, -1)), FillOperation.REPLACE)
    for i in range(4):
        blocks.fill(BLACK_CONCRETE, positions.add(setpos, pos((2+i)*left-1, -1-3*i, (2+i)*front-1)), positions.add(setpos, pos((2+i)*left+1, -4-3*i, (2+i)*front+1)), FillOperation.REPLACE)
