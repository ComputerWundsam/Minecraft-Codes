height = 3
layers = 8
startpos = pos(0, 0, 0)
entrancepos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createrings()
    createpivotpoint()
    blocks.place(LAVA, positions.add(startpos, pos(0, -height+1, 0)))
    waitforpivotpoint()
    blocks.place(WATER, positions.add(startpos, pos(0, -height+3, 0)))
    waitforpivotpoint()
    blocks.place(AIR, positions.add(startpos, pos(0, -height+3, 0)))
    createentrance()
    createfloor()


def createrings():
    for i in range(layers):
        for j in range(i):
            blocks.fill(GLOWSTONE, positions.add(startpos, pos(i-j-1, -i*height, j)), positions.add(startpos, pos(-i+j+1, -i*height, -j)))
        for j in range(i-1):
            blocks.fill(AIR, positions.add(startpos, pos(i-2-j, -i*height, j)), positions.add(startpos, pos(-i+2+j, -i*height, -j)))

def createpivotpoint():
    global entrancepos
    entrancepos = positions.add(startpos, pos(-layers+1, 0, 0))
    while blocks.test_for_block(AIR, entrancepos):
        entrancepos = positions.add(entrancepos, pos(0, -1 ,0))
    entrancepos = positions.add(entrancepos, pos(0, 1 ,0))
    player.say(entrancepos)

def waitforpivotpoint():
    global entrancepos
    loops.pause(500*height*layers)
    while blocks.test_for_block(AIR, entrancepos):
        loops.pause(500)

def createentrance():
    blocks.fill(COBBLESTONE, positions.add(entrancepos, pos(0, -1, -1)), positions.add(entrancepos, pos(0, 3, 1)))
    blocks.place(OAK_DOOR, positions.add(entrancepos, pos(0, 1, 0)))

def createfloor():
    for i in range(layers):
        player.execute("fill " + positions.add(entrancepos, pos(0+i, 1, i)) + " " + positions.add(entrancepos, pos(2*layers-i, height*layers, -i)) + " air replace lava")
        blocks.fill(DIAMOND_BLOCK, positions.add(entrancepos, pos(0+i, 0, i)), positions.add(entrancepos, pos(2*layers-i, 0, -i)))

player.on_chat("run", on_on_chat)
