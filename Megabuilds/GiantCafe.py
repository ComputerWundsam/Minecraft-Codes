startpos = pos(0, 0, 0)
housex = 32
housez = 30
checkeredplates = [BLACK_CONCRETE, WHITE_CONCRETE]
floorsize = 10
floorheight = 7
lightdistance = 6
roofblocks = [PLANKS_DARK_OAK, DARK_OAK_WOOD_SLAB]

def on_on_chat():
    global startpos
    startpos = player.position()
    loops.pause(3000)
    createcafebuilding()
player.on_chat("run", on_on_chat)

def createcafebuilding():
    createflooring(positions.add(startpos, pos(0, -1, -housez)), positions.add(startpos, pos(floorsize, -1, 0)))
    createhouse()
    createpavillon()
    createsideentrance()
    createsecondfloor()
    addfurniture()


def createhouse():
    blocks.fill(AIR, positions.add(startpos, pos(0, 0, 0)), positions.add(startpos, pos(-housex, floorheight, -housez)), FillOperation.REPLACE)
    blocks.fill(PLANKS_ACACIA, positions.add(startpos, pos(0, 0, 0)), positions.add(startpos, pos(-housex, floorheight, -housez)), FillOperation.HOLLOW)
    createsign()
    createwindows()
    createentrance(positions.add(startpos, pos(-housex/2, 0, -housez)))
    createlighting(positions.add(startpos, pos(-1, floorheight-1, -1)), positions.add(startpos, pos(-housex+1, floorheight-1, -housez+1)))



def createsign():
    blocks.replace(DARK_OAK_FENCE, AIR, positions.add(startpos, pos(-housex-1, floorheight+1, -housez-1)), positions.add(startpos, pos(1, floorheight, 1)))
    blocks.replace(AIR, DARK_OAK_FENCE, positions.add(startpos, pos(-housex, floorheight, -housez)), positions.add(startpos, pos(1, floorheight+1, 0)))
    player.execute("setblock " + positions.add(startpos, pos(-housex/2+2, floorheight, -housez-1)) + " element_20")
    player.execute("setblock " + positions.add(startpos, pos(-housex/2+1, floorheight, -housez-1)) + " element_26")

def createwindows():
    for i in range(housex/4):
        blocks.place(GLASS, positions.add(startpos, pos(-2-4*i, 3, 0)))
        blocks.place(GLASS, positions.add(startpos, pos(-2-4*i, 3, -housez)))


def createflooring(beginpos: Position  ,endpos: Position):
    player.say(beginpos)
    setx = endpos.get_value(Axis.X) - beginpos.get_value(Axis.X)
    setz = endpos.get_value(Axis.Z) - beginpos.get_value(Axis.Z)
    blocks.fill(AIR, endpos, positions.add(endpos, pos(1, 0, -setz)), FillOperation.REPLACE)
    for i in range(setx+1):
        blocks.fill(checkeredplates[i%checkeredplates.length], positions.add(beginpos, pos(i, 0, 0)), positions.add(beginpos, pos(i, 0, setz)), FillOperation.REPLACE)
    for i in range(setz/2):
        blocks.place(blocks.block_with_data(PISTON, 4), positions.add(beginpos,pos(-1, 0, 2*i+1)))
    for i in range(setz/2):
        blocks.place(REDSTONE_BLOCK, positions.add(beginpos,pos(-2, 0, 2*i+1)))
    loops.pause(500)
    blocks.fill(GRASS, positions.add(endpos, pos(1, 0, 0)), positions.add(endpos, pos(1, 0, -setz)), FillOperation.REPLACE)
    

