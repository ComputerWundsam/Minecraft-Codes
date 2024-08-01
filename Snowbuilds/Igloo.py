pi = 3.14159265359
radius = 16
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos 
    startpos = player.position()
    loops.pause(5000)
    flatten()
    createigloo()

player.on_chat("run", on_on_chat)


def flatten():
    dradius = 2*radius
    for i in range(2*dradius*pi):
        blocks.fill(AIR, positions.add(startpos, pos(Math.sin(i/dradius)*dradius, 0, Math.cos(i/dradius)*dradius)), positions.add(startpos, pos(0, 20, 0)), FillOperation.REPLACE)
        blocks.fill(ICE, positions.add(startpos, pos(Math.sin(i/dradius)*dradius, -1, Math.cos(i/dradius)*dradius)), positions.add(startpos, pos(0, -2, 0)), FillOperation.REPLACE)

def createigloo():
    sradius = radius-2
    h = -1
    for j in range(radius*pi/2):
        diff = Math.cos(j/radius)
        if (h == Math.round(Math.sin(j/radius)*radius)):
            pass
        else:
            h += 1
            for i in range(2*(radius*diff)*pi):
                blocks.fill(SNOW, positions.add(startpos, pos(0, Math.sin(j/radius)*radius, 0)),
                    positions.add(startpos, pos(Math.sin(i/(radius*diff))*(radius*diff), Math.sin(j/radius)*radius+1, Math.cos(i/(radius*diff))*(radius*diff))), FillOperation.REPLACE)
#            for i in range(2*(sradius*diff)*pi):
#                blocks.fill(AIR, positions.add(startpos, pos(0, Math.sin(j/sradius)*sradius, 0)),
#                    positions.add(startpos, pos(Math.sin(i/(sradius*diff))*(sradius*diff), Math.sin(j/radius)*sradius, Math.cos(i/(sradius*diff))*(sradius*diff))), FillOperation.REPLACE)
    createentrance()

def createentrance():
    sradius = 8
    for i in range(sradius*pi):
        blocks.fill(SNOW, positions.add(startpos, pos(0, Math.sin(i/sradius)*sradius, radius-4)),
            positions.add(startpos, pos(Math.cos(i/sradius)*sradius, Math.sin(i/sradius)*sradius, radius+4)), FillOperation.REPLACE)
    sradius = sradius-2
    for i in range(sradius*pi+1):
        blocks.fill(AIR, positions.add(startpos, pos(0, Math.sin(i/sradius)*sradius, radius-4)),
            positions.add(startpos, pos(Math.cos(i/sradius)*sradius, Math.sin(i/sradius)*sradius, radius+4)), FillOperation.REPLACE)

