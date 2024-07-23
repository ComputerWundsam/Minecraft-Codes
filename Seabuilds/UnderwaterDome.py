radius = 30
pi = 3.14159265359
startpos = pos(0, 0, 0)

def oceandome():
    global startpos
    startpos = player.position()
    flatten()
    createground()
    createdome()
    creategates()
    createhouses()

def flatten():
    for i in range(radius/3):
        for j in range(9):
            blocks.fill(WATER, positions.add(startpos, pos(-radius*3/2 + radius*(j//3), 0+3*i, -radius*3/2 + radius*(j%3))), positions.add(startpos, pos(-radius*3/2 + radius + radius*(j//3), 2+3*i, -radius*3/2 + radius + radius*(j%3))))

def createdome():
    sradius = radius-2
    h = -1
    for j in range(radius*pi/2):
        diff = Math.cos(j/radius)
        if (h == Math.round(Math.sin(j/radius)*radius)):
            pass
        else:
            h += 1
            for i in range(2*(radius*diff)*pi):
                blocks.fill(WHITE_STAINED_GLASS, positions.add(startpos, pos(0, Math.sin(j/radius)*radius, 0)),
                    positions.add(startpos, pos(Math.sin(i/(radius*diff))*(radius*diff), Math.sin(j/radius)*radius+1, Math.cos(i/(radius*diff))*(radius*diff))), FillOperation.REPLACE)
            for i in range(2*(sradius*diff)*pi):
                blocks.fill(AIR, positions.add(startpos, pos(0, Math.sin(j/sradius)*sradius, 0)),
                    positions.add(startpos, pos(Math.sin(i/(sradius*diff))*(sradius*diff), Math.sin(j/radius)*sradius, Math.cos(i/(sradius*diff))*(sradius*diff))), FillOperation.REPLACE)
    

def createground():
    shapes.circle(BLOCK_OF_NETHERITE, positions.add(startpos, pos(0, -1, 0)), radius-1, Axis.Y, ShapeOperation.REPLACE)
    for j in range(5):
        setradius = radius - (radius*((j+1)/5))
        for i in range(2*setradius*pi):
            blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, 
                pos(Math.sin(i/setradius)*setradius, -1, Math.cos(i/setradius)*setradius)))
    blocks.replace(OCHRE_FROGLIGHT, BLOCK_OF_NETHERITE, positions.add(startpos, pos(-radius, -1, -1)),positions.add(startpos,  pos(radius, -1, 1)))
    blocks.replace(OCHRE_FROGLIGHT, BLOCK_OF_NETHERITE, positions.add(startpos, pos(-1, -1, -radius)),positions.add(startpos,  pos(1, -1, radius)))

def creategates():
    for i in range(2):
        v = -1+2*i
        blocks.fill(GLASS, positions.add(startpos, pos(v*(radius-4), -1, -2)), positions.add(startpos, pos(v*(radius+6), 4, 2)), FillOperation.REPLACE)
        blocks.fill(AIR, positions.add(startpos, pos(v*(radius-4), 0, -1)), positions.add(startpos, pos(v*(radius+5), 3, 1)), FillOperation.REPLACE)
        blocks.fill(OCHRE_FROGLIGHT, positions.add(startpos, pos(v*(radius-2), 4, 0)), positions.add(startpos, pos(v*(radius+6), 4, 0)), FillOperation.REPLACE)
        blocks.place(IRON_DOOR, positions.add(startpos, pos(v*(radius+6), 0, 0)))
        blocks.place(WEIGHTED_PRESSURE_PLATE_LIGHT, positions.add(startpos, pos(v*(radius+7), 0, 0)))
        blocks.place(WEIGHTED_PRESSURE_PLATE_LIGHT, positions.add(startpos, pos(v*(radius+5), 0, 0)))

def createhouses():
    blocks.fill(IRON_BLOCK, positions.add(startpos, pos(2, 0, 2)), positions.add(startpos, pos(radius/2, radius*3/5-1, radius/2)), FillOperation.REPLACE)
    for i in range(radius*(3/10)):
        blocks.replace(GLASS, IRON_BLOCK, positions.add(startpos, pos(2+1, 2+i*2, 2)), positions.add(startpos, pos(radius/2-1, 2+i*2, radius/2)))
        blocks.replace(GLASS, IRON_BLOCK, positions.add(startpos, pos(2, 2+i*2, 2+1)), positions.add(startpos, pos(radius/2, 2+i*2, radius/2-1)))
    hydroponicgarden()
    researchlab()
    geolab()

def hydroponicgarden():
    blocks.fill(EMERALD_BLOCK, positions.add(startpos, pos(-3, 0, 3)), positions.add(startpos, pos(-radius/2, radius*3/5-1, radius/2)), FillOperation.REPLACE)
    for i in range(radius*(1/5)-1):
        blocks.replace(CHERRY_LOG, EMERALD_BLOCK, positions.add(startpos, pos(-4, 3+i*3, 2)), positions.add(startpos, pos(-(radius/2-1), 3+i*3, radius/2)))
        blocks.replace(CHERRY_LOG, EMERALD_BLOCK, positions.add(startpos, pos(-3, 3+i*3, 3)), positions.add(startpos, pos(-radius/2, 3+i*3, radius/2-1)))
        blocks.replace(GLASS, EMERALD_BLOCK, positions.add(startpos, pos(-4, 2+i*3, 3)), positions.add(startpos, pos(-(radius/2-1), 3+i*3, radius/2)))
        blocks.replace(GLASS, EMERALD_BLOCK, positions.add(startpos, pos(-3, 2+i*3, 4)), positions.add(startpos, pos(-radius/2, 3+i*3, radius/2-1)))
        blocks.replace(CHERRY_LEAVES, AIR, positions.add(startpos, pos(-2, 3+i*3, 2)), positions.add(startpos, pos(-radius/2-1, 3+i*3, radius/2+1)))

def researchlab():
    blocks.fill(LAPIS_LAZULI_BLOCK, positions.add(startpos, pos(-2, 0, -2)), positions.add(startpos, pos(-radius/2, radius*3/5-1, -radius/2)), FillOperation.REPLACE)
    for i in range(radius*(3/10)):
        blocks.replace(GLASS, LAPIS_LAZULI_BLOCK, positions.add(startpos, pos(-2-1, 2+i*2, -2)), positions.add(startpos, pos(-radius/2+1, 2+i*2, -radius/2)))
        blocks.replace(GLASS, LAPIS_LAZULI_BLOCK, positions.add(startpos, pos(-2, 2+i*2, -2-1)), positions.add(startpos, pos(-radius/2, 2+i*2, -radius/2+1)))
    blocks.fill(VERDANT_FROGLIGHT, positions.add(startpos, pos(-3, 0, -3)), positions.add(startpos, pos(-radius/2+1, radius*3/5-2, -radius/2+1)), FillOperation.REPLACE)

def geolab():
    blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(2, 0, -2)), positions.add(startpos, pos(radius/2, radius*3/5-1, -radius/2)), FillOperation.REPLACE)
    for i in range(radius*(3/10)):
        blocks.replace(GLASS, BLOCK_OF_NETHERITE, positions.add(startpos, pos(3, 2+i*2, -2)), positions.add(startpos, pos(radius/2-1, 2+i*2, -radius/2)))
        blocks.replace(GLASS, BLOCK_OF_NETHERITE, positions.add(startpos, pos(2, 2+i*2, -2-1)), positions.add(startpos, pos(radius/2, 2+i*2, -radius/2+1)))
    blocks.fill(MAGMA_BLOCK, positions.add(startpos, pos(3, 0, -3)), positions.add(startpos, pos(radius/2-1, radius*3/5-2, -radius/2+1)), FillOperation.REPLACE)


player.on_chat("run", oceandome)

