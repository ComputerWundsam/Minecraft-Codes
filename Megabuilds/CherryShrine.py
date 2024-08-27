pi = 3.14159265359
radius = 50
layers = 5

height = 8
reduction = 5

startpos = pos(0, 0, 0)


def on_on_chat():
    global radius, startpos, reduction
    reduction = radius/layers
    startpos = player.position()
    loops.pause(5000)
    for i in range(radius/reduction):
        createcircle(radius-reduction*i, positions.add(startpos, pos(reduction*i, height*i, 0)))
        createstairs(positions.add(startpos, pos(-radius-height+3 + (2*reduction*i), height*i, 0)))
        createpathway(positions.add(startpos, pos(reduction*i, height*(i+1)-1, 0)))
        planttrees(radius-reduction*i-2, positions.add(startpos, pos(reduction*i, height*(i+1), 0)))
    createcentralarch(positions.add(startpos, pos(radius-reduction, height*layers, 0)), reduction)


    

def createcentralarch(setpos, setradius):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(-1, 0, -setradius-1)), positions.add(setpos,pos(1, height*3, -setradius+1)), FillOperation.REPLACE)
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(-1, 0, setradius-1)), positions.add(setpos,pos(1, height*3, setradius+1)), FillOperation.REPLACE)
    for i in range(2*setradius*pi):
        blocks.fill(PURPUR_BLOCK, positions.add(setpos, pos(-1, height*3 + (Math.sin(i/setradius)*setradius-1), Math.cos(i/setradius)*setradius-1)), 
        positions.add(setpos, pos(1, height*3 + Math.sin(i/setradius)*setradius+1, Math.cos(i/setradius)*setradius+1)), FillOperation.REPLACE)




def createcircle(setradius, setpos):
    for i in range(2*setradius*pi):
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(Math.sin(i/setradius)*setradius-1, -height, Math.cos(i/setradius)*setradius-1)),  
                positions.add(setpos, pos(Math.sin(i/setradius)*setradius+1, height, Math.cos(i/setradius)*setradius+1)), FillOperation.REPLACE)
        blocks.fill(GRASS, positions.add(setpos, pos(0, height-2, 0)),  positions.add(setpos, pos(Math.sin(i/setradius)*(setradius-1), height-1, Math.cos(i/setradius)*(setradius-1))), FillOperation.REPLACE)
        blocks.place(CHERRY_LOG, positions.add(setpos, pos(Math.sin(i/setradius)*setradius, height+1, Math.cos(i/setradius)*setradius)))
        blocks.replace(CHERRY_LEAVES, AIR, positions.add(setpos, pos(Math.sin(i/setradius)*setradius-1, height-1, Math.cos(i/setradius)*setradius-1)),
                        positions.add(setpos, pos(Math.sin(i/setradius)*setradius+1, height+2, Math.cos(i/setradius)*setradius+1)))



def createstairs(setpos):
    for i in range(height):
        blocks.fill(AIR, positions.add(setpos, pos(i, i+1, -1)), positions.add(setpos, pos(i-1, i+height, 1)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(i, 0, -2)), positions.add(setpos, pos(i, i, 2)), FillOperation.REPLACE)
        blocks.replace(BLOCK_OF_QUARTZ, GRASS, positions.add(setpos, pos(i, 0, -2)), positions.add(setpos, pos(i, i, 2)))
        blocks.fill(QUARTZ_STAIRS, positions.add(setpos, pos(i, i, -1)), positions.add(setpos, pos(i, i, 1)), FillOperation.REPLACE)


def createpathway(setpos):
    blocks.replace(CHISELED_QUARTZ_BLOCK, GRASS, positions.add(setpos, pos(-radius, 0, -1)), positions.add(setpos, pos(radius, 0, 1)))
    blocks.replace(CHISELED_QUARTZ_BLOCK, GRASS, positions.add(setpos, pos(-1, 0, -radius)), positions.add(setpos, pos(1, 0, radius)))


def planttrees(setradius, setpos):
    for i in range(setradius):
        xpos = randint(-setradius, 0)
        zpos = randint(-setradius, setradius)
        blocks.replace(CHERRY_SAPLING, AIR, positions.add(setpos, pos(xpos, 0, zpos)), positions.add(setpos, pos(xpos, 0, zpos)))


player.on_chat("run", on_on_chat)


def on_chat():
    createcentralarch(player.position(), 10)
    
player.on_chat("jump", on_chat)
