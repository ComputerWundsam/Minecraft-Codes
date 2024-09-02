def on_travelled_fly():
    blocks.fill(AIR, pos(-15, -15, -15), pos(15, 15, 15))
player.on_travelled(TravelMethod.FALL, on_travelled_fly)
