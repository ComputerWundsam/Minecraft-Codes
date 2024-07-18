platformarray = [30, 28, 26, 24, 22, 20, 18, 16, 14, 11, 9, 7, 6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0]
carrierblock = BLOCK_OF_NETHERITE
groundblock = BLACKSTONE
hullblock = IRON_BLOCK
lineblock = RED_CONCRETE
startpos = pos(0, 0, 0)
bdist = 6

def on_on_chat():
    global startpos
    startpos = player.position()
    partialplatform()
    startpos = positions.add(startpos, pos(platformarray.length, 0, 0))
    for i in range(7):
        fullplatform()
        startpos = positions.add(startpos, pos(30, 0, 0))
    createback()
    propeller(positions.add(startpos, pos(0, -platformarray.length+3, 0)))
    createtower(positions.add(startpos, pos(-50, 0, 30)))
    createsiderunway(positions.add(startpos, pos(-100, 0, -30)))
    createmainrunway()
    for i in range(9):
        createplane(positions.add(startpos, pos(-221 + 18*i, 4, 0)))
        createplane(positions.add(startpos, pos(-212 + 18*i, 4, 15)))

def createback():
    for j in range(platformarray.length):
        blocks.fill(hullblock, positions.add(startpos, pos(0, -j, -platformarray[j]-1)), positions.add(startpos, pos(0, -j, platformarray[j]+1)))
    
def propeller(wingpos):
    blocks.fill(carrierblock, wingpos, positions.add(wingpos, pos(bdist, 0, 0)))
    blocks.fill(carrierblock, positions.add(wingpos, pos(bdist, -(2*bdist+4), 0)), positions.add(wingpos, pos(bdist, 2*bdist+4, 0)))
    blocks.fill(carrierblock, positions.add(wingpos, pos(bdist, 0, -(2*bdist+4))), positions.add(wingpos, pos(bdist, 0, 2*bdist+4)))
    for i in range(7):
        blocks.fill(hullblock, positions.add(wingpos, pos(bdist, 3+2*i, 1)), positions.add(wingpos, pos(bdist, 4+2*i, 1+i)))
        blocks.fill(hullblock, positions.add(wingpos, pos(bdist, -(3+2*i), -1)), positions.add(wingpos, pos(bdist, -(4+2*i), -(1+i))))
        blocks.fill(hullblock, positions.add(wingpos, pos(bdist, -1, 3+2*i)), positions.add(wingpos, pos(bdist, -(1+i), 4+2*i)))
        blocks.fill(hullblock, positions.add(wingpos, pos(bdist, 1, -(3+2*i))), positions.add(wingpos, pos(bdist, 1+i, -(4+2*i))))
    
def fullplatform():
    for j in range(platformarray.length):
        blocks.fill(hullblock, positions.add(startpos, pos(0, -j, -platformarray[j]-1)), positions.add(startpos, pos(30, -j, platformarray[j]+1)))
        blocks.fill(groundblock, positions.add(startpos, pos(0, -j, -platformarray[j])), positions.add(startpos, pos(30, -j, platformarray[j])))
        

def partialplatform():
    for i in range(platformarray.length):
        blocks.fill(hullblock, positions.add(startpos, pos(i, -i, -platformarray[i]-1)), positions.add(startpos, pos(i, -i, platformarray[i]+1)))
        for j in range(i):
            blocks.fill(hullblock, positions.add(startpos, pos(i, -j, -platformarray[j]-1)), positions.add(startpos, pos(i, -j, platformarray[j]+1)))
            blocks.fill(groundblock, positions.add(startpos, pos(i, -j, -platformarray[j])), positions.add(startpos, pos(i, -j, platformarray[j])))


