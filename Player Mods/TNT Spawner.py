def on_on_chat():
    while True:
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
player.on_chat("run", on_on_chat)
