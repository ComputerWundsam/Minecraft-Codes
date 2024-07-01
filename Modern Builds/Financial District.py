streetblock = BLACK_CONCRETE
whiteblock = WHITE_CONCRETE
glassblock = GLASS
houseblocks = BLUE_CONCRETE, GREEN_CONCRETE, BRICKS, STONE_BRICKS
streetwidth = 12
startpos = pos(0, 0, 0)
streetlength = 0

def on_on_chat():
    global startpos, streetlength
    startpos = positions.add(player.position(), pos(0, -1, 0))
    while True:
        counter = 0
        streetlength = randint(30, 20)
        while counter < streetlength:
            createstreet(startpos)
            startpos = positions.add(startpos, pos(1, 0, 0))
            counter += 1
        createhouse(startpos, streetlength)
        createhouse(positions.add(startpos, pos(0, 0, streetwidth+streetlength+1)), streetlength)

        createcrossroads()

def createstreet(setpos):
    blocks.fill(streetblock, setpos, positions.add(setpos, pos(0, 0, streetwidth)))
    blocks.place(whiteblock, positions.add(setpos, pos(0, 0, streetwidth/2)))

def createcrossroads():
    global startpos
    blocks.fill(whiteblock, startpos, positions.add(startpos, pos(-1, 0, streetwidth)))
    for i in range(streetwidth):
        blocks.fill(streetblock, positions.add(startpos, pos(0, 0, (i-streetwidth/2)*streetwidth+streetwidth)), positions.add(startpos, pos(streetwidth, 0, ((i-streetwidth/2)*streetwidth))))
    startpos = positions.add(startpos, pos(streetwidth, 0, 0))
    blocks.fill(whiteblock, startpos, positions.add(startpos, pos(-1, 0, streetwidth)))



def createhouse(setpos, houselength):
    setblock = houseblocks[randint(0, houseblocks.length-1)]
    househeight = randint(20, 50)
    for i in range(streetlength):
        blocks.fill(setblock, positions.add(setpos, pos(-1, 0, -1-i)), positions.add(setpos, pos(-houselength, househeight, -1-i)))
        if(i%2 == 1 and i < streetlength - 1):
            blocks.fill(glassblock, positions.add(setpos, pos(-1, 0, -1-i)), positions.add(setpos, pos(-houselength, househeight-2, -1-i)))
    for i in range(streetlength/2-1):
        blocks.fill(glassblock, positions.add(setpos, pos(-2-2*i, 0, -1)), positions.add(setpos, pos(-2-2*i, househeight-2, -streetlength)))



player.on_chat("run", on_on_chat)
