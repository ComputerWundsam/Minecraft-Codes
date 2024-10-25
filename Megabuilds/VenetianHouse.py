walllength = 8
wallwidth = 5
househeight = 20
windowcount = 4

startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    loops.pause(5000)
    firstfloor()
    mainhouse(positions.add(startpos, pos(0, 6, 0)))

#    blocks.fill(BLACK_WOOL, positions.add(startpos, pos(walllength*5-2, 0, wallwidth*5-2)), positions.add(startpos,pos(1, 5, 1)), FillOperation.REPLACE)

def mainhouse(setpos):
    for i in range(househeight):
        blocks.fill(BRICKS, positions.add(setpos, pos(walllength*5-2, i, wallwidth*5-2)), positions.add(setpos,pos(1, i, 1)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(walllength*5-3+(i%2), i, wallwidth*5-2)), positions.add(setpos,pos(walllength*5-2, i, 1)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(1+(i%2), i, wallwidth*5-2)), positions.add(setpos,pos(1, i, 1)), FillOperation.REPLACE)
    createroof(positions.add(setpos, pos(0, househeight, 0)))
    createbalcony(positions.add(setpos, pos(3, 2, 0)))
    for i in range(windowcount):
        createbalconywindow(positions.add(setpos, pos(3*i+4, 2, 0)))
        createbalconywindow(positions.add(setpos, pos(3*i+4, househeight/2, 0)))
        createfloralwindow(positions.add(setpos, pos(walllength*3 + (6 * (i//2)), (househeight/4)*(2*(i%2))+2, 0)))

def createroof(setpos):
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos,pos(walllength*5-1, 0, wallwidth*5-1)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 4), positions.add(setpos, pos(-1, 0, -1)), positions.add(setpos,pos(-1, 0, wallwidth*5)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 6), positions.add(setpos, pos(-1, 0, -1)), positions.add(setpos,pos(walllength*5, 0, -1)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 7), positions.add(setpos, pos(-1, 0, wallwidth*5)), positions.add(setpos,pos(walllength*5, 0, wallwidth*5)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 5), positions.add(setpos, pos(walllength*5, 0, -1)), positions.add(setpos,pos(walllength*5, 0, wallwidth*5)), FillOperation.REPLACE)
    for i in range(3):
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(1+i, 1+i, 1+i)), positions.add(setpos,pos(walllength*5-2-i, 1+i, wallwidth*5-2-i)), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 0), positions.add(setpos, pos(0+i, 1+i, 0+i)), positions.add(setpos,pos(0+i, 1+i, wallwidth*5)), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 2), positions.add(setpos, pos(0+i, 1+i, 0+i)), positions.add(setpos,pos(walllength*5-1-i, 1+i, 0+i)), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 3), positions.add(setpos, pos(0+i, 1+i, wallwidth*5-1-i)), positions.add(setpos,pos(walllength*5-1-i, 1+i, wallwidth*5-1-i)), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 1), positions.add(setpos, pos(walllength*5-1-i, 1+i, 0+i)), positions.add(setpos,pos(walllength*5-1-i, 1+i, wallwidth*5-1-i)), FillOperation.REPLACE)

def createfloralwindow(setpos):
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(3, 3, 0)), FillOperation.REPLACE)
    blocks.fill(BLACK_WOOL, positions.add(setpos, pos(0, 0, 1)), positions.add(setpos, pos(3, 3, 1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(1, 1, 0)), positions.add(setpos, pos(2, 2, 0)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 4), positions.add(setpos, pos(2, 2, 0)))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 5), positions.add(setpos, pos(1, 2, 0)))


def createbalconywindow(setpos):
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(3, househeight/3+1, 0)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(1, 1, 0)), positions.add(setpos, pos(2, househeight/3-1, 0)), FillOperation.REPLACE)
    for i in range(househeight/10):
        blocks.fill(QUARTZ_SLAB, positions.add(setpos, pos(1, 2*i+3, 0)), positions.add(setpos, pos(2, 2*i+3, 0)), FillOperation.REPLACE)
    blocks.fill(BLACK_WOOL, positions.add(setpos, pos(1, 1, 1)), positions.add(setpos, pos(2, househeight/3, 1)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 4), positions.add(setpos, pos(2, househeight/3, 0)))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 5), positions.add(setpos, pos(1, househeight/3, 0)))

def createbalcony(setpos):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(4*windowcount, 0, 0)), positions.add(setpos, pos(0, 0, -4)), FillOperation.REPLACE)
    blocks.fill(WHITE_STAINED_GLASS_PANE, positions.add(setpos, pos(4*windowcount, 1, 0)), positions.add(setpos, pos(0, 1, -4)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(4*windowcount-1, 1, 0)), positions.add(setpos, pos(1, 1, -3)), FillOperation.REPLACE)


def firstfloor():
    for i in range(walllength):
        wallpartx(positions.add(startpos, pos(5*i, 0, 0)))
        wallpartx(positions.add(startpos, pos(5*i, 0, wallwidth*5-1)))
    for i in range(wallwidth):
        wallparty(positions.add(startpos, pos(0, 0, 5*i)))
        wallparty(positions.add(startpos, pos(walllength*5-1, 0, 5*i)))

player.on_chat("run", on_on_chat)

def wallpartx(setpos):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(4, 5, 0)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(1, 0, 0)), positions.add(setpos, pos(3, 4, 0)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 4), positions.add(setpos, pos(3, 4, 0)))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 5), positions.add(setpos, pos(1, 4, 0)))
    blocks.replace(blocks.block_with_data(QUARTZ_STAIRS, 7), AIR, positions.add(setpos, pos(0, 5, 1)), positions.add(setpos, pos(4, 5, 1)))
    blocks.replace(blocks.block_with_data(QUARTZ_STAIRS, 6), AIR, positions.add(setpos, pos(0, 5, -1)), positions.add(setpos, pos(4, 5, -1)))

def wallparty(setpos):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(0, 5, 4)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(0, 0, 1)), positions.add(setpos, pos(0, 4, 3)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 6), positions.add(setpos, pos(0, 4, 3)))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 7), positions.add(setpos, pos(0, 4, 1)))
    blocks.replace(blocks.block_with_data(QUARTZ_STAIRS, 5), AIR, positions.add(setpos, pos(1, 5, 0)), positions.add(setpos, pos(1, 5, 4)))
    blocks.replace(blocks.block_with_data(QUARTZ_STAIRS, 4), AIR, positions.add(setpos, pos(-1, 5, 0)), positions.add(setpos, pos(-1, 5, 4)))
