platformarray = [30, 28, 26, 24, 22, 20, 18, 16, 14, 11, 9, 7, 6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0]
carrierblock = BLACKSTONE
groundblock = BLACKSTONE
hullblock = IRON_BLOCK
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    partialplatform()
    startpos = positions.add(startpos, pos(platformarray.length, 0, 0))
    for i in range(8):
        fullplatform()
        startpos = positions.add(startpos, pos(30, 0, 0))
    for i in range(6):
        createplane(positions.add(startpos, pos(-242 + 18*i, 3, 15)))
    createtower(positions.add(startpos, pos(-80, 0, 0)))

    
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
    blocks.fill(hullblock, setpos, positions.add(setpos, pos(80, 10, -30)))


def createplane(setpos):
    blocks.fill(carrierblock, positions.add(setpos, pos(0, 0, -4)), positions.add(setpos, pos(0, 0, -6)))
    for i in range(3):
        shapes.circle(carrierblock, positions.add(setpos, pos(0, 0, -3+i)), 1, Axis.Z, ShapeOperation.REPLACE)
    for i in range(15):
        shapes.circle(hullblock, positions.add(setpos, pos(0, 0, i)), 2, Axis.Z, ShapeOperation.REPLACE)
    for i in range(5):
        blocks.fill(hullblock, positions.add(setpos, pos(-3-i, 0, 6+2*i)), positions.add(setpos, pos(3+i, 0, 5+2*i)))
    blocks.replace(BLACK_STAINED_GLASS, hullblock, positions.add(setpos, pos(0, 2, 0)), positions.add(setpos, pos(0, 2, 3)))
    blocks.place(BLACK_WOOL, positions.add(setpos, pos(0, -3, 3)))
    blocks.place(BLACK_WOOL, positions.add(setpos, pos(0, -3, 13)))

player.on_chat("run", on_on_chat)


