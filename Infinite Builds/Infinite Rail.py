def on_on_chat():
    startpos = player.position()
    while True:
        if(not blocks.test_for_block(AIR, startpos)):
            startpos = positions.add(startpos, pos(0, 1, 0))
        if(blocks.test_for_block(AIR, positions.add(startpos, pos(0, -1, 0)))):
            startpos = positions.add(startpos, pos(0, -1, 0))
            blocks.place(AIR, positions.add(startpos, pos(1, 0, 0)))
        blocks.fill(AIR, startpos, positions.add(startpos, pos(0, 4, 0)))
        blocks.place(REDSTONE_BLOCK, startpos)
        blocks.place(POWERED_RAIL, positions.add(startpos, pos(0, 1, 0)))
        startpos = positions.add(startpos, pos(1, 0, 0))
player.on_chat("run", on_on_chat)