def createtower(setpos):
    blocks.fill(hullblock, setpos, positions.add(setpos, pos(40, 10, -30)))
    for i in range(3):
        blocks.replace(GLASS, hullblock, positions.add(setpos, pos(2, 2+3*i, 0)), positions.add(setpos, pos(38, 2+3*i, -30)))
        blocks.replace(GLASS, hullblock, positions.add(setpos, pos(0, 2+3*i, -2)), positions.add(setpos, pos(40, 2+3*i, -28)))
    for j in range(12):
        blocks.fill(hullblock, positions.add(setpos, pos(2+j, 11, -15+j)), positions.add(setpos, pos(38-j, 16, -15+j)))
        blocks.fill(hullblock, positions.add(setpos, pos(2+j, 11, -15-j)), positions.add(setpos, pos(38-j, 16, -15-j)))
    for j in range(2):
        blocks.replace(GLASS, hullblock, positions.add(setpos, pos(4, 12+2*j, 0)), positions.add(setpos, pos(36, 12+2*j, -30)))
    for j in range(3):
        blocks.fill(hullblock, positions.add(setpos, pos(33+j, 11+8*j, -12-j)), positions.add(setpos, pos(37-j, 24+8*j, -18+j)))
        blocks.fill(hullblock, positions.add(setpos, pos(35, 24+8*j, 0)), positions.add(setpos, pos(35, 24+8*j, -30)))
        blocks.replace(IRON_BARS, AIR, positions.add(setpos, pos(35, 18+8*j, -1)), positions.add(setpos, pos(35, 23+8*j, -29)))

def createsiderunway(setpos):
    for i in range(9):
        blocks.fill(groundblock, positions.add(setpos, pos(-i-2, 0, 0)), positions.add(setpos, pos(-i-2, 0, -32+4*i)))
        blocks.fill(hullblock, positions.add(setpos, pos(-i-3, 0, -28+4*i)), positions.add(setpos, pos(-i-3, 0, -32+4*i)))
    for i in range(32):
        blocks.fill(groundblock, positions.add(setpos, pos(3*i-2, 0, 0)), positions.add(setpos, pos(3*i, 0, -31+i)))
        blocks.fill(hullblock, positions.add(setpos, pos(3*i-2, 0, -32+i)), positions.add(setpos, pos(3*i, 0, -32+i)))
        blocks.fill(lineblock, positions.add(setpos, pos(3*i-2, 0, -26+i)), positions.add(setpos, pos(3*i, 0, -26+i)))
        blocks.fill(lineblock, positions.add(setpos, pos(3*i-5, 0, -10+i)), positions.add(setpos, pos(3*i-3, 0, -10+i)))

def createmainrunway():
    for i in range(26):
        blocks.replace(lineblock, groundblock, positions.add(startpos, pos(-10*i-10, 0, -10)), positions.add(startpos, pos(-10*i, 0, -10)))
        blocks.replace(lineblock, groundblock, positions.add(startpos, pos(-10*i-10, 0, -24)), positions.add(startpos, pos(-10*i, 0, -24)))
        if i % 2 == 0:
            blocks.replace(lineblock, groundblock, positions.add(startpos, pos(-10*i-10, 0, -17)), positions.add(startpos, pos(-10*i, 0, -17)))


def createplane(setpos):
    blocks.fill(carrierblock, positions.add(setpos, pos(0, 0, -3)), positions.add(setpos, pos(0, 0, -5)))
    for i in range(2):
        shapes.circle(carrierblock, positions.add(setpos, pos(0, 0, -2+i)), 1, Axis.Z, ShapeOperation.REPLACE)
    for i in range(13):
        shapes.circle(hullblock, positions.add(setpos, pos(0, 0, i)), 2, Axis.Z, ShapeOperation.REPLACE)
    shapes.circle(carrierblock, positions.add(setpos, pos(0, 0, i)), 1, Axis.Z, ShapeOperation.REPLACE)
    blocks.place(MAGMA_BLOCK, positions.add(setpos, pos(0, 0, i)))
    for i in range(4):
        blocks.fill(hullblock, positions.add(setpos, pos(-3-i, 0, 6+2*i)), positions.add(setpos, pos(3+i, 0, 5+2*i)))
    blocks.replace(BLACK_STAINED_GLASS, hullblock, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 2, 2)))
    blocks.place(BLACK_WOOL, positions.add(setpos, pos(0, -3, 3)))
    blocks.place(BLACK_WOOL, positions.add(setpos, pos(0, -3, 11)))

player.on_chat("run", on_on_chat)
