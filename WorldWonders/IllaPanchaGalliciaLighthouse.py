outerhousesize = 24
househeight = 8
roofheight = 8
innerhousesize = 0

startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos, innerhousesize
    innerhousesize = outerhousesize-2*roofheight
    startpos = player.position()
    loops.pause(5000)
    flatten(outerhousesize+innerhousesize)
    createbasewalls(startpos, outerhousesize)
    createlowerfloor()
    createroof(outerhousesize)
    createbasewalls(positions.add(startpos, pos(0, househeight+roofheight, 0)), innerhousesize)
    createlighthouse(positions.add(startpos, pos(0, 2*househeight+roofheight+1, 0)), innerhousesize)

def flatten(setsize):
    for i in range(setsize):
        blocks.fill(AIR, positions.add(startpos, pos(-i, 0, -setsize)), positions.add(startpos, pos(-i, 5*househeight, setsize)), FillOperation.REPLACE)
        blocks.fill(AIR, positions.add(startpos, pos(i, 0, -setsize)), positions.add(startpos, pos(i, 5*househeight, setsize)), FillOperation.REPLACE)

def createbasewalls(setpos, housesize):
    blocks.fill(WHITE_CONCRETE, positions.add(setpos, pos(-housesize, -1, -housesize)), positions.add(setpos, pos(housesize, househeight, housesize)), FillOperation.HOLLOW)
    for i in range(4):
        blocks.fill(LIGHT_BLUE_CONCRETE, positions.add(setpos,pos(-housesize, househeight * (i//2), -housesize + (2*housesize*(i%2)))), 
                                    positions.add(setpos, pos(housesize, househeight * (i//2), -housesize + (2*housesize*(i%2)))), FillOperation.REPLACE)
        blocks.fill(LIGHT_BLUE_CONCRETE, positions.add(setpos, pos(-housesize + (2*housesize*(i%2)), househeight * (i//2), -housesize)), 
                                    positions.add(setpos, pos(-housesize + (2*housesize*(i%2)), househeight * (i//2), housesize)), FillOperation.REPLACE)
        blocks.fill(LIGHT_BLUE_CONCRETE, positions.add(setpos, pos(-housesize + (2*housesize*(i%2)), 0, -housesize + (2*housesize*(i//2)))), 
                                    positions.add(setpos, pos(-housesize + (2*housesize*(i%2)), househeight, -housesize + (2*housesize*(i//2)))), FillOperation.REPLACE)

def createroof(housesize):
    for i in range(roofheight):
        blocks.fill(BLACKSTONE_SLAB, positions.add(startpos, pos(-housesize-1+2*i, househeight+1+i, -housesize-1+2*i)), positions.add(startpos, pos(housesize+1-2*i, househeight+1+i, housesize+1-2*i)), FillOperation.REPLACE)
        blocks.fill(BLACKSTONE, positions.add(startpos, pos(-housesize+2*i, househeight+1+i, -housesize+2*i)), positions.add(startpos, pos(housesize-2*i, househeight+1+i, housesize-2*i)), FillOperation.REPLACE)
player.on_chat("run", on_on_chat)


def createlowerfloor():
    blocks.fill(STONE_BRICKS, positions.add(startpos, pos(-outerhousesize-4, -1, -outerhousesize-4)), positions.add(startpos, pos(outerhousesize+4, -1, outerhousesize+4)), FillOperation.HOLLOW)
    for j in range(2):
        for i in range(3):
            createwindow(positions.add(startpos, pos(-outerhousesize/2 + (i*outerhousesize/2), 0, -outerhousesize + 2*outerhousesize*j)))
    createwindow(positions.add(startpos, pos(-outerhousesize, 0, 0)))
    createwindow(positions.add(startpos, pos(outerhousesize, 0, outerhousesize/2)))
    createwindow(positions.add(startpos, pos(outerhousesize, 0, -outerhousesize/2)))
    createmaindoor(positions.add(startpos, pos(outerhousesize, 0, 0)))

def createmaindoor(setpos):
    blocks.replace(LIGHT_BLUE_CONCRETE, WHITE_CONCRETE, positions.add(setpos, pos(-1, 2, -1)), positions.add(setpos, pos(1, 0, 1)))
    blocks.place(ACACIA_DOOR, setpos)

def createwindow(setpos):
    blocks.replace(LIGHT_BLUE_CONCRETE, WHITE_CONCRETE, positions.add(setpos, pos(-2, househeight/2-(househeight/4), -2)), positions.add(setpos, pos(2, househeight/2+(househeight/4), 2)))
    blocks.replace(IRON_BARS, LIGHT_BLUE_CONCRETE, positions.add(setpos, pos(-1, househeight/2-(househeight/4)+1, -1)), positions.add(setpos, pos(1, househeight/2+(househeight/4)-1, 1)))
    
def createlighthouse(setpos, housesize):
    halfhousesize = housesize/2
    blocks.fill(LIGHT_BLUE_CONCRETE, positions.add(setpos, pos(-housesize-1, 0, -housesize-1)), positions.add(setpos, pos(housesize+1, 0, housesize+1)), FillOperation.REPLACE)
    blocks.fill(DARK_OAK_FENCE, positions.add(setpos, pos(-housesize-1, 1, -housesize-1)), positions.add(setpos, pos(housesize+1, 1, housesize+1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(-housesize, 1, -housesize)), positions.add(setpos, pos(housesize, 1, housesize)), FillOperation.REPLACE)
    blocks.fill(BRICKS, positions.add(setpos, pos(-halfhousesize, 1, -halfhousesize)), positions.add(setpos, pos(halfhousesize, househeight/2, halfhousesize)), FillOperation.REPLACE)
    blocks.fill(GLASS, positions.add(setpos, pos(-halfhousesize+1, househeight, -halfhousesize+1)), positions.add(setpos, pos(halfhousesize-1, househeight/2, halfhousesize-1)), FillOperation.REPLACE)
    blocks.fill(GLOWSTONE, positions.add(setpos, pos(-halfhousesize+2, househeight, -halfhousesize+2)), positions.add(setpos, pos(halfhousesize-2, househeight/2, halfhousesize-2)), FillOperation.REPLACE)
    for i in range(halfhousesize/2):
        blocks.fill(BLACKSTONE_SLAB, positions.add(setpos, pos(-halfhousesize-1+2*i, househeight+1+i, -halfhousesize-1+2*i)), positions.add(setpos, pos(halfhousesize+1-2*i, househeight+1+i, halfhousesize+1-2*i)), FillOperation.REPLACE)
        blocks.fill(BLACKSTONE, positions.add(setpos, pos(-halfhousesize+2*i, househeight+1+i, -halfhousesize+2*i)), positions.add(setpos, pos(halfhousesize-2*i, househeight+1+i, halfhousesize-2*i)), FillOperation.REPLACE)
