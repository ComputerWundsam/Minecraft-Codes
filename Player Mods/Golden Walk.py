def on_travelled_walk():
    blocks.fill(GOLD_BLOCK, pos(5, -1, 5), pos(-5, -1, -5))
player.on_travelled(WALK, on_travelled_walk)
