width = 5
depth = 10
height = 3
startpos = pos(0, 0, 0)
maxvalue = 15
plankblock = CHERRY_PLANKS
logblock = CHERRY_LOG
fenceblock = CHERRY_FENCE
doorblock = BIRCH_DOOR
slabblock = CHERRY_SLAB
windowblock = GLASS

def createplatform():
    global width, depth, startpos
    width = randint(5, maxvalue)
    depth = randint(5, maxvalue)
    startpos = player.position()
    loops.pause(5000)
    for i in range(4):
        player.execute("fill " + positions.add(startpos, pos(-width + 2*width * (i%2) - 1, -100, -depth + 2 * depth * (i//2)-1)) + " " +
            positions.add(startpos, pos(-width + 2*width * (i%2)+1, 0, -depth + 2 * depth * (i//2)+1)) + " cherry_log replace water")
        player.execute("fill " + positions.add(startpos, pos(-width + 2*width * (i%2)-1, -100, -depth + 2 * depth * (i//2)-1)) + " " +
            positions.add(startpos, pos(-width + 2*width * (i%2)+1, 0, -depth + 2 * depth * (i//2)+1)) + " cherry_log replace air")
    blocks.fill(plankblock, positions.add(startpos, pos(-width-1, 1, -depth-1)), positions.add(startpos, pos(width+1, 1, (depth+1))), FillOperation.REPLACE)
    blocks.fill(fenceblock, positions.add(startpos, pos(-width-1, 2, -depth-1)), positions.add(startpos, pos(width+1, 2, (depth+1))), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-width, 2, -depth)), positions.add(startpos, pos(width, 2, depth)), FillOperation.REPLACE)
    createhouse()


def createhouse():
    swidth = width-2
    sdepth = depth - 2
    height = randint(6, 10)
    blocks.fill(plankblock, positions.add(startpos, pos(-swidth, 1, -sdepth)), positions.add(startpos, pos(swidth, height, sdepth)), FillOperation.HOLLOW)
    for i in range(4):
        blocks.fill(logblock, positions.add(startpos, pos(-swidth + 2*swidth * (i%2), 1, -sdepth + 2 * sdepth * (i//2))), positions.add(startpos, pos(-swidth + 2*swidth * (i%2), height, -sdepth + 2 * sdepth * (i//2))), FillOperation.REPLACE)
    for i in range((min(swidth, sdepth))+2):
        if i% 2 == 0:
            setblock = slabblock
        else:
            setblock = plankblock
        blocks.fill(setblock, positions.add(startpos, pos(-swidth-2+i, height + i//2, -sdepth-2+i)), positions.add(startpos, pos(swidth+2-i, height + i//2, sdepth+2-i)), FillOperation.REPLACE)
    for i in range(height/4):
        for j in range(sdepth/2):
            blocks.replace(windowblock, plankblock, positions.add(startpos, pos(-swidth, 3+3*i, -sdepth+2+4*j)), positions.add(startpos, pos(swidth, 3+3*i, -sdepth+2+4*j)))
        for j in range(swidth/2):
            blocks.replace(windowblock, plankblock, positions.add(startpos, pos(-swidth+2+4*j, 3+3*i, -sdepth)), positions.add(startpos, pos(-swidth+2+4*j, 3+3*i, sdepth)))
    blocks.replace(doorblock, plankblock, positions.add(startpos, pos(-swidth, 2, 0)), positions.add(startpos, pos(swidth, 2, 0)))
    blocks.replace(doorblock, plankblock, positions.add(startpos, pos(0, 2, -sdepth)), positions.add(startpos, pos(0, 2, sdepth)))


def createbridge():
    x = randint (maxvalue, width+maxvalue)
    z = randint (maxvalue, maxvalue+depth)
    if (Math.random() < 0.5):
        x = x * -1
    if (Math.random() < 0.5):
        z = z * -1
    newpos = positions.add(startpos, pos(x, 0, z))
    

player.on_chat("run", createplatform)
