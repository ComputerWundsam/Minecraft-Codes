carpets = [RED_CARPET, ORANGE_CARPET, YELLOW_CARPET, LIME_CARPET, LIGHT_BLUE_CARPET, MAGENTA_CARPET]
cheight = 20

def on_on_chat():
    startpos = player.position()
    blocks.place(SLIME_BLOCK, positions.add(startpos, pos(0, -1, 0)))
    player.execute("effect @s jump_boost 9999 99 true")
    player.execute("effect @s slow_falling 9999 99 true")
    counter = 0
    while startpos.get_value(Axis.Y) < 320 - cheight:
        for i in range(cheight):
            for j in range(4):
                player.execute("setblock " + positions.add(startpos, pos(-1 + (2*(j%2)), 0, -1 + (2*(j//2)))) + " barrier")
                blocks.place(carpets[counter%carpets.length], positions.add(startpos, pos(-1 + (2*(j%2)), 0, -1 + (2*(j//2)))))
            startpos = positions.add(startpos, pos(0, 2, 0))
        counter += 1

player.on_chat("run", on_on_chat)
