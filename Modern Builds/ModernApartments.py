wallblock = WHITE_CONCRETE
stairsleft = blocks.block_with_data(QUARTZ_STAIRS, 2)
stairsright = blocks.block_with_data(QUARTZ_STAIRS, 3)
villagerblocks = [BARREL, BLAST_FURNACE, BREWING_STAND, CARTOGRAPHY_TABLE, CAULDRON, COMPOSTER, FLETCHING_TABLE, LOOM, SMITHING_TABLE, SMOKER, STONECUTTER]

fsize = 12
fheight = 6
balconysize = 3
floors = 10
flatsperfloor = 4
lobbysize = 7

def on_on_chat():
    startpos = player.position()
    loops.pause(5000)
    flatten(startpos)
    for i in range(floors):
        createlobbyfloor(positions.add(startpos, pos(fsize, fheight*i, 0)))
        for j in range(flatsperfloor):
            createflat(positions.add(startpos, pos(0, fheight*i, j*fsize)))
    createlobbywalls(positions.add(startpos, pos(fsize, 0, 0)))


player.on_chat("run", on_on_chat)

def flatten(setpos):
    for i in range(fsize*flatsperfloor):
        blocks.fill(AIR, positions.add(setpos, pos(-3, 0, i)), positions.add(setpos, pos(2*fsize, fheight*flatsperfloor, i)), FillOperation.REPLACE)
        blocks.fill(GRASS, positions.add(setpos, pos(-3, -1, i)), positions.add(setpos, pos(2*fsize, -1, i)), FillOperation.REPLACE)

def createlobbywalls(setpos):
    blocks.fill(wallblock, positions.add(setpos, pos(0, 0, 0)),  positions.add(setpos, pos(lobbysize, fheight*floors, 0)), FillOperation.HOLLOW)
    blocks.fill(wallblock, positions.add(setpos, pos(0, 0, (flatsperfloor)*fsize)),  positions.add(setpos, pos(lobbysize, fheight*floors, (flatsperfloor)*fsize)), FillOperation.HOLLOW)
    blocks.replace(GLASS, AIR, positions.add(setpos, pos(lobbysize, 0, 0)),  positions.add(setpos, pos(lobbysize, fheight*floors, (flatsperfloor)*fsize)))
    blocks.fill(wallblock, positions.add(setpos, pos(0, fheight*floors, 0)), positions.add(setpos, pos(lobbysize, fheight*floors, flatsperfloor*fsize)), FillOperation.HOLLOW)
    createentrance(positions.add(setpos, pos(lobbysize, 0, fheight+5)))
    createentrance(positions.add(setpos, pos(lobbysize, 0, flatsperfloor*fsize-fheight-5)))

def createentrance(setpos):
    blocks.fill(wallblock, positions.add(setpos, pos(0, 0, -2)), positions.add(setpos, pos(1, fheight*floors, 1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(0, 1, -1)), positions.add(setpos, pos(1, 2, 0)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 1),positions.add(setpos, pos(2, 0, -2)), positions.add(setpos,pos(2, 0, 1)), FillOperation.REPLACE)
    agent.teleport( positions.add(setpos, pos(0, 1, 0)), EAST)
    agent.set_item(BIRCH_DOOR, 2, 1)
    agent.place(FORWARD)    
    blocks.place(blocks.block_with_data(BIRCH_DOOR, 0), positions.add(setpos, pos(1, 1, -1)))


def createlobbyfloor(setpos):
    blocks.fill(wallblock, setpos,  positions.add(setpos, pos(lobbysize, 0, (flatsperfloor)*fsize)), FillOperation.HOLLOW)
    for i in range(fheight):
        blocks.fill(AIR, positions.add(setpos, pos(lobbysize/2, -i, i+4)), positions.add(setpos, pos(lobbysize-1, -i+4, i+4)))
        blocks.fill(stairsright, positions.add(setpos, pos(lobbysize/2, -i, i+4)), positions.add(setpos, pos(lobbysize-1, -i, i+4)))
        blocks.fill(AIR, positions.add(setpos, pos(lobbysize/2, -i, flatsperfloor*fsize - i - 4)), positions.add(setpos, pos(lobbysize-1, -i+4, flatsperfloor*fsize - i - 4)))
        blocks.fill(stairsleft, positions.add(setpos, pos(lobbysize/2, -i, flatsperfloor*fsize - i - 4)), positions.add(setpos, pos(lobbysize-1, -i, flatsperfloor*fsize - i - 4)))

    for i in range(flatsperfloor):
        blocks.place(OCHRE_FROGLIGHT, positions.add(setpos, pos(lobbysize/2-1, fheight-1, fsize/2+fsize*i)))

def createflat(setpos):
    blocks.fill(wallblock, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(fsize, fheight, fsize)), FillOperation.HOLLOW)
    blocks.place(blocks.block_with_data(BIRCH_DOOR, 2), positions.add(setpos, pos(fsize, 1, 2)))
    createbalcony(setpos)
    addfurniture(setpos)

