trainblock = BLOCK_OF_NETHERITE
wagonblock = RED_CONCRETE
roofblock = PLANKS_OAK
railblock = IRON_BLOCK

startpos = pos(0, 0, 0)
trainlength = 20
trainsize = 6

def on_on_chat():
    global startpos
    startpos = player.position()
    flatten(positions.add(startpos, pos(0, -trainsize-3, 0)))
    createrails(positions.add(startpos, pos(0, -trainsize-3, 0)))
    createcenterpiece()
    createcabin(positions.add(startpos, pos(trainlength, -trainsize+1, -trainsize)))
    createchimney(positions.add(startpos, pos(trainlength/3, 4, 0)))
    for i in range(3):
        createwheel(positions.add(startpos, pos(2+i*9, -trainsize+1, 0)), 3)
    createwheel(positions.add(startpos, pos(30, -trainsize+3, 0)), 5)

    for i in range(4):
        createwagon(positions.add(startpos, pos(40+40*i, -4, 0)))

def flatten(setpos):
    for j in range(20):
        for i in range(4):
            blocks.fill(AIR, positions.add(setpos, pos(-100 + (20*j), 8*i, -(trainsize+8))), positions.add(setpos, pos(-80 + (20*j), 8*i+8, (trainsize+8))))



def createrails(setpos):
    for i in range(20):
        blocks.fill(OBSIDIAN, positions.add(setpos, pos(-100 + 20*i, -1, -(trainsize+8))), positions.add(setpos, pos(-80 + 20*i, -1, (trainsize+8))))
        blocks.fill(railblock, positions.add(setpos, pos(-100 + 20*i, 0, trainsize+4)), positions.add(setpos, pos(-80 + 20*i, 1, trainsize+3)))
        blocks.fill(railblock, positions.add(setpos, pos(-100 + 20*i, 0, -(trainsize+4))), positions.add(setpos, pos(-80 + 20*i, 1, -(trainsize+3))))
        blocks.fill(roofblock, positions.add(setpos, pos(-88 + 20*i, -1, -(trainsize+8))), positions.add(setpos, pos(-92 + 20*i, -1, (trainsize+8))))


def createcenterpiece():
    for i in range(3):
        shapes.circle(trainblock, positions.add(startpos, pos(-1-i, 0, 0)), trainsize-1-i, Axis.X, ShapeOperation.REPLACE)
    for i in range(3):
        for j in range(3-i):
            blocks.fill(trainblock, positions.add(startpos, pos(-4-j, i-trainsize, trainsize-i-j)), positions.add(startpos,pos(-4-j, i-trainsize, -(trainsize-i-j))), FillOperation.REPLACE)
        blocks.replace(trainblock, AIR, positions.add(startpos,pos(-5+i, i-trainsize, -trainsize+2+i)), positions.add(startpos,pos(6+i, i-trainsize, trainsize-2-i)))
    blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, pos(-3, 0, 0)))
    for i in range(trainlength):
        shapes.circle(trainblock, positions.add(startpos, pos(i, 0, 0)), trainsize, Axis.X, ShapeOperation.REPLACE)
    blocks.replace(DARK_OAK_FENCE, AIR, positions.add(startpos, pos(3, 2, 3)), positions.add(startpos, pos(3, 8, 3)))
    blocks.place(BELL, positions.add(startpos, pos(3, 9, 3)))

def createchimney(setpos):
    for j in range(2):
        for i in range(4-j):
            shapes.circle(trainblock, positions.add(setpos, pos(0, j*4+i, 0)), 3-j, Axis.Y, ShapeOperation.REPLACE)

def createcabin(setpos):
    blocks.fill(trainblock, positions.add(setpos, pos(0, 7, 0)), positions.add(setpos, pos(14, 14, trainsize*2)), FillOperation.HOLLOW)
    blocks.fill(trainblock, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(14, 7, trainsize*2-2)))
    blocks.fill(trainblock, positions.add(setpos, pos(10, 2, trainsize)), positions.add(setpos, pos(18, 2, trainsize)))
    for i in range(3):
        blocks.replace(GLASS, trainblock, positions.add(setpos, pos(2+4*i, 8, 0)), positions.add(setpos, pos(3+4*i, 12, trainsize*2)))
    blocks.replace(GLASS, trainblock, positions.add(setpos, pos(0, 8,2)), positions.add(setpos, pos(0, 12, 10)))

def createwheel(setpos, size):
    blocks.fill(trainblock, positions.add(setpos, pos(0, 0, -trainsize-4)), positions.add(setpos, pos(0, 0, trainsize+4)))
    for i in range(2):
        shapes.circle(trainblock, positions.add(setpos, pos(0, 0, -trainsize-2-i)), size-i, Axis.Z, ShapeOperation.REPLACE)
        shapes.circle(trainblock, positions.add(setpos, pos(0, 0, trainsize+2+i)), size-i, Axis.Z, ShapeOperation.REPLACE)

def createwagon(setpos):
    blocks.fill(trainblock, positions.add(setpos, pos(0, 0, -6)), positions.add(setpos, pos(30, 1, 6)))
    blocks.fill(wagonblock, positions.add(setpos, pos(0, 2, -6)), positions.add(setpos, pos(30, 10, 6)), FillOperation.HOLLOW)
    blocks.fill(roofblock, positions.add(setpos, pos(-1, 11, -7)), positions.add(setpos, pos(31, 11, 7)), FillOperation.HOLLOW)
    blocks.fill(roofblock, positions.add(setpos, pos(0, 12, -6)), positions.add(setpos, pos(30, 12, 6)), FillOperation.HOLLOW)
    for i in range(2):
        blocks.replace(GLASS, wagonblock, positions.add(setpos, pos(0, 4*i+4, -5)), positions.add(setpos, pos(30, 4*i+4, 5)))
        blocks.replace(GLASS, wagonblock, positions.add(setpos, pos(2, 4*i+4, -6)), positions.add(setpos, pos(28, 4*i+4, 6)))
    blocks.fill(trainblock, positions.add(setpos, pos(-8, 0, -1)), positions.add(setpos, pos(38, 1, 1)))
    for i in range(4):
        createwheel(positions.add(setpos, pos(10*i, -1, 0)), 3)
        blocks.fill(roofblock, positions.add(setpos, pos(30*(i%2), 2, -6+12*(i//2))), positions.add(setpos, pos(30*(i%2), 10, -6+12*(i//2))), FillOperation.HOLLOW)

player.on_chat("r", on_on_chat)
