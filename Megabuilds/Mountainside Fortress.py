radius = 20
depth = 15
jobblocks = [BARREL, BLAST_FURNACE, BREWING_STAND, CARTOGRAPHY_TABLE, CAULDRON, COMPOSTER, FLETCHING_TABLE, STONECUTTER_BLOCK, LOOM, SMITHING_TABLE, SMOKER]
startpos = pos(0, 0, 0)


def createcavefortress():
    global startpos
    startpos = player.position()
    loops.pause(8000)
    blocks.fill(AIR, positions.add(startpos, pos(-10, -radius, -radius)), positions.add(startpos, pos(0, radius, radius)))
    shapes.circle(GLASS, startpos, radius, Axis.X, ShapeOperation.REPLACE)
    startpos = positions.add(startpos, pos(1, 0, 0))
    for i in range(depth):
        crosscircle(startpos, i)
    shapes.circle(IRON_BLOCK, positions.add(startpos, pos(depth, 0, 0)), radius, Axis.X, ShapeOperation.REPLACE)
    shapes.circle(OCHRE_FROGLIGHT, positions.add(startpos, pos(depth, 0, 0)), radius-2, Axis.X, ShapeOperation.OUTLINE)
    createstairs()
    createfarm()
    furniture()
    createexit(positions.add(startpos, pos(-2, -radius+1, 0)))



def createstairs():
    for i in range(radius):
        blocks.fill(AIR, positions.add(startpos, pos(depth-1, -i, -radius+2+i)), positions.add(startpos, pos(depth-3, -i+4, -radius+2+i)))
        blocks.fill(IRON_BLOCK, positions.add(startpos, pos(depth-1, -i, -radius+2+i)), positions.add(startpos, pos(depth-3, -i, -radius+2+i)))
    player.say(2)

def createfarm():
    blocks.fill(GRASS, positions.add(startpos, pos(3, 1, -1)), positions.add(startpos, pos(depth-1, 1, -radius+8)))
    blocks.fill(DARK_OAK_FENCE, positions.add(startpos, pos(3, 2, -1)), positions.add(startpos, pos(depth-1, 2, -radius+9)))
    blocks.fill(AIR, positions.add(startpos, pos(4, 2, -1)), positions.add(startpos, pos(depth-1, 2, -radius+10)))
    blocks.replace(DARK_OAK_FENCE_GATE, DARK_OAK_FENCE, positions.add(startpos, pos(5, 2, -radius+9)), positions.add(startpos, pos(5, 2, -radius+9)))
    for i in range(depth):
        mobs.spawn(CHICKEN, positions.add(startpos, pos(5, 2, -radius+12)))


def furniture():
    counter = 0
    blocks.fill(AIR, positions.add(startpos, pos(0, 1, 0)), positions.add(startpos, pos(2, 3, 0)))
    blocks.fill(AIR, positions.add(startpos, pos(0, -radius+2, 0)), positions.add(startpos, pos(2, -radius+4, 0)))
    for i in range(depth-1):
        for j in range(radius/4-1):
            blocks.place(BED, positions.add(startpos, pos(depth-1-i, 1, radius-2-4*j)))
            blocks.place(jobblocks[randint(0, jobblocks.length-1)], positions.add(startpos, pos(depth-1-i, 1, radius-4-4*j)))
            mobs.spawn(VILLAGER, positions.add(startpos, pos(depth-1-i, 1, radius-2-4*j)))
        player.execute("summon iron_golem " + positions.add(startpos, pos(depth-1-i, -4, 2)))
    for i in range(radius-3):   
        while(blocks.test_for_block(AIR, positions.add(startpos, pos(1, -radius+2+i, -2-counter)))):
            blocks.replace(CHEST, AIR, positions.add(startpos, pos(1, -radius+2+i, -2-counter)), positions.add(startpos, pos(depth, -radius+2+i, -2-counter)))
            counter += 1

def createexit(setpos):
    counter = 0
    blocks.place(DARK_OAK_DOOR, positions.add(setpos, pos(1, 1, 2)))
    while(blocks.test_for_block(AIR, positions.add(setpos, pos(-counter, -counter, 0)))):
        player.say(blocks.test_for_block(AIR, positions.add(setpos, pos(-counter, -counter, 0))))
        blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-counter, -counter, -3)), positions.add(setpos, pos(-counter, -counter, 3)))
        counter += 1

def crosscircle(startpos, i):
    shapes.circle(IRON_BLOCK, positions.add(startpos, pos(i, 0, 0)), radius, Axis.X, ShapeOperation.REPLACE)
    shapes.circle(AIR, positions.add(startpos, pos(i, 0, 0)), radius-1, Axis.X, ShapeOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(startpos, pos(i, -radius, 0)), positions.add(startpos, pos(i, radius, 0)))
    blocks.fill(IRON_BLOCK, positions.add(startpos, pos(i, 0, -radius)), positions.add(startpos, pos(i, 0, radius)))
    if(i%5 == 4):
        blocks.fill(OCHRE_FROGLIGHT, positions.add(startpos, pos(i, -radius/2, 0)), positions.add(startpos, pos(i, radius/2, 0)))
        blocks.fill(OCHRE_FROGLIGHT, positions.add(startpos, pos(i, 0, -radius/2)), positions.add(startpos, pos(i, 0, radius/2)))

player.on_chat("run", createcavefortress)
