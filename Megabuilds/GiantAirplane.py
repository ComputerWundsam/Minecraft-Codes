pradius = 12
startpos = pos(0, 0, 0)
pi = 3.14159265359
nplength = 3
bplength = 3
plength = 70
planeblock = IRON_BLOCK
wingspan = 24
wingsegment = 3


def on_on_chat():
    global startpos
    startpos = player.position()
    createplanecenter()
    createwings(positions.add(startpos, pos(0, pradius-3, plength/2 + nplength*pradius )))
    createplanewindows()
    createdecoration()
player.on_chat("run", on_on_chat)


def createplanecenter():
    for k in range(pradius*2):
        i = k/2
        for j in range(i * pi):
            blocks.fill(planeblock, positions.add(startpos, pos(Math.sin(j/i)*i, Math.cos(j/i)*i + (i/2), nplength*i+nplength)), positions.add(startpos, pos(-Math.sin(j/i)*i, Math.cos(j/i)*i + (i/2), nplength*i)), FillOperation.REPLACE)
    setpos = positions.add(startpos, pos(0, pradius/2, (pradius+1) * nplength))
    for j in range(pradius * pi):
        blocks.fill(planeblock, positions.add(setpos, pos(Math.sin(j/pradius)*pradius, Math.cos(j/pradius)*pradius, 0)), positions.add(setpos, pos(-Math.sin(j/pradius)*pradius, Math.cos(j/pradius)*pradius, plength)), FillOperation.REPLACE)
    setpos = positions.add(setpos, pos(0, pradius , plength))
    for k in range(pradius*2):
            i = pradius - (k/2)
            for j in range(i * pi):
                blocks.fill(planeblock, positions.add(setpos, pos(Math.sin(j/i)*i, Math.cos(j/i)*i - i, bplength*(pradius-i)+bplength)), positions.add(setpos, pos(-Math.sin(j/i)*i, Math.cos(j/i)*i - i, bplength*(pradius-i))), FillOperation.REPLACE)

def createplanewindows():
    blocks.replace(GLASS, planeblock, positions.add(startpos, pos(-pradius, pradius/2, pradius)), positions.add(startpos, pos(pradius, pradius-1, pradius*nplength)))
    for i in range(plength/2):
        for j in range(pradius/5):
            blocks.replace(GLASS, planeblock, positions.add(startpos, pos(-pradius, pradius - 2 - 3*j, (pradius+1)*nplength + 2*i)), positions.add(startpos, pos(pradius, pradius-2 - 3*j, (pradius+1)*nplength + 2*i)))

def createwings(setpos):
    for i in range(wingspan):
        blocks.fill(planeblock, positions.add(setpos, pos(-pradius - wingsegment*i, 0, i)), positions.add(setpos, pos(pradius + wingsegment*i, 0, i)), FillOperation.REPLACE)
    createbackwings(positions.add(setpos, pos(0, pradius, plength/2 + bplength*pradius - wingspan/2)))

def createbackwings(setpos):
    for i in range(wingspan/2):
        blocks.fill(planeblock, positions.add(setpos, pos(-i-pradius, -pradius, i-pradius)), positions.add(setpos, pos( i+pradius, -pradius, i-pradius)), FillOperation.REPLACE)
        blocks.fill(planeblock, positions.add(setpos, pos(0, 0, i)), positions.add(setpos, pos(0, i, i)), FillOperation.REPLACE)

def createdecoration():
    for i in range(pradius/2):
        blocks.replace(REDSTONE_BLOCK, planeblock, positions.add(startpos, pos(-pradius, 2*pradius - 4 - 4*i, 0)), positions.add(startpos, pos(pradius, 2*pradius -4 - 4*i, plength + (bplength + nplength)*pradius)))
    blocks.replace(OCHRE_FROGLIGHT, planeblock, positions.add(startpos, pos(-pradius+2, pradius, 0)), positions.add(startpos, pos(pradius-2, pradius, plength + (bplength + nplength)*pradius)))
