def on_on_chat():
    startpos = player.position()
    while(blocks.test_for_block(WATER, startpos)):
        counter = 0
        while(blocks.test_for_block(WATER, positions.add(startpos, pos(0, counter, 0)))):
            counter -= 1
        blocks.fill(GLASS, positions.add(startpos, pos(1, 0, 1)), positions.add(startpos, pos(5, counter, 0)))
        blocks.fill(GLASS, startpos, positions.add(startpos, pos(5, counter, 0)))
        blocks.fill(AIR, positions.add(startpos, pos(1, 0, 0)), positions.add(startpos, pos(4, counter+1, 0)))
        startpos = positions.add(startpos, pos(0, 0, 1))
player.on_chat("run", on_on_chat)
