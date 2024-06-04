wallblocks = PLANKS_ACACIA
cubesize = 10
houseblocks = 3

def on_on_chat(size, hblocks):
    global cubesize, houseblocks
    cubesize = size
    houseblocks = hblocks
    startpos = positions.add(player.position(), pos(0, -1, 0))
    for i in range(houseblocks):
        for j in range(houseblocks):
            createhouse(positions.add(startpos, pos(cubesize*j, -1, cubesize*i)))
    for i in range(houseblocks):
        for j in range(houseblocks-1):
            createhorizontaltunnel(positions.add(startpos, pos(i*cubesize, 0, j*cubesize)))
            createverticaltunnel(positions.add(startpos, pos(j*cubesize, 0, i*cubesize)))


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
    blocks.fill(GLASS, positions.add(setpos, pos(1, 0, 1)), positions.add(setpos, pos(cubesize-3, 0, cubesize-3)))
    furnish(positions.add(setpos, pos(cubesize-3, -5, cubesize -3)))

def furnish(setpos):
    blocks.place(BED, setpos)

player.on_chat("run", on_on_chat)
