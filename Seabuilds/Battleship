outsideblocks = [RED_CONCRETE,  BLOCK_OF_NETHERITE, IRON_BLOCK, PLANKS_BIRCH]
hullpartsize = [12, 2, 8, 0]


radius = 24
pi = 3.14159265359
startpos = pos(0, 0,0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createhull()
    createcentralbridge()
    createcannons()



def createhull():
    global startpos
    for j in range(outsideblocks.length):
        for i in range(2*radius*pi):
            blocks.fill(outsideblocks[j], positions.add(startpos, pos(0, 0, 0)), positions.add(startpos, pos(Math.sin(i/radius)*radius*8, hullpartsize[j], Math.cos(i/radius)*radius)), FillOperation.REPLACE)
        startpos = positions.add(startpos, pos(0, hullpartsize[j]+1, 0))
    for i in range(2*radius*pi):
        blocks.fill(NETHER_BRICK_FENCE, positions.add(startpos, pos(Math.sin((i-1)/radius)*radius*8, 0, Math.cos((i-1)/radius)*radius)), positions.add(startpos, pos(Math.sin(i/radius)*radius*8, 0, Math.cos(i/radius)*radius)), FillOperation.REPLACE)
        

def createcentralbridge():
    for i in range(radius/2):
        blocks.fill(IRON_BLOCK, positions.add(startpos, pos(-radius*3, i, -radius/2)), positions.add(startpos, pos(radius*3-i, i, radius/2)), FillOperation.REPLACE)
    blocks.fill(NETHER_BRICK_FENCE, positions.add(startpos, pos(-radius*3, i, -radius/2+1)), positions.add(startpos, pos(radius*3-i-1, i, radius/2-1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-radius*3+1, i, -radius/2+2)), positions.add(startpos, pos(radius*3-i-2, i, radius/2-2)), FillOperation.REPLACE)

    blocks.fill(IRON_BLOCK, positions.add(startpos, pos(-radius, radius/2, -radius/3)), positions.add(startpos, pos(radius, radius, radius/3)), FillOperation.REPLACE)
    sradius = radius/8
    for i in range(3):
        blocks.replace(GLASS, IRON_BLOCK, positions.add(startpos, pos(radius-1, radius/2 + (sradius)*i+1, radius/3)), positions.add(startpos,pos(-radius+1,radius/2 + (sradius)*i+1, -radius/3)))
        blocks.replace(GLASS, IRON_BLOCK, positions.add(startpos, pos(radius, radius/2 + (sradius)*i+1, radius/3-1)), positions.add(startpos,pos(-radius,radius/2 + (sradius)*i+1, -radius/3+1)))
    blocks.replace(GLASS, IRON_BLOCK, positions.add(startpos, pos(radius*3, radius/3, radius)), positions.add(startpos,pos(radius*2, radius/3+2, -radius)))
    for i in range(4):
        blocks.replace(GLASS, IRON_BLOCK, positions.add(startpos, pos(radius*2-2, radius/4 * i/2+1, radius)), positions.add(startpos,pos(-radius*3, radius/4 * i/2+1, -radius)))
    createtower(positions.add(startpos, pos(radius, radius, 0)))
    createtower(positions.add(startpos, pos(-radius, radius, 0)))


def createtower(setpos):
    blocks.fill(IRON_BLOCK, setpos, positions.add(setpos, pos(0, radius, 0)))
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, radius*4/5, -radius)), positions.add(setpos, pos(0, radius*4/5, radius)))
    blocks.replace(IRON_BARS, AIR, positions.add(setpos, pos(0, radius*4/5, -radius)), positions.add(setpos, pos(0, radius/4, radius)))
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, radius/3, -radius/2)), positions.add(setpos, pos(0, radius/3, radius/2)))


def createcannons():
    createcannon(positions.add(startpos, pos(5*radius, 0, 0)), radius/2, radius/4, 1)
    createcannon(positions.add(startpos, pos(-5*radius, 0, 0)), radius/2, radius/4, -1)
    createcannon(positions.add(startpos, pos(radius/2, 0, radius*3/4)), radius/6, radius/6, 1)
    createcannon(positions.add(startpos, pos(radius/2, 0, -radius*3/4)), radius/6, radius/6, 1)
    createcannon(positions.add(startpos, pos(-radius/2, 0, radius*3/4)), radius/6, radius/6, -1)
    createcannon(positions.add(startpos, pos(-radius/2, 0, -radius*3/4)), radius/6, radius/6, -1)
    createcannon(positions.add(startpos, pos(radius*3.5, 0, radius/2)), radius/4, radius/6, 1)
    createcannon(positions.add(startpos, pos(radius*3.5, 0, -radius/2)), radius/4, radius/6, 1)
    createcannon(positions.add(startpos, pos(-radius*3.5, 0, radius/2)), radius/4, radius/6, -1)
    createcannon(positions.add(startpos, pos(-radius*3.5, 0, -radius/2)), radius/4, radius/6, -1)



def createcannon(setpos, csize, cheight, cdir):
    shapes.circle(IRON_BLOCK, positions.add(setpos, pos(0, -1, 0)), csize+2, Axis.Y, ShapeOperation.REPLACE)
    for i in range(2*csize*pi):
        blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(Math.sin(i/csize)*csize, cheight, Math.cos(i/csize)*csize)), FillOperation.REPLACE)

    blocks.fill(BLOCK_OF_NETHERITE, positions.add(setpos, pos(0, cheight-1 - csize/6, -csize*(4/6))), positions.add(setpos, pos(csize*2*cdir, cheight-1, -csize*(5/6))), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, positions.add(setpos, pos(0, cheight-1 - csize/6, csize*(4/6))), positions.add(setpos, pos(csize*2*cdir, cheight-1, csize*(5/6))), FillOperation.REPLACE)


player.on_chat("run", on_on_chat)
