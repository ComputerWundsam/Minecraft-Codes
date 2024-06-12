def on_travelled_fly():
    blocks.fill(AIR, pos(-10, -2, -10), pos(10, 18, 10), FillOperation.REPLACE)
player.on_travelled(FLY, on_travelled_fly)
