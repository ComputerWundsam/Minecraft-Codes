
fenceblock = SPRUCE_FENCE
woodblock = PLANKS_SPRUCE
halfwood = SPRUCE_WOOD_SLAB
swidth = 14
iwidth = 5
floors = 4
startpos = pos(0, 0, 0)
j = 0
h = 0

def on_on_chat():
    global startpos, j, h
    startpos = player.position()
    loops.pause(1000)
    createtree()
    createstairs()
    createtreehouse( positions.add(startpos, pos(0, iwidth*floors*4, 0)))



def createstairs():
    global startpos, j, h
    for j in range(floors):
        h = 0
        setplatform(-1, -1)
        h += 1
        for k in range(2*iwidth-1):
            if k % 2 ==  1:
                setblock = woodblock
            else:
                setblock = halfwood
            blocks.fill(setblock, positions.add(startpos, pos(-(iwidth-1)+k, j*(4*iwidth)+h, -swidth)), positions.add(startpos, pos(-(iwidth-1)+k, j*(4*iwidth)+h, -iwidth)), FillOperation.REPLACE)
            blocks.fill(fenceblock, positions.add(startpos, pos(-(iwidth-1)+k, j*(4*iwidth)+h, -swidth-1)), positions.add(startpos, pos(-(iwidth-1)+k, j*(4*iwidth)+h+2, -swidth-1)), FillOperation.REPLACE)
            if k%2 == 1:
                h += 1
        setplatform(1, -1)
        h += 1
        for k in range(2*iwidth- 1):
            if k %2 == 1:
                setblock = woodblock
            else:
                setblock = halfwood
            blocks.fill(setblock, positions.add(startpos, pos(swidth, j*(4*iwidth)+h, -(iwidth-1)+k)), positions.add(startpos, pos(iwidth, j*(4*iwidth)+h, -(iwidth-1)+k)), FillOperation.REPLACE)
            blocks.fill(fenceblock, positions.add(startpos, pos(swidth+1, j*(4*iwidth)+h, -(iwidth-1)+k)), positions.add(startpos, pos(swidth+1, j*(4*iwidth)+h+2, -(iwidth-1)+k)), FillOperation.REPLACE)
            if k%2 == 1:
                h += 1
        setplatform(1, 1)
        h += 1
        for k in range(2*iwidth - 1):
            if k%2 == 1:
                setblock = woodblock
            else:
                setblock = halfwood
            blocks.fill(setblock, positions.add(startpos, pos(iwidth-1-k, j*(4*iwidth)+h, swidth)), positions.add(startpos, pos(iwidth-1-k, j*(4*iwidth)+h, iwidth)), FillOperation.REPLACE)
            blocks.fill(fenceblock, positions.add(startpos, pos(iwidth-1-k, j*(4*iwidth)+h, swidth+1)), positions.add(startpos, pos(iwidth-1-k, j*(4*iwidth)+h+2, swidth+1)), FillOperation.REPLACE)
            if k%2 == 1:
                h += 1
        setplatform(-1, 1)
        h += 1
        for k in range(2*iwidth - 1):
            if k%2 == 1:
                setblock = woodblock
            else:
                setblock = halfwood
            blocks.fill(setblock, positions.add(startpos, pos(-swidth, j*(4*iwidth)+h, iwidth-1-k)), positions.add(startpos, pos(-iwidth, j*(4*iwidth)+h, iwidth-1-k)), FillOperation.REPLACE)
            blocks.fill(fenceblock, positions.add(startpos, pos(-swidth-1, j*(4*iwidth)+h, iwidth-1-k)), positions.add(startpos, pos(-swidth-1, j*(4*iwidth)+h+2, iwidth-1-k)), FillOperation.REPLACE)
            if k%2 == 1:
                h += 1
    h = 0
    setplatform(-1, -1)



def setplatform(x, z):
    blocks.fill(fenceblock, positions.add(startpos, pos((swidth+1)*x, j*(4*iwidth)+h, (swidth+1)*z)), positions.add(startpos, pos(x*iwidth, j*(4*iwidth)+h+1, z*iwidth)), FillOperation.REPLACE)
    blocks.fill(woodblock, positions.add(startpos, pos(swidth*x, j*(4*iwidth)+h, swidth*z)), positions.add(startpos, pos(iwidth*x, j*(4*iwidth)+h, iwidth*z)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(swidth*x, j*(4*iwidth)+h+1, swidth*z)), positions.add(startpos, pos(iwidth*x, j*(4*iwidth)+h+1, iwidth*z)), FillOperation.REPLACE)

def createtreehouse(setpos):
    blocks.fill(woodblock, positions.add(setpos, pos(-iwidth, 0, -iwidth)), positions.add(setpos, pos(iwidth+swidth, 12, -iwidth-swidth)), FillOperation.HOLLOW)
    blocks.fill(GLASS, positions.add(setpos, pos(-iwidth+1, 12, -iwidth-1)), positions.add(setpos, pos(iwidth+swidth-1, 12, -iwidth-swidth+1)), FillOperation.HOLLOW)
    for i in range(4):
        blocks.replace(GLASS, woodblock, positions.add(setpos, pos(-iwidth, 10-4*i, -iwidth)), positions.add(setpos, pos(iwidth+swidth, 10-4*i, -iwidth-swidth)))
    blocks.fill(LOG_SPRUCE, positions.add(startpos, pos(iwidth+swidth, 0, -iwidth-swidth)), positions.add(setpos, pos(iwidth+swidth, 12, -iwidth-swidth)), FillOperation.REPLACE)
    blocks.fill(LOG_SPRUCE, positions.add(startpos, pos(-iwidth, 0, -iwidth-swidth)), positions.add(setpos, pos(-iwidth, 12, -iwidth-swidth)), FillOperation.REPLACE)
    blocks.fill(LOG_SPRUCE, positions.add(startpos, pos(iwidth+swidth, 0, -iwidth)), positions.add(setpos, pos(iwidth+swidth, 12, -iwidth)), FillOperation.REPLACE)

    blocks.place(SPRUCE_DOOR, positions.add(setpos, pos(-iwidth, 1, -iwidth-iwidth/2)))

def createtree():
    for i in range(iwidth*floors):
        blocks.fill(LOG_SPRUCE, positions.add(startpos, pos(-iwidth+1, 5*i, -iwidth+1)), positions.add(startpos,pos(iwidth-1, 5*i+7, iwidth-1)), FillOperation.REPLACE)
    for i in range(iwidth+2):
        blocks.fill(LEAVES_SPRUCE, positions.add(startpos, pos(-3*iwidth+i*2, (iwidth*floors*5)+6*i, -3*iwidth+i*2)), positions.add(startpos,pos(3*iwidth-i*2, iwidth*floors*5+6*i+6, 3*iwidth-i*2)), FillOperation.REPLACE)
        blocks.fill(LOG_SPRUCE, positions.add(startpos, pos(-3*iwidth+i*2+1, (iwidth*floors*5)+6*i+2, -3*iwidth+2*i+1)), positions.add(startpos,pos(3*iwidth-i*2-1, iwidth*floors*5+6*i+5, 3*iwidth-i*2-1)), FillOperation.REPLACE)

player.on_chat("run", on_on_chat)
