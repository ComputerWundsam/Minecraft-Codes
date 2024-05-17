def on_travelled_fall():
    blocks.fill(AIR, pos(-5, -20, -5), pos(5, 5, 5))
player.on_travelled(FALL, on_travelled_fall)
