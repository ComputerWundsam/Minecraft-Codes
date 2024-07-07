hullblock = IRON_BLOCK
jetblock = BLACK_CONCRETE
glassblock = GLASS
lightblock = OCHRE_FROGLIGHT
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createtip()
    createhull()
    createwings(startpos)
    createnozzle()


def createhull():
    global startpos
    for i in range(25):
        if(i%4 == 0):
            setblock = jetblock
            blocks.place(lightblock, positions.add(startpos, pos(-1, -8, 0)))
            blocks.place(lightblock, positions.add(startpos, pos(-1, 8, 0)))
            blocks.place(lightblock, positions.add(startpos, pos(-1, 0, -8)))
            blocks.place(lightblock, positions.add(startpos, pos(-1, 0, 8)))
        else:
            setblock = hullblock
        shapes.circle(setblock, startpos, 8, Axis.X, ShapeOperation.REPLACE) 
        if(i%4 == 2):
            blocks.replace(glassblock, hullblock, positions.add(startpos, pos(0, -8, -1)), positions.add(startpos, pos(0, 8, 1)))
            blocks.replace(glassblock, hullblock, positions.add(startpos, pos(0, -1, -8)), positions.add(startpos, pos(0, 1, 8)))
        startpos = positions.add(startpos, pos(1, 0, 0))


def createtip():
    global startpos
    blocks.place(lightblock, positions.add(startpos, pos(-1, -6, 0)))
    for i in range(7):
        shapes.circle(hullblock, positions.add(startpos, pos(0, -6+i, 0)), 1+i, Axis.X, ShapeOperation.REPLACE)
        startpos = positions.add(startpos, pos(1, 0, 0))
        for j in range(2):
            shapes.circle(hullblock, positions.add(startpos, pos(0, -6+i, 0)), 1+i, Axis.X, ShapeOperation.REPLACE)
            shapes.circle(hullblock, positions.add(startpos, pos(0, -5+i, 0)), 1+i, Axis.X, ShapeOperation.REPLACE)
            startpos = positions.add(startpos, pos(1, 0, 0))
    blocks.replace(glassblock, hullblock, positions.add(startpos, pos(-2, 2, 8)), positions.add(startpos, pos(-10, 3, -8)))
    blocks.replace(lightblock, hullblock, positions.add(startpos, pos(-1, 2, 6)), positions.add(startpos, pos(-1, 3, -6)))


def createwings(setpos):
    for i in range(9):
        blocks.fill(hullblock, positions.add(setpos, pos(-i-1, 9, 0)), positions.add(setpos, pos(-i-1, 17-i, 0)))
        blocks.fill(hullblock, positions.add(setpos, pos(-i-1, -9, 0)), positions.add(setpos, pos(-i-1, -17+i, 0)))
        blocks.fill(hullblock, positions.add(setpos, pos(-i-1, 0, 9)), positions.add(setpos, pos(-i-1, 0, 17-i)))
        blocks.fill(hullblock, positions.add(setpos, pos(-i-1, 0, -9)), positions.add(setpos, pos(-i-1, 0, -17+i)))
    blocks.place(lightblock, positions.add(setpos, pos(-1, -18, 0)))
    blocks.place(lightblock, positions.add(setpos, pos(-1, 18, 0)))
    blocks.place(lightblock, positions.add(setpos, pos(-1, 0, -18)))
    blocks.place(lightblock, positions.add(setpos, pos(-1, 0, 18)))

def createnozzle():
    global startpos
    for i in range(6):
        shapes.circle(jetblock, startpos, 4+i, Axis.X, ShapeOperation.REPLACE)
        startpos = positions.add(startpos, pos(1, 0, 0))
    shapes.circle(MAGMA_BLOCK, startpos, 7, Axis.X, ShapeOperation.REPLACE)

player.on_chat("r", on_on_chat)
