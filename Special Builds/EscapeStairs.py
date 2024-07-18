def on_on_chat():
    startpos = positions.add(player.position(), pos(-1, 0, 0))
    while not blocks.test_for_block(AIR, startpos):
        blocks.fill(AIR, positions.add(startpos, pos(0, -1, 0)), positions.add(startpos, pos(0, 8, -6)))
        blocks.fill(GOLD_BLOCK, startpos, positions.add(startpos, pos(0, 0, -6)))
        blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, pos(0, 6, -3)))
        startpos = positions.add(startpos, pos(-1, 1, 0))
player.on_chat("run", on_on_chat)
