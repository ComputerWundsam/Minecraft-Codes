wallblock = STONE_BRICKS
roofblock = SANDSTONE

startpos = pos(0, 0, 0)
counter = 0


def on_on_chat():
    global startpos, counter
    startpos = player.position()
    loops.pause(5000)
    while True:
        placewall()
        setnextposition()
        counter += 1

def placewall():
    blocks.fill(wallblock, positions.add(startpos, pos(0, -40, 0)), positions.add(startpos, pos(0, 12, 6)))
    blocks.place(wallblock, positions.add(startpos, pos(0, 13, 0)))
    blocks.place(wallblock, positions.add(startpos, pos(0, 13, 6)))
    if(counter%2 == 0):
        blocks.place(wallblock, positions.add(startpos, pos(0, 14, 0)))
        blocks.place(wallblock, positions.add(startpos, pos(0, 14, 6)))
        if(counter%10 == 0):
            blocks.fill(AIR, positions.add(startpos, pos(0, 6, 0)), positions.add(startpos, pos(0, 9, 6)))
            if(counter%100 == 0):
                createtower()


def setnextposition():
    global startpos
    if(blocks.test_for_block(AIR, positions.add(startpos, pos(1, -1, 0)))):
        startpos = positions.add(startpos, pos(1, -1, 0))
    elif(blocks.test_for_block(AIR, positions.add(startpos, pos(1, 0, 0)))):
        startpos = positions.add(startpos, pos(1, 0, 0))
    else:
        startpos = positions.add(startpos, pos(1, 1, 0))
    if(counter%100 < 80 and counter%100 != 0):
        startpos = positions.add(startpos, pos(0, 0, randint(-20, 20)//18))

def createtower():
    global startpos
    blocks.fill(wallblock, positions.add(startpos, pos(0, 0, -4)), positions.add(startpos, pos(-14, 25, 10)))
    blocks.fill(AIR, positions.add(startpos, pos(-1, 25, -3)), positions.add(startpos, pos(-13, 25, 9)))
    blocks.fill(wallblock, positions.add(startpos, pos(-4, 25, 0)), positions.add(startpos, pos(-10, 28, 6)))
    for i in range(3):
        blocks.fill(wallblock, positions.add(startpos, pos(-5-i, 29+i, 0)), positions.add(startpos, pos(-9+i, 29+i, 6)))

    for i in range(5):
        blocks.fill(roofblock, positions.add(startpos, pos(-3-i, 28+i, -1)), positions.add(startpos, pos(-3-i, 28+i, 7)))
        blocks.fill(roofblock, positions.add(startpos, pos(-11+i, 28+i, -1)), positions.add(startpos, pos(-11+i, 28+i, 7)))


    blocks.fill(AIR, positions.add(startpos, pos(0, 13, 1)), positions.add(startpos, pos(-14, 16, 5)))
    blocks.fill(AIR, positions.add(startpos, pos(0, 17, 2)), positions.add(startpos, pos(-14, 17, 4)))
    for i in range(8):
        blocks.place(wallblock, positions.add(startpos, pos(-14+2*i, 26, 10)))
        blocks.place(wallblock, positions.add(startpos, pos(0-2*i, 26, -4)))
        blocks.place(wallblock, positions.add(startpos, pos(-14, 26, 10-2*i)))
        blocks.place(wallblock, positions.add(startpos, pos(0, 26, -4+2*i)))
    for i in range(3):
        blocks.fill(AIR, positions.add(startpos, pos(-2-5*i, 15, -4)), positions.add(startpos, pos(-2-5*i, 20, 10)))


player.on_chat("run", on_on_chat)
