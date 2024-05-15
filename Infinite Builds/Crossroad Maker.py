streetblock = BLACK_CONCRETE

def on_on_chat():
    startpos = positions.add(player.position().to_world(), pos(0, -1, 0))
    counter = 0
    while True:
        randno = randint (0, 15)
        if ((randno + counter) > 30):
            createstreetlight(positions.add(startpos, pos(0, 0, -counter/2)))
            createstreetlight(positions.add(startpos, pos(4, 0, -counter/2)))
            makecrossing(startpos)
            startpos = positions.add(startpos, pos(0, 0, 5))
            counter = 0
        blocks.fill(AIR, startpos, positions.add(startpos, pos(4, 10, 0)))
        blocks.fill(streetblock, startpos, positions.add(startpos, pos(4, 0, 0)))
        blocks.place(STONE_BRICKS_SLAB, positions.add(startpos, pos(0, 1, 0)))
        blocks.place(STONE_BRICKS_SLAB, positions.add(startpos, pos(4, 1, 0)))
        startpos = positions.add(startpos, pos(0, 0, 1))
        counter += 1

def createstreetlight(setpos):
    blocks.fill(BLACKSTONE_WALL, setpos, positions.add(setpos, pos(0, 4, 0)))
    blocks.place(OCHRE_FROGLIGHT, positions.add(setpos, pos(0, 5, 0)))

def makecrossing(setposition):
    streetlength = randint(30, 40)
    blocks.fill(AIR, setposition, positions.add(setposition, pos(-streetlength, 10, 4)))
    blocks.fill(AIR, setposition, positions.add(setposition, pos(streetlength, 10, 4)))
    blocks.fill(streetblock, positions.add(setposition, pos(4, 0, 0)), positions.add(setposition, pos(-streetlength, 0, 4)))
    blocks.fill(streetblock, positions.add(setposition, pos(4, 0, 0)), positions.add(setposition, pos(streetlength+4, 0, 4)))
    blocks.fill(STONE_BRICKS_SLAB, positions.add(setposition, pos(0, 1, 0)), positions.add(setposition, pos(-streetlength, 1, 0)))
    blocks.fill(STONE_BRICKS_SLAB, positions.add(setposition, pos(0, 1, 4)), positions.add(setposition, pos(-streetlength, 1, 4)))
    blocks.fill(STONE_BRICKS_SLAB, positions.add(setposition, pos(4, 1, 0)), positions.add(setposition, pos(streetlength+4, 1, 0)))
    blocks.fill(STONE_BRICKS_SLAB, positions.add(setposition, pos(4, 1, 4)), positions.add(setposition, pos(streetlength+4, 1, 4)))
    for i in range(4):
        createstreetlight(positions.add(setposition, pos(4*(i//2), 0, 4*(i%2))))
    for i in range(2):
        createstreetlight(positions.add(setposition, pos(-streetlength, 0, 4*i)))
        createstreetlight(positions.add(setposition, pos(streetlength+4, 0, 4*i)))
        createstreetlight(positions.add(setposition, pos(-streetlength/2, 0, 4*i)))
        createstreetlight(positions.add(setposition, pos(streetlength/2+2, 0, 4*i)))
player.on_chat("run", on_on_chat)

def deletewalk():
    blocks.replace(AIR, STONE_BRICKS_SLAB, pos(-10, -1, -10), pos(10, 4, 10))
    blocks.replace(AIR, BLACK_CONCRETE, pos(-10, -1, -10), pos(10, 8, 10))
    blocks.replace(AIR, OCHRE_FROGLIGHT, pos(-10, -1, -10), pos(10, 8, 10))
    blocks.replace(AIR, BLACKSTONE_WALL, pos(-10, -1, -10), pos(10, 8, 10))
        
