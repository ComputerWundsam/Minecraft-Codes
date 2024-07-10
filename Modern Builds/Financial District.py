streetblock = BLACK_CONCRETE
whiteblock = WHITE_CONCRETE
pavementblock = STONE_BRICKS_SLAB
glassblock = GLASS
houseblocks = [BLUE_CONCRETE, GREEN_CONCRETE, RED_CONCRETE, BROWN_CONCRETE, IRON_BLOCK, WHITE_CONCRETE, CONCRETE, BLACK_CONCRETE]
streetwidth = 16
startpos = pos(0, 0, 0)
streetlength = 0

def createdistrict():
    global startpos, streetlength
    startpos = positions.add(player.position(), pos(0, -1, 0))
    while True:
        counter = 0
        streetlength = randint(30, 20)
        while counter < streetlength:
            createstreet(startpos)
            if(counter == 0):
                blocks.fill(whiteblock, startpos, positions.add(startpos, pos(0, 0, streetwidth)))
            startpos = positions.add(startpos, pos(1, 0, 0))
            counter += 1
        createhouse(positions.add(startpos, pos(1, 0, 0)), streetlength)
        createhouse(positions.add(startpos, pos(1, 0, streetwidth+streetlength+1)), streetlength)
        createcrossroads()

def createstreet(setpos):
    blocks.fill(streetblock, setpos, positions.add(setpos, pos(0, 0, streetwidth)))
    blocks.place(whiteblock, positions.add(setpos, pos(0, 0, streetwidth/2)))
    blocks.place(pavementblock, positions.add(setpos, pos(0, 1, streetwidth)))
    blocks.place(pavementblock, positions.add(setpos, pos(0, 1, 0)))

def createcrossroads():
    global startpos
    blocks.fill(whiteblock, startpos, positions.add(startpos, pos(-1, 0, streetwidth)))
    for i in range(streetwidth):
        blocks.fill(streetblock, positions.add(startpos, pos(0, 0, (i-streetwidth/2)*streetwidth+streetwidth)), positions.add(startpos, pos(streetwidth, 0, ((i-streetwidth/2)*streetwidth))))
        if(i-streetwidth/2 != 0):
            if(i-streetwidth/2 == 1):
                blocks.fill(whiteblock, positions.add(startpos, pos(streetwidth, 0, streetwidth)), positions.add(startpos, pos(0, 0, streetwidth)))
            blocks.fill(whiteblock, positions.add(startpos, pos(streetwidth/2, 0, (i-streetwidth/2)*streetwidth+streetwidth)), positions.add(startpos, pos(streetwidth/2, 0, ((i-streetwidth/2)*streetwidth))))
            blocks.fill(pavementblock, positions.add(startpos, pos(streetwidth, 1, (i-streetwidth/2)*streetwidth+streetwidth)), positions.add(startpos, pos(streetwidth, 1, ((i-streetwidth/2)*streetwidth))))            
            blocks.fill(pavementblock, positions.add(startpos, pos(0, 1, (i-streetwidth/2)*streetwidth+streetwidth)), positions.add(startpos, pos(0, 1, ((i-streetwidth/2)*streetwidth))))
        else:
            blocks.fill(whiteblock, positions.add(startpos, pos(streetwidth, 0, 0)), startpos)        
    blocks.fill(pavementblock, positions.add(startpos, pos(0, 1, 0)), positions.add(startpos, pos(0, 1, -streetlength*2)))
    blocks.fill(pavementblock, positions.add(startpos, pos(0, 1, streetwidth)), positions.add(startpos, pos(0, 1, streetwidth+streetlength*2)))
    startpos = positions.add(startpos, pos(streetwidth, 0, 0))
    blocks.fill(pavementblock, positions.add(startpos, pos(0, 1, 0)), positions.add(startpos, pos(0, 1, -streetlength*2)))
    blocks.fill(pavementblock, positions.add(startpos, pos(0, 1, streetwidth)), positions.add(startpos, pos(0, 1, streetwidth+(streetlength*2))))



def createhouse(setpos, houselength):
    setblock = houseblocks[randint(0, houseblocks.length-1)]
    househeight = randint(20, 50)
    for i in range(streetlength):
        blocks.fill(setblock, positions.add(setpos, pos(-2, 0, -1-i)), positions.add(setpos, pos(-houselength, househeight, -1-i)))
        if(i%2 == 1 and i < streetlength - 1):
            blocks.replace(glassblock, setblock, positions.add(setpos, pos(-1, 2, -1-i)), positions.add(setpos, pos(-houselength, househeight-2, -1-i)))
    for i in range(streetlength/2-1):
        blocks.replace(glassblock, setblock, positions.add(setpos, pos(-1-2*i, 2, -1)), positions.add(setpos, pos(-1-2*i, househeight-2, -streetlength)))



player.on_chat("run", createdistrict)
