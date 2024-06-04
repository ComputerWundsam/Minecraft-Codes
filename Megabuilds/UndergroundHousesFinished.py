wallblocks = WHITE_CONCRETE
cubesize = 10
houseblocks = 3
villagerblock = [BELL, BARREL, BLAST_FURNACE, BREWING_STAND, CARTOGRAPHY_TABLE, CAULDRON, COMPOSTER, FLETCHING_TABLE, STONECUTTER_BLOCK, LOOM, SMITHING_TABLE, SMOKER]

def on_on_chat(size, hblocks):
    global cubesize, houseblocks
    cubesize = size
    houseblocks = hblocks
    startpos = positions.add(player.position(), pos(0, -1, 0))
    loops.pause(5000)
    flattenground(startpos)
    for i in range(houseblocks):
        for j in range(houseblocks):
            createhouse(positions.add(startpos, pos(cubesize*j, -1, cubesize*i)))
    for i in range(houseblocks):
        for j in range(houseblocks-1):
            createhorizontaltunnel(positions.add(startpos, pos(i*cubesize, 0, j*cubesize)))
            createverticaltunnel(positions.add(startpos, pos(j*cubesize, 0, i*cubesize)))
    createentrance(positions.add(startpos, pos(3, -7, 0)))

def createentrance(setpos):
    blocks.fill(AIR, setpos, positions.add(setpos, pos(3, 5, 0)))
    blocks.fill(AIR, positions.add(setpos, pos(0, 0, -1)), positions.add(setpos, pos(4, 9, -6)))
    blocks.fill(wallblocks, positions.add(setpos, pos(0, 6, -1)), positions.add(setpos, pos(4, 9, -1)))
    blocks.fill(wallblocks, positions.add(setpos, pos(4, 0, 0)), positions.add(setpos, pos(4, 9, -6)))
    blocks.fill(wallblocks, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(0, 9, -6)))
    blocks.fill(wallblocks, positions.add(setpos, pos(0, 9, -1)), positions.add(setpos, pos(4, 9, -6)))
    blocks.fill(wallblocks, positions.add(setpos, pos(0, 6, -6)), positions.add(setpos, pos(4, 9, -6)))
    blocks.place(ACACIA_DOOR, positions.add(setpos, pos(2, 7, -6)))
    for i in range(7):
        blocks.fill(wallblocks, positions.add(setpos, pos(1, i, -i)), positions.add(setpos, pos(3, i, -i)))


def flattenground(setpos):
    for i in range(houseblocks):
        for j in range(houseblocks): 
            blocks.fill(AIR, positions.add(setpos, pos(cubesize*j, 0, cubesize*i)), positions.add(setpos, pos(cubesize*(j+1), 10, cubesize*(i+1))))

def createhorizontaltunnel(setpos):
    blocks.fill(wallblocks, positions.add(setpos, pos((cubesize/2)-2, -3, cubesize-2)), positions.add(setpos, pos((cubesize/2), -7, cubesize)))
    blocks.fill(AIR, positions.add(setpos, pos((cubesize/2)-1, -4, cubesize-2)), positions.add(setpos, pos((cubesize/2)-1, -6, cubesize)))
    blocks.place(ACACIA_DOOR, positions.add(setpos, pos((cubesize/2)-1, -6, cubesize-1)))

def createverticaltunnel(setpos):
    blocks.fill(wallblocks, positions.add(setpos, pos(cubesize-2, -3, (cubesize/2)-2)), positions.add(setpos, pos(cubesize, -7, (cubesize/2))))
    blocks.fill(AIR, positions.add(setpos, pos(cubesize-2, -4, (cubesize/2)-1)), positions.add(setpos, pos(cubesize, -6, (cubesize/2)-1)))
    blocks.place(ACACIA_DOOR, positions.add(setpos, pos(cubesize-1, -6, (cubesize/2)-1)))

def createhouse(setpos):
    blocks.fill(wallblocks, setpos, positions.add(setpos, pos(cubesize-2, -6, cubesize-2)), FillOperation.HOLLOW)
    player.execute("fill " + positions.add(setpos, pos(1, 0, 1)) + " " + positions.add(setpos, pos(cubesize-3, 0, cubesize-3)) + " barrier")

    #blocks.fill(GLASS, positions.add(setpos, pos(1, 0, 1)), positions.add(setpos, pos(cubesize-3, 0, cubesize-3)))
    furnish(positions.add(setpos, pos(cubesize-3, -5, cubesize -3)))

def furnish(setpos):
    for i in range(2):
        blocks.place(BED, positions.add(setpos, pos(i-1, 0, -1)))
        blocks.place(villagerblock[(randint(0, villagerblock.length))%villagerblock.length], positions.add(setpos, pos(-cubesize+4+i, 0, 0)))
        blocks.place(villagerblock[(randint(0, villagerblock.length))%villagerblock.length], positions.add(setpos, pos(0, 0, -cubesize+4+i)))
        blocks.place(CHEST, positions.add(setpos, pos(-cubesize+4+i, 0, -cubesize+4)))
        mobs.spawn(VILLAGER, positions.add(setpos, pos(-cubesize+7, 0, -cubesize+7)))
    blocks.fill(BOOKSHELF, setpos, positions.add(setpos, pos(-2, 4, 0)))
    blocks.place(TORCH, positions.add(setpos, pos(-cubesize+4, 0, -cubesize+4)))



player.on_chat("run", on_on_chat)

def on_travelled_walk():
    blocks.fill(AIR, pos(-10, 0, -10), pos(10, 20, 10))
#player.on_travelled(FLY, on_travelled_walk)

