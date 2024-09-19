width = 16
depth = 40
height = 20
radius = 5
wradius = 4
pi = 3.14159265359
startpos = player.position()
wallbrick = STONE_BRICKS

def on_on_chat():
    global startpos
    startpos = player.position()
    loops.pause(5000)
    flatten()
    createship()
    for i in range(4):
        createtowers(positions.add(startpos, pos(-width + (2*width) * (i%2), 0, depth * (i//2))))
    creategate()
    createwindows()
    createinterior()
    createlamps()

def flatten():
    for i in range(2*height+2):
        blocks.fill(AIR, positions.add(startpos, pos(-width-radius, 2*height-i, -radius)), positions.add(startpos, pos(width+radius, 2*height-i, depth+radius)), FillOperation.REPLACE)

def createship():
    blocks.fill(wallbrick, positions.add(startpos, pos(width, -1, depth)), positions.add(startpos, pos(-width, -1, 0)), FillOperation.REPLACE)
    blocks.fill(wallbrick, positions.add(startpos, pos(width+1, -1, depth)), positions.add(startpos, pos(width+1, height-1, 0)), FillOperation.REPLACE)
    blocks.fill(wallbrick, positions.add(startpos, pos(-width-1, -1, depth)), positions.add(startpos, pos(-width-1, height-1, 0)), FillOperation.REPLACE)
    blocks.fill(wallbrick, positions.add(startpos, pos(width, 0, 0)), positions.add(startpos, pos(-width, height, 0)), FillOperation.REPLACE)
    blocks.fill(wallbrick, positions.add(startpos, pos(width, 0, depth)), positions.add(startpos, pos(-width, height, depth)), FillOperation.REPLACE)
    for i in range(width+1):
        blocks.fill(wallbrick, positions.add(startpos, pos(width-i, height, 0)), positions.add(startpos, pos(-width+i, height+i, 0)), FillOperation.REPLACE)
        blocks.fill(wallbrick, positions.add(startpos, pos(width-i, 0, depth)), positions.add(startpos, pos(-width+i, height+i, depth)), FillOperation.REPLACE)
        blocks.replace(blocks.block_with_data(STONE_BRICK_STAIRS, 1), AIR, positions.add(startpos, pos(width-i+1, height+i, 0)), positions.add(startpos, pos(width-i+1, height+i, depth)))
        blocks.replace(blocks.block_with_data(STONE_BRICK_STAIRS, 0), AIR, positions.add(startpos, pos(-width+i-1, height+i, 0)), positions.add(startpos, pos(-width+i-1, height+i, depth)))
    blocks.replace(STONE_BRICKS_SLAB, AIR, positions.add(startpos, pos(0, height+width+1, 0)), positions.add(startpos, pos(0, height+width+1, depth)))

def createtowers(setpos):
    for i in range(radius*pi*2):
        blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(Math.sin(i/radius)*radius-1, 0, Math.cos(i/radius)*radius-1)), positions.add (setpos, pos(Math.sin(i/radius)*radius+1, 2*height, Math.cos(i/radius)*radius+1)), FillOperation.REPLACE)
        blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(0, 2*height-1, 0)), positions.add (setpos, pos(Math.sin(i/radius)*radius, 2*height-1, Math.cos(i/radius)*radius)), FillOperation.REPLACE)

def creategate():
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(-3, -1, -1)), positions.add(startpos, pos(3, 3, 1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-2, 0, -1)), positions.add(startpos, pos(2, 2, 1)), FillOperation.REPLACE)

def createinterior():
    blocks.fill(RED_CARPET, positions.add(startpos, pos(-2, 0, 2)), positions.add(startpos, pos(2, 0, depth-1)), FillOperation.REPLACE)
    for i in range(depth/3):
        blocks.replace(blocks.block_with_data(OAK_WOOD_STAIRS, 3), AIR, positions.add(startpos, pos(-width+1, 0, 2 + 2*i)), positions.add(startpos, pos(width-1, 0,  2 + 2*i)))
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(startpos, pos(-5, 0, 4*depth/5)), positions.add(startpos, pos(5, 0, depth-1)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 2), positions.add(startpos, pos(-5, 0, 4*depth/5-1)), positions.add(startpos, pos(5, 0, 4*depth/5-1)), FillOperation.REPLACE)
    blocks.fill(GOLD_BLOCK, positions.add(startpos, pos(-2, 1, 9*depth/10)), positions.add(startpos,  pos(2, 1, 9*depth/10)), FillOperation.REPLACE)
    blocks.fill(RED_CARPET, positions.add(startpos, pos(-2, 2, 9*depth/10)), positions.add(startpos, pos(2, 2, 9*depth/10)), FillOperation.REPLACE)

def createlamps():
    for i in range(depth/4 - 1):
            blocks.replace(OAK_FENCE, AIR, positions.add(startpos, pos(-width+1, height, 6 + i*4)), positions.add(startpos, pos(width-1, height, 6 + i*4)))
    for i in range(width/4):
        for j in range(depth/4 - 1):
            for k in range(2):
                blocks.replace(OAK_FENCE, AIR, positions.add(startpos, pos((-2 - i*4) * (-1 + 2*k), height - 1, 6 + j*4)), positions.add(startpos, pos((-2 - i*4) * (-1 + 2*k), height - 1, 6 + j*4)))
                blocks.replace(OCHRE_FROGLIGHT, AIR, positions.add(startpos, pos((-2 - i*4) * (-1 + 2*k), height - 2, 6 + j*4)), positions.add(startpos, pos((-2 - i*4) * (-1 + 2*k), height - 2, 6 + j*4)))


def createwindows():
    for i in range (2*wradius*pi):
        blocks.replace(WHITE_STAINED_GLASS, wallbrick, positions.add(startpos, pos(0, height, 0)), positions.add(startpos, pos(Math.cos(i/wradius)*radius, height + Math.sin(i/wradius)*radius, depth)))
    blocks.replace(YELLOW_STAINED_GLASS, WHITE_STAINED_GLASS, positions.add(startpos, pos(-1, height-wradius-2, 0)), positions.add(startpos,pos(1, height+wradius+2, depth)))
    blocks.replace(YELLOW_STAINED_GLASS, WHITE_STAINED_GLASS, positions.add(startpos, pos(-wradius-2, height-1, -1)), positions.add(startpos, pos(wradius+2, height+1, depth+1)))

player.on_chat("run", on_on_chat)


# def on_travelled_walk():
#      blocks.fill(AIR, pos(-10, -10, -10), pos(10, 10, 10))
# player.on_travelled(FLY, on_travelled_walk)
