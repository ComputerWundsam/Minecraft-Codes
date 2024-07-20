pi = 3.14159265359
radius = 8
maxradius = 30
woolblocks = [RED_WOOL, ORANGE_WOOL, YELLOW_WOOL, LIME_WOOL, LIGHT_BLUE_WOOL, MAGENTA_WOOL, PINK_WOOL]
startpos = pos(0, 0, 0)
balloonsummit = []
cheight = 20
counter = 0
fence = DARK_OAK_FENCE


def on_on_chat():
    global startpos
    startpos = player.position()
    createbasket()
    createballoon()

def createbasket():
    blocks.fill(PLANKS_DARK_OAK, positions.add(startpos, pos(-3, -2, -3)), positions.add(startpos, pos(3, -1, 3)), FillOperation.HOLLOW)
    blocks.fill(fence, positions.add(startpos, pos(-3, 0, -3)), positions.add(startpos, pos(3, 0, 3)), FillOperation.OUTLINE)
    for i in range(2):
        blocks.fill(fence, positions.add(startpos, pos(0, 0, -3+6*i)), positions.add(startpos, pos(0, radius, -3+6*i)), FillOperation.OUTLINE)
        blocks.fill(fence, positions.add(startpos, pos(-3+6*i, 0, 0)), positions.add(startpos, pos(-3+6*i, radius, 0)), FillOperation.OUTLINE)
    blocks.fill(fence, positions.add(startpos, pos(-radius-1, radius-1, 0)), positions.add(startpos, pos(radius+1, radius-1, 0)), FillOperation.OUTLINE)
    blocks.fill(fence, positions.add(startpos, pos(0, radius-1, -radius-1)), positions.add(startpos, pos(0, radius-1, radius+1)), FillOperation.OUTLINE)

    blocks.fill(AIR, positions.add(startpos, pos(-2, -1, -2)), positions.add(startpos, pos(2, 0, 2)), FillOperation.OUTLINE)

def createballoon():
    global radius, startpos, counter
    while radius < maxradius:
        shapes.circle(woolblocks[(counter//4)%woolblocks.length], positions.add(startpos, pos(0, radius, 0)), radius, Axis.Y, ShapeOperation.REPLACE)
        blocks.replace(fence, AIR, positions.add(startpos, pos(-radius-2, radius, 0)), positions.add(startpos, pos(radius+2, radius, 0)))
        blocks.replace(fence, AIR, positions.add(startpos, pos(0, radius, -radius-2)), positions.add(startpos, pos(0, radius, radius+2)))
        radius += 1
        counter += 1
    startpos = positions.add(startpos, pos(0, radius, 0))
    for i in range(2*radius*pi):
        blocks.fill(WOOL, startpos, positions.add(startpos, pos(Math.sin(i/radius)*radius, cheight, Math.cos(i/radius)*radius)))
    for i in range(2):
        blocks.replace(fence, AIR, positions.add(startpos, pos(-radius-1, 0, 0)), positions.add(startpos, pos(radius+1, cheight, 0)))
        blocks.replace(fence, AIR, positions.add(startpos, pos(0, 0, -radius-1)), positions.add(startpos, pos(0, cheight, radius+1)))
    for i in range(cheight+1):
        blocks.replace(woolblocks[(counter//4)%woolblocks.length], WOOL, positions.add(startpos, pos(-radius, i, -radius)), positions.add(startpos, pos(radius, i, radius)))
        counter += 1
    startpos = positions.add(startpos, pos(0, cheight+1, 0))
    blocks.fill(fence, positions.add(startpos,pos(-radius-1, 0, 0)), positions.add(startpos,pos(radius+1, 0, 0)), FillOperation.REPLACE)
    blocks.fill(fence, positions.add(startpos, pos(0, 0, -radius-1)), positions.add(startpos,pos(0, 0, radius+1)), FillOperation.REPLACE)
    for i in range(radius/2):
        shapes.circle(woolblocks[(counter//4)%woolblocks.length], positions.add(startpos, pos(0, i, 0)), Math.cos((2*i)/radius)*radius, Axis.Y, ShapeOperation.REPLACE)
        blocks.fill(fence, positions.add(startpos,pos(-(Math.cos((2*i)/radius)*radius)-1, i+1, 0)), positions.add(startpos,pos(Math.cos((2*i)/radius)*radius+1, i+1, 0)), FillOperation.REPLACE)
        blocks.fill(fence, positions.add(startpos, pos(0, i+1, -(Math.cos((2*i)/radius)*radius)-1)), positions.add(startpos,pos(0, i+1, Math.cos((2*i)/radius)*radius+1)), FillOperation.REPLACE)
        counter += 1


player.on_chat("run", on_on_chat)
