stripeblocks = [EMERALD_BLOCK, LAPIS_LAZULI_BLOCK, REDSTONE_BLOCK, PURPUR_BLOCK, GOLD_BLOCK, BLOCK_OF_NETHERITE, DIAMOND_BLOCK]
glassblocks = [LIME_STAINED_GLASS, BLUE_STAINED_GLASS, RED_STAINED_GLASS, PURPLE_STAINED_GLASS, YELLOW_STAINED_GLASS, BLACK_STAINED_GLASS, BLUE_STAINED_GLASS]

pi = 3.14159265359
radius = 8
depth = 40
turbinesize = 6
linecount = 4
backruddersize = 18
stripeblock = EMERALD_BLOCK
glassblock = LIME_STAINED_GLASS

def on_on_chat():
    global glassblock, stripeblock
    blockindex = randint(0, stripeblocks.length-1)
    stripeblock = stripeblocks[blockindex]
    glassblock = glassblocks[blockindex]
    startpos = player.position()
    for j in range(radius+1):
        setradius = (radius+1) - j
        for i in range(pi*setradius+j):
            blocks.fill(IRON_BLOCK, positions.add(startpos, pos(i+2*j, -Math.sin(j/(radius))*radius, Math.sin(i/(2*setradius))*setradius)), 
                                    positions.add(startpos, pos(i+2*j, Math.sin(j/(radius))*radius, -Math.sin(i/(2*setradius))*setradius)))    
    createsides(positions.add(startpos, pos(2*radius+1, 0, 0)))
    blocks.replace(glassblock, IRON_BLOCK, positions.add(startpos,pos(radius/2, 2, -radius)), positions.add(startpos,pos(2*radius, 2+radius/2, radius)))
    createbackrudder(positions.add(startpos, pos(2*radius+depth+1, 0, 0)))
    createstripes(positions.add(startpos, pos(radius, 0, 0)))
    createturbines(positions.add(startpos, pos(3*radius, -1, 0)))
    createturbines(positions.add(startpos, pos(radius+depth, -1, 0)))

def createbackrudder(setpos):
    for i in range(backruddersize-radius):
        blocks.fill(stripeblock, positions.add(setpos, pos(-i, backruddersize-i, 0)), positions.add(setpos, pos(-i, 0, 0)), FillOperation.REPLACE)
        blocks.fill(stripeblock, positions.add(setpos, pos(-i, 0, backruddersize-i)), positions.add(setpos,pos(-i, 0, -backruddersize+i)), FillOperation.REPLACE)

def createstripes(startpos):
    for i in range(2*radius+depth/linecount):
        blocks.replace(stripeblock, IRON_BLOCK, positions.add(startpos,pos(i*linecount, -radius, -radius)), positions.add(startpos, pos(i*linecount, radius, radius)))
        blocks.replace(glassblock, IRON_BLOCK, positions.add(startpos,pos(i*linecount+2, -radius/4, -radius)), positions.add(startpos, pos(i*linecount+2, radius/4, radius)))
        blocks.replace(glassblock, IRON_BLOCK, positions.add(startpos,pos(i*linecount+2, -radius, -radius/4)), positions.add(startpos, pos(i*linecount+2, radius, radius/4)))
    blocks.replace(OCHRE_FROGLIGHT, IRON_BLOCK, positions.add(startpos,pos(0, -radius, 0)), positions.add(startpos, pos(depth, radius, 0)))
    blocks.replace(OCHRE_FROGLIGHT, IRON_BLOCK, positions.add(startpos,pos(0, 0, -radius)), positions.add(startpos, pos(depth, 0, radius)))

def createsides(setpos):
    sradius = radius-1
    for i in range(sradius*pi):
        blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, Math.sin(i/sradius)*sradius, Math.cos(i/sradius)*sradius)), positions.add(setpos, pos(depth, -Math.sin(i/sradius)*sradius, -Math.cos(i/sradius)*sradius)))
    sradius = radius-3
    for i in range(sradius*pi):
        blocks.fill(MAGMA_BLOCK, positions.add(setpos, pos(depth-2, Math.sin(i/sradius)*sradius, Math.cos(i/sradius)*sradius)), positions.add(setpos, pos(depth+1, -Math.sin(i/sradius)*sradius, -Math.cos(i/sradius)*sradius)))


def createturbines(setpos):
    for j in range(radius*2):
        value = (2*j*pi)/3
        if(j%3 != 0):
            blocks.fill(IRON_BLOCK, positions.add(setpos, pos(1, Math.cos(value)*j-1, Math.sin(value)*j-1)), positions.add(setpos, pos(5, Math.cos(value)*j+1, Math.sin(value)*j+1)), FillOperation.REPLACE)
    for i in range(2):
        singleturbine(positions.add(setpos, pos(3, Math.cos(2*pi/3 * (i+1))*radius*2, Math.sin(2*pi/3 * (i+1))*radius*2)))

def singleturbine(setpos):
    for i in range(2*turbinesize*pi):
            blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 0, 0)),
                                    positions.add(setpos, pos(8, Math.cos(i/turbinesize)*turbinesize, Math.sin(i/turbinesize)*turbinesize)), FillOperation.REPLACE)
    for i in range(2*(turbinesize-2)*pi):
            blocks.fill(MAGMA_BLOCK, positions.add(setpos, pos(1, 0, 0)),
                                    positions.add(setpos, pos(9, Math.cos(i/(turbinesize-2))*(turbinesize-2), Math.sin(i/(turbinesize-2))*(turbinesize-2))), FillOperation.REPLACE)


player.on_chat("run", on_on_chat)

def on_chat():
    createturbines(player.position())
player.on_chat("jump", on_chat)
