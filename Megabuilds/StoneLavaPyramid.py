height = 8
layers = 10
startpos = pos(0, 0, 0)
entrancepos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createpivotpoint()
    createrings()
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
            player.execute("fill " + positions.add(startpos, pos(i-2-j, -i*height, j)) + " " + positions.add(startpos, pos(-i+2+j, -i*height+1, -j)) + " barrier")

def createpivotpoint():
    global entrancepos
    entrancepos = positions.add(startpos, pos(-layers+1, 0, 0))
    while blocks.test_for_block(AIR, entrancepos):
        entrancepos = positions.add(entrancepos, pos(0, -1 ,0))
    entrancepos = positions.add(entrancepos, pos(0, 1 ,0))
    player.say(entrancepos)

def waitforpivotpoint():
    global entrancepos
    while blocks.test_for_block(AIR, entrancepos):
        loops.pause(500)
    entrancepos = positions.add(entrancepos, pos(-1, 1, 0))

def createentrance():
    blocks.fill(COBBLESTONE, positions.add(entrancepos, pos(2, -3, -1)), positions.add(entrancepos, pos(2, 1, 1)))
    blocks.place(OAK_DOOR, positions.add(entrancepos, pos(2, -1, 0)))

def createfloor():
    for i in range(layers):
        blocks.fill(DIAMOND_BLOCK, positions.add(entrancepos, pos(i+2, -2, i)), positions.add(entrancepos, pos(2*layers-i, -2, -i)))


player.on_chat("run", on_on_chat)

def on_chat():
    global entrancepos 
    entrancepos = player.position()
    createfloor()
player.on_chat("jump", on_chat)

# def on_travelled_walk():
#     blocks.fill(AIR, pos(-15, 0, -15), pos(15, 10, 15))
# player.on_travelled(FLY, on_travelled_walk)
