def on_on_chat():
    startpos = player.position()
    while True:
        blocks.fill(AIR, startpos, positions.add(startpos, pos(5, 5, 5)), FillOperation.REPLACE)
        startpos = positions.add(startpos, pos(-1, -1, -1))
player.on_chat("dig", on_on_chat)
