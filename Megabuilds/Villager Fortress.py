setsize = 160
setheight = 40
setwidth = 2
wallbrick = STONE_BRICKS

def on_on_chat(size, height):
    global setsize, setheight
    setheight = height
    setsize = size
    startpos = player.position()
    flatten(startpos)
    createwalls(startpos, setsize, setheight, setwidth)
    createtowers(startpos, setsize, setheight, setwidth)
    createdoors(startpos, setsize, setwidth)
    spawninhabitants(startpos, setsize)

def flatten(startpos):
    for i in range(setsize/2):
        for j in range(setsize/2):
            blocks.fill(AIR, positions.add(startpos, pos(-setsize-5+5*i, 0, -setsize-5+5*j)), positions.add(startpos, pos(-setsize+5+5*i, setheight+10, -setsize+5+5*j)))

def createwalls(startpos, wallsize, wallheight, wallwidth):
    for i in range(wallsize*2):
        blocks.fill(wallbrick, positions.add(startpos, pos(-wallsize+i-wallwidth, 0, -wallsize-wallwidth)), positions.add(startpos, pos(-wallsize+i+wallwidth, wallheight,  -wallsize+wallwidth)), FillOperation.REPLACE)
        blocks.fill(wallbrick, positions.add(startpos, pos(wallsize-i-wallwidth, 0, wallsize-wallwidth)), positions.add(startpos, pos(wallsize-i+wallwidth, wallheight,  wallsize+wallwidth)), FillOperation.REPLACE)
        blocks.fill(wallbrick, positions.add(startpos, pos(-wallsize-wallwidth, 0, wallsize-i-wallwidth)), positions.add(startpos, pos(-wallsize+wallwidth, wallheight,  wallsize-i+wallwidth)), FillOperation.REPLACE)
        blocks.fill(wallbrick, positions.add(startpos, pos(wallsize-wallwidth, 0, -wallsize+i-wallwidth)), positions.add(startpos, pos(wallsize+wallwidth, wallheight,  -wallsize+i+wallwidth)), FillOperation.REPLACE)
        if i%2 == 0:
            blocks.place(wallbrick, positions.add(startpos, pos(wallsize+wallwidth, wallheight+1, -wallsize+i-wallwidth)))
            blocks.place(wallbrick, positions.add(startpos, pos(-wallsize-wallwidth, wallheight+1, wallsize-i+wallwidth)))
            blocks.place(wallbrick, positions.add(startpos, pos(-wallsize+i-wallwidth, wallheight+1, -wallsize-wallwidth)))
            blocks.place(wallbrick, positions.add(startpos, pos(wallsize-i+wallwidth, wallheight+1, wallsize+wallwidth)))


def createtowers(startpos, wallsize, wallheight, wallwidth):
    for i in range(4):
        blocks.fill(wallbrick, positions.add(startpos, pos(-wallsize-wallwidth + ((i%2)*2*wallsize -2), 0, -wallsize-wallwidth + ((i//2)*2*wallsize) -2)), 
            positions.add(startpos, pos(-wallsize+wallwidth + ((i%2)*2*wallsize) +2, wallheight+10, -wallsize+wallwidth + ((i//2)*2*wallsize) +2)))
        blocks.fill(AIR, positions.add(startpos, pos(-wallsize-wallwidth + ((i%2)*2*wallsize -1), wallheight+10, -wallsize-wallwidth + ((i//2)*2*wallsize) -1)),
                positions.add(startpos, pos(-wallsize+wallwidth + ((i%2)*2*wallsize) +1, wallheight+10, -wallsize+wallwidth + ((i//2)*2*wallsize) +1)))


def createdoors(startpos, wallsize, wallwidth):
    blocks.fill(AIR, positions.add(startpos, pos(-wallsize-wallwidth, 0, -wallwidth)), positions.add(startpos, pos(-wallsize+wallwidth, 4,  wallwidth)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(wallsize-wallwidth, 0, -wallwidth)), positions.add(startpos, pos(wallsize+wallwidth, 4,  wallwidth)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-wallwidth, 0, -wallsize-wallwidth)), positions.add(startpos, pos(wallwidth, 4,  -wallsize+wallwidth)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-wallwidth, 0, wallsize-wallwidth)), positions.add(startpos, pos(wallwidth, 4,  wallsize+wallwidth)), FillOperation.REPLACE)
    createstreets(startpos, wallsize, wallwidth)

def createstreets(startpos, wallsize, wallwidth):
    for i in range(2*wallsize+wallwidth):
        blocks.fill(COBBLESTONE, positions.add(startpos, pos(-wallsize-wallwidth+i, -1, -wallwidth)), positions.add(startpos, pos(-wallsize+wallwidth+i, -1, wallwidth)))
        blocks.fill(COBBLESTONE, positions.add(startpos, pos(-wallwidth, -1, -wallsize-wallwidth+i)), positions.add(startpos, pos(wallwidth, -1, -wallsize+wallwidth+i)))
    createhouse(positions.add(startpos, pos(3, 0, 3)), wallsize-2*wallwidth-4)
    createhouse(positions.add(startpos, pos(-wallsize+5, 0, 3)), wallsize-2*wallwidth-4)
    createhouse(positions.add(startpos, pos(3, 0, -wallsize+5)), wallsize-2*wallwidth-4)
    createhouse(positions.add(startpos, pos(-wallsize+5, 0, -wallsize+5)), wallsize-2*wallwidth-4)


def createhouse(setpos, wallsize):
    blocks.fill(PLANKS_OAK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(wallsize, 4, 0)))
    blocks.fill(PLANKS_OAK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(0, 4, wallsize)))
    blocks.fill(PLANKS_OAK, positions.add(setpos, pos(wallsize, 0, wallsize)), positions.add(setpos, pos(wallsize, 4, 0)))
    blocks.fill(PLANKS_OAK, positions.add(setpos, pos(wallsize, 0, wallsize)), positions.add(setpos, pos(0, 4, wallsize)))
    blocks.fill(BED, positions.add(setpos, pos(3, 0, 3)), positions.add(setpos, pos(wallsize-3, 0, wallsize-3)))
    blocks.place(DARK_OAK_DOOR, positions.add(setpos, pos(0, 0, 2)))
    blocks.place(DARK_OAK_DOOR, positions.add(setpos, pos(wallsize, 0, 2)))
    blocks.place(DARK_OAK_DOOR, positions.add(setpos, pos(0, 0, wallsize-2)))
    blocks.place(DARK_OAK_DOOR, positions.add(setpos, pos(wallsize, 0, wallsize-2)))
    blocks.fill(OCHRE_FROGLIGHT, positions.add(setpos, pos(3, 4, 3)), positions.add(setpos, pos(wallsize-3, 4, wallsize-3)))
    for i in range(wallsize/2):
        blocks.fill(PLANKS_DARK_OAK, positions.add(setpos, pos(0+i, 5+i, 0+i)), positions.add(setpos, pos(wallsize-i, 5+i, wallsize-i)))

def spawninhabitants(startpos, wallsize):
    for i in range(4*wallsize):
        mobs.spawn(VILLAGER, positions.add(startpos, pos(randint(-wallsize+4, wallsize-4), 1, randint(-wallsize+4, wallsize-4))))

player.on_chat("run", on_on_chat)
