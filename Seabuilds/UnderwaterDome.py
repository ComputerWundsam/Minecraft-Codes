radius = 30
pi = 3.14159265359
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createdome()
    createground()
    creategates()


def createdome():
    sradius = radius-2
    h = -1
    for j in range(radius*pi/2):
        diff = Math.cos(j/radius)
        if (h == Math.round(Math.sin(j/radius)*radius)):
            pass
        else:
            h += 1
            for i in range(2*radius*pi):
                blocks.fill(GLASS, positions.add(startpos, pos(0, Math.sin(j/radius)*radius, 0)),
                    positions.add(startpos, pos(Math.sin(i/(radius*diff))*(radius*diff), Math.sin(j/radius)*radius+1, Math.cos(i/(radius*diff))*(radius*diff))), FillOperation.REPLACE)
            for i in range(2*sradius*pi):
                blocks.fill(AIR, positions.add(startpos, pos(0, Math.sin(j/sradius)*sradius, 0)),
                    positions.add(startpos, pos(Math.sin(i/(sradius*diff))*(sradius*diff), Math.sin(j/sradius)*sradius-1, Math.cos(i/(sradius*diff))*(sradius*diff))), FillOperation.REPLACE)
    

def createground():
    shapes.circle(GRASS, positions.add(startpos, pos(0, -1, 0)), radius-1, Axis.X, ShapeOperation.REPLACE)
    for j in range(5):
        for i in range(2*radius*pi):
            setradius = radius - (radius*i/5)
            blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, 
                pos(Math.sin(setradius)*setradius, -1, Math.cos(setradius)*setradius)))


def creategates():
    for i in range(2):
        v = -1+2*i
        blocks.fill(GLASS, positions.add(startpos, pos(v*(radius-4), -1, -2)), positions.add(startpos, pos(v*(radius+6), 4, 2)), FillOperation.REPLACE)
        blocks.fill(AIR, positions.add(startpos, pos(v*(radius-4), 0, -1)), positions.add(startpos, pos(v*(radius+5), 3, 1)), FillOperation.REPLACE)
        blocks.fill(OCHRE_FROGLIGHT, positions.add(startpos, pos(v*(radius-2), 4, 0)), positions.add(startpos, pos(v*(radius+6), 4, 0)), FillOperation.REPLACE)
        blocks.place(IRON_DOOR, positions.add(startpos, pos(v*(radius+6), 0, 0)))
        blocks.place(WEIGHTED_PRESSURE_PLATE_LIGHT, positions.add(startpos, pos(v*(radius+7), 0, 0)))
        blocks.place(WEIGHTED_PRESSURE_PLATE_LIGHT, positions.add(startpos, pos(v*(radius+5), 0, 0)))

player.on_chat("run", on_on_chat)

def on_chat():
    creategates()
player.on_chat("jump", on_chat)