def createpavillon():
    player.execute("gamerule randomtickspeed 2000")
    blocks.fill(CHERRY_PLANKS, positions.add(startpos, pos(1, floorheight, 0)), positions.add(startpos, pos(1+floorsize, floorheight, -housez)))
    for i in range(4):
        blocks.fill(CHERRY_LOG, positions.add(startpos, pos(1+(floorsize*(i//2)), 0, -housez*(i%2))), positions.add(startpos, pos(1+(floorsize*(i//2)), floorheight, -housez*(i%2))), FillOperation.REPLACE)
        blocks.place(GRASS, positions.add(startpos, pos(1+(floorsize*(i//2)), floorheight+1, -housez*(i%2))))
        blocks.place(CHERRY_SAPLING, positions.add(startpos, pos(1+(floorsize*(i//2)), floorheight+2, -housez*(i%2))))
    blocks.replace(CHERRY_FENCE, AIR, positions.add(startpos, pos(1, floorheight+1, 0)), positions.add(startpos, pos(1+floorsize, floorheight+1, -housez)))
    blocks.replace(AIR, CHERRY_FENCE, positions.add(startpos, pos(0, floorheight+1, -1)), positions.add(startpos, pos(floorsize, floorheight+1, -housez+1)))
    blocks.fill(LIGHT_BLUE_STAINED_GLASS, positions.add(startpos, pos(2, floorheight, -1)), positions.add(startpos, pos(floorsize, floorheight, -housez+1)), FillOperation.REPLACE)
    blocks.replace(CHERRY_FENCE, AIR, positions.add(startpos, pos(-1, 0, 0)), positions.add(startpos, pos(1+floorsize, 0, -housez)))
    blocks.fill(AIR, positions.add(startpos, pos(1, 0, -1)), positions.add(startpos, pos(floorsize, 0, -housez+1)))
    blocks.fill(CHERRY_FENCE, positions.add(startpos, pos(floorsize/2+2, 0, -housez)), positions.add(startpos, pos(floorsize/2-2, floorheight-1, -housez)))
    blocks.fill(AIR, positions.add(startpos, pos(floorsize/2+1, 0, -housez)), positions.add(startpos, pos(floorsize/2-1, floorheight-2, -housez)))
    loops.pause(2000)
    player.execute("gamerule randomtickspeed 1")
    blocks.replace(CHERRY_LOG, DIRT, positions.add(startpos,pos(-1, floorheight+1, 1)), positions.add(startpos,pos(floorsize+2, floorheight+1, -housez-1)))


def addfurniture():
    createbar()
    for i in range(floorsize/5):
        for j in range(housez/6):
            createtable(positions.add(startpos, pos(floorsize-2-i*5, 0, -housez+3+j*5)))
    for i in range(housex/12):
            for j in range(housez/5):
                createtable(positions.add(startpos, pos(-(housex/2)+3+i*5, floorheight+1, -housez+2+j*5)))
    for i in range(housex/12):
        for j in range(housez/10):
            createtable(positions.add(startpos, pos(-(housex/2)+3+i*5, 1, -(housez/2)+2+j*5)))
            createtable(positions.add(startpos, pos(-housex+9+i*5, 1, -housez+6+j*5)))
    for i in range(3):
        createbench(positions.add(startpos, pos(-housex+3+i, i*floorheight+1, -floorheight - 7)), housez - floorheight - 13)
    for i in range(2):
        for j in range(housez/6):
            createtable(positions.add(startpos, pos(-housex+10,  i*floorheight+1+floorheight, -housez+3+j*5)))

def createtable(setpos):
    blocks.place(OAK_FENCE, positions.add(setpos, pos(0, 0, 0)))
    blocks.place(LIME_CARPET, positions.add(setpos, pos(0, 1, 0)))
    for i in range(2):
        blocks.place(BAMBOO_SLAB, positions.add(setpos, pos(-1+2*i, 0, 0)))
        blocks.place(BAMBOO_SLAB, positions.add(setpos, pos(0, 0, -1+2*i)))
        blocks.place(blocks.block_with_data(BIRCH_TRAPDOOR, 13-i), positions.add(setpos, pos(-2+4*i, 0, 0)))
        blocks.place(blocks.block_with_data(BIRCH_TRAPDOOR, 15-i), positions.add(setpos, pos(0, 0, -2+4*i)))

def createbench(setpos, length):
    blocks.fill(BAMBOO_SLAB, positions.add(setpos, pos(-1, 0, 0)), positions.add(setpos, pos(1, 0, -length)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(BIRCH_TRAPDOOR, 13), positions.add(setpos, pos(-2, 0, 0)), positions.add(setpos, pos(-2, 0, -length)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(BIRCH_TRAPDOOR, 12), positions.add(setpos, pos(2, 0, 0)), positions.add(setpos, pos(2, 0, -length)), FillOperation.REPLACE)
    blocks.fill(OAK_FENCE, setpos, positions.add(setpos, pos(0, 0, -length)), FillOperation.REPLACE)
    blocks.fill(YELLOW_CARPET, positions.add(setpos, pos(0, 1, 0)), positions.add(setpos, pos(0, 1, -length)), FillOperation.REPLACE)


def createentrance(setpos):
    blocks.fill(PLANKS_ACACIA, positions.add(setpos, pos(-2, 0, -1)), positions.add(setpos, pos(2, floorheight-1, 1)))
    blocks.fill(AIR, positions.add(setpos, pos(1, 1, -1)), positions.add(setpos, pos(-1, floorheight-2, 1)))
    blocks.fill(PLANKS_ACACIA, positions.add(setpos, pos(2, 0, -2)), positions.add(setpos, pos(-2, 0, -3)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(ACACIA_WOOD_STAIRS, 2), positions.add(setpos, pos(2, 0, -3)), positions.add(setpos, pos(-2, 0, -3)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(ACACIA_WOOD_STAIRS, 1), positions.add(setpos, pos(3, 0, -1)), positions.add(setpos, pos(3, 0, -3)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(ACACIA_WOOD_STAIRS, 0), positions.add(setpos, pos(-3, 0, -1)), positions.add(setpos, pos(-3, 0, -3)), FillOperation.REPLACE)
    blocks.fill(LIGHT_BLUE_CARPET, positions.add(setpos, pos(1, 1, 0)), positions.add(setpos, pos(-1, 1, 1)))

    
def createsecondfloor():
    blocks.fill(PLANKS_ACACIA, positions.add(startpos, pos(-housex/2, floorheight, 0)), positions.add(startpos, pos(-housex, floorheight*2, -housez)), FillOperation.HOLLOW)
    createroof(positions.add(startpos, pos(-housex, 2*floorheight+1, 0)))
    createchimney()
    createstairs(positions.add(startpos, pos(-housex+1, 0, -floorheight-3)))
    createstairs(positions.add(startpos, pos(-housex+1, floorheight, -floorheight-3)))
    blocks.fill(ACACIA_FENCE, positions.add(startpos, pos(-housex+1, floorheight*2+1, -floorheight-4)), positions.add(startpos, pos(-housex+6, floorheight*2+1, -4)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-housex+1, floorheight*2+1, -floorheight-3)), positions.add(startpos, pos(-housex+5, floorheight*2+1, -4)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-housex/2, floorheight+1, -1)), positions.add(startpos, pos(-housex/2, floorheight+3, -3)), FillOperation.REPLACE)
    createlighting(positions.add(startpos, pos(-housex/2-1, 2*floorheight-1, -1)), positions.add(startpos, pos(-housex+1, 2*floorheight-1, -housez+1)))

def createstairs(setpos):
    blocks.fill(AIR, positions.add(setpos, pos(0, 1, 0)), positions.add(setpos, pos(4, floorheight+1, floorheight-1)), FillOperation.REPLACE)
    blocks.fill(PLANKS_ACACIA, positions.add(setpos, pos(5, 0, 0)), positions.add(setpos, pos(5, floorheight, floorheight)), FillOperation.REPLACE)
    for i in range(floorheight):
        blocks.fill(blocks.block_with_data(ACACIA_WOOD_STAIRS, 2), positions.add(setpos, pos(4, i+1, i)), 
                                positions.add(setpos, pos(0, i+1, i)), FillOperation.REPLACE)

def createlighting(beginpos: Position, endpos: Position):
    setx = abs((beginpos.get_value(Axis.X) - endpos.get_value(Axis.X))/lightdistance)
    setz = abs((beginpos.get_value(Axis.Z) - endpos.get_value(Axis.Z))/lightdistance)
    player.say(setz)
    for i in range(setx):
        for j in range(setz):
            blocks.place(PEARLESCENT_FROGLIGHT, positions.add(endpos, pos(lightdistance/2 + lightdistance*i, 0, lightdistance/2 + lightdistance*j)))

def createroof(setpos):
    for i in range(housex/2 + 1):
        roofblock = roofblocks[i%roofblocks.length]
        if i > 0:
            blocks.fill(PLANKS_DARK_OAK, positions.add(setpos, pos(i, 0, 0)), positions.add(setpos, pos(i, (i/2)-1, -housez)), FillOperation.REPLACE)  
            if i < (housex/2):
                blocks.fill(AIR, positions.add(setpos, pos(i, 0, -1)), positions.add(setpos, pos(i, (i/2)-1, -housez+1)), FillOperation.REPLACE)
        blocks.fill(roofblock, positions.add(setpos, pos(i, i/2, +1)), positions.add(setpos, pos(i, i/2, -housez-1)), FillOperation.REPLACE)
    blocks.replace(LIGHT_BLUE_STAINED_GLASS, PLANKS_DARK_OAK, positions.add(setpos, pos(housex/2, 1, -1)), positions.add(setpos, pos(housex/2+2, housex/2, -housez+1)))
    for i in range(housez/6):
        blocks.place(PEARLESCENT_FROGLIGHT, positions.add(setpos, pos(housex/2 - 1, housex/4 - 1, -housez+6*i+3)))

def createchimney():
    blocks.fill(BRICKS, positions.add(startpos, pos(-housex+3, 0, -housez+3)), positions.add(startpos, pos(-housex+1, floorheight*3, -housez+1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-housex+2, 0, -housez+2)), positions.add(startpos, pos(-housex+2, floorheight*3, -housez+2)), FillOperation.REPLACE)
    for i in range(2):
        blocks.replace(IRON_BARS, BRICKS, positions.add(startpos, pos(-housex+3, i*floorheight+2, -housez+3)), positions.add(startpos, pos(-housex+2, i*floorheight+4, -housez+2)))
        blocks.place(NETHERRACK, positions.add(startpos, pos(-housex+2, i*floorheight+1, -housez+2)))
        blocks.place(FIRE, positions.add(startpos, pos(-housex+2, i*floorheight+2, -housez+2)))
    blocks.place(HAY_BLOCK, positions.add(startpos, pos(-housex+2, floorheight*3-1, -housez+2)))
    blocks.place(CAMPFIRE, positions.add(startpos, pos(-housex+2, floorheight*3, -housez+2)))

def createsideentrance():
    blocks.fill(AIR,  positions.add(startpos, pos(0, 1, -1)),  positions.add(startpos,pos(0, 3, -3)), FillOperation.REPLACE)
    blocks.fill(ACACIA_WOOD_SLAB,  positions.add(startpos, pos(1, 0, -1)), positions.add(startpos,pos(1, 0, -4)), FillOperation.REPLACE)

def createbar():
    blocks.fill(BAMBOO_PLANKS, positions.add(startpos, pos(-1, 1, -housez+1)), positions.add(startpos, pos(-housex/4, 1, -housez/2)), FillOperation.REPLACE)
    blocks.fill(BAMBOO_SLAB, positions.add(startpos, pos(-1, 2, -housez+1)), positions.add(startpos, pos(-housex/4, 2, -housez/2)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-1, 1, -housez+1)), positions.add(startpos, pos(-housex/4+1, 2, -housez/2-1)), FillOperation.REPLACE)
    for i in range(housez/4 - 1):
        createbarchair(positions.add(startpos, pos(-housex/4-1, 1, -housez/2 - 1 - 2*i)))
    blocks.place(blocks.block_with_data(BIRCH_DOOR, 3), positions.add(startpos, pos(-housex/8, 1, -housez/2)))

    

def createbarchair(setpos):
    blocks.place(OAK_FENCE, positions.add(setpos, pos(0, 0, 0)))
    blocks.place(RED_CARPET, positions.add(setpos, pos(0, 1, 0)))
    blocks.place(blocks.block_with_data(MANGROVE_TRAPDOOR, 13), positions.add(setpos, pos(-1, 1, 0)))



def on_chat():
    global startpos
    startpos = player.position()
    for i in range(40):
        blocks.fill(AIR, pos(-20, i, -20), pos(20, i, 20), FillOperation.REPLACE)

player.on_chat("jump", on_chat)

