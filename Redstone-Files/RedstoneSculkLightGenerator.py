length = 20

def on_on_chat():
    startpos = player.position()
    for i in range(2):
        blocks.fill(REDSTONE_BLOCK, positions.add(startpos, pos(length, -1, length*i)), positions.add(startpos, pos(0, -1, length*i)), FillOperation.REPLACE)
        blocks.fill(REDSTONE_BLOCK, positions.add(startpos, pos(length*i, -1, length)), positions.add(startpos, pos(length*i, -1, 0)), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(POWERED_RAIL, 0), positions.add(startpos, pos(length, 0, length*i)), positions.add(startpos, pos(0, 0, length*i)), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(POWERED_RAIL, 1), positions.add(startpos, pos(length*i, 0, length)), positions.add(startpos, pos(length*i, 0, 0)), FillOperation.REPLACE)
    for i in range(4):
        blocks.place(RAIL, positions.add(startpos, pos(length*(i//2), 0, length*(i%2))))
    for i in range(4):
        blocks.place(GRASS, positions.add(startpos, pos(0, 2+i, 6-i)))
        blocks.place(RAIL, positions.add(startpos, pos(0, 3+i, 6-i)))
    for i in range(length/5):
        player.execute("summon minecart " + positions.add(startpos, pos(0, 6, 4)))
        loops.pause(1200)
    blocks.fill(AIR, positions.add(startpos, pos(0, 6, 3)), positions.add(startpos, pos(0, 2, 6)), FillOperation.REPLACE)
    player.execute("fill " + positions.add(startpos, pos(-2, 1, -2)) + " " + positions.add(startpos, pos(length+2, 1, length+2)) + " sculk_sensor")
    for i in range(3):
        blocks.replace(REDSTONE_LAMP, AIR, positions.add(startpos, pos(-3, i, -3)), positions.add(startpos, pos(length+3, i, length+3)))
player.on_chat("run", on_on_chat)
