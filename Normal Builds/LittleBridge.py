def on_on_chat():
    startpos = positions.add(player.position(), pos(0, -1, 0))
    counter = 0
    loops.pause(5000)
    while (blocks.test_for_block(AIR, startpos)):
        blocks.fill(MANGROVE_PLANKS, startpos, positions.add(startpos, pos(6, 0, 0)))
        blocks.place(MANGROVE_FENCE, positions.add(startpos, pos(0, 1, 0)))
        blocks.place(MANGROVE_FENCE, positions.add(startpos, pos(6, 1, 0)))
        if(counter % 8 == 0):
            blocks.fill(MANGROVE_FENCE, positions.add(startpos, pos(0, 2, 0)), positions.add(startpos, pos(0, 5, 0)))
            blocks.fill(MANGROVE_FENCE, positions.add(startpos, pos(6, 2, 0)), positions.add(startpos, pos(6, 5, 0)))
            blocks.place(TORCH, positions.add(startpos, pos(0, 6, 0)))
            blocks.place(TORCH, positions.add(startpos, pos(6, 6, 0)))
        counter += 1
        startpos = positions.add(startpos, pos(0, 0, -1))
    startpos = positions.add(startpos, pos(0, 0, 1))
    blocks.fill(MANGROVE_FENCE, positions.add(startpos, pos(0, 2, 0)), positions.add(startpos, pos(0, 5, 0)))
    blocks.fill(MANGROVE_FENCE, positions.add(startpos, pos(6, 2, 0)), positions.add(startpos, pos(6, 5, 0)))
    blocks.place(TORCH, positions.add(startpos, pos(0, 6, 0)))
    blocks.place(TORCH, positions.add(startpos, pos(6, 6, 0)))
player.on_chat("run", on_on_chat)
