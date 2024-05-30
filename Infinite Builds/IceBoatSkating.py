def on_on_chat():
    startpos = positions.add(player.position(), pos(0, -1, -7))
    blocks.fill(ICE, startpos, positions.add(startpos, pos(20, 0, 20)))
    startpos = positions.add(startpos, pos(-15, 0, randint(-2, 2)))
    while True:
        blocks.fill(AIR, startpos, positions.add(startpos, pos(20, 6, 20)))
        blocks.fill(ICE, startpos, positions.add(startpos, pos(20, 0, 20)))
        startpos = positions.add(startpos, pos(3, 0, randint(-2, 2)))
player.on_chat("run", on_on_chat)
