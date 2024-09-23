width = 7
depth = 12
blockset = [RED_CONCRETE, ORANGE_CONCRETE, YELLOW_CONCRETE, LIME_CONCRETE, LIGHT_BLUE_CONCRETE, MAGENTA_CONCRETE]

def on_on_chat():
    startpos = positions.add(player.position(), pos(0, -3, 0))
    loops.pause(5000)
    blocks.fill(AIR, positions.add(startpos, pos(0, 0, 0)), positions.add(startpos, pos(width, 3, depth)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 2), positions.add(startpos, pos(0, 0, 0)), positions.add(startpos, pos(width, 0, depth)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 4), positions.add(startpos, pos(0, 0, -1)), positions.add(startpos, pos(width, 0, -1)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 0), positions.add(startpos, pos(0, 1, 0)), positions.add(startpos, pos(width, 1, depth)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(STICKY_PISTON, 1), positions.add(startpos, pos(0, 2, 0)), positions.add(startpos, pos(width, 2, depth)), FillOperation.REPLACE)
    for i in range(width+1):
        for j in range(depth+1):
            blocks.place(blockset[(i+j + depth)%blockset.length], positions.add(startpos, pos(i, 4, j)))
    blocks.fill(GRASS, positions.add(startpos, pos(-3, -1, -1)), positions.add(startpos, pos(-1, -1, -3)), FillOperation.REPLACE)
    for i in range(4):
        blocks.place(REDSTONE , positions.add(startpos, pos(-1-2*(i//2), 0, -1-2*(i%2))))
    blocks.place(blocks.block_with_data(REPEATER, 12), positions.add(startpos, pos(-1, 0, -2)))
    blocks.place(blocks.block_with_data(REPEATER, 14), positions.add(startpos, pos(-3, 0, -2)))
    blocks.place(blocks.block_with_data(REPEATER, 15), positions.add(startpos, pos(-2, 0, -3)))
    blocks.place(blocks.block_with_data(REPEATER, 13), positions.add(startpos, pos(-2, 0, -1)))
    blocks.place(REDSTONE_BLOCK, positions.add(startpos, pos(-4, 0, -1)))
    loops.pause(100)
    blocks.place(AIR, positions.add(startpos, pos(-4, 0, -1)))

player.on_chat("run", on_on_chat)