def createbalcony(setpos):
    blocks.fill(AIR , positions.add(setpos,pos(0, 2, 1)), positions.add(setpos,pos(0, fheight-1, fsize-1)), FillOperation.REPLACE)
    blocks.fill(GLASS_PANE, positions.add(setpos,pos(0, 1, 1)), positions.add(setpos,pos(0, 1, fsize-1)), FillOperation.REPLACE)
    blocks.fill(wallblock, positions.add(setpos,pos(balconysize, 1, 1)), positions.add(setpos,pos(balconysize, fheight-1, fsize)), FillOperation.REPLACE)
    blocks.fill(GLASS, positions.add(setpos,pos(balconysize, 2, 1)), positions.add(setpos,pos(balconysize, 2, fsize-1)), FillOperation.REPLACE)
    blocks.place(ACACIA_DOOR, positions.add(setpos,pos(balconysize, 1, 2)))

def addfurniture(setpos):
    blocks.place(OCHRE_FROGLIGHT, positions.add(setpos, pos((fsize+balconysize)/2, fheight-1, fsize/2)))
    blocks.place(BED, positions.add(setpos, pos(fsize-1, 1, fsize-1)))
    blocks.place(BED, positions.add(setpos, pos(fsize-2, 1, fsize-1)))
    blocks.place(ACACIA_FENCE, positions.add(setpos, pos(fsize/2, 1, fsize/2)))
    blocks.place(ACACIA_PRESSURE_PLATE, positions.add(setpos, pos(fsize/2, 2, fsize/2)))
    blocks.place(blocks.block_with_data(ACACIA_WOOD_STAIRS, 3), positions.add(setpos, pos(fsize/2, 1, fsize/2-1)))
    blocks.place(blocks.block_with_data(ACACIA_WOOD_STAIRS, 2), positions.add(setpos, pos(fsize/2, 1, fsize/2+1)))
    blocks.fill(BLACK_CONCRETE, positions.add(setpos, pos(fsize-1, 1, fsize/2-1)), positions.add(setpos, pos(fsize-1, 2, fsize/2+2)))
    blocks.fill(blocks.block_with_data(ACACIA_DOOR, 2), positions.add(setpos, pos(fsize-2, 1, fsize/2-1)), positions.add(setpos, pos(fsize-2, 1, fsize/2+2)))
    blocks.fill(BOOKSHELF, positions.add(setpos, pos(fsize-3, 1, fsize-1)), positions.add(setpos, pos(fsize/2, 4, fsize-1))) 
    blocks.place(villagerblocks[randint(0, villagerblocks.length-1)], positions.add(setpos, pos(fsize/2-1, 1, fsize-1)))
    mobs.spawn(VILLAGER, positions.add(setpos, pos(fsize/2-2, 1, fsize/2)))
    mobs.spawn(VILLAGER, positions.add(setpos, pos(fsize/2+2, 1, fsize/2)))
