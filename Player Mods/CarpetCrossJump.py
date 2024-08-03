x = [-1, 0, 0, 1]
z = [0, -1, 1, 0]
carpets = [PINK_CARPET, RED_CARPET, BROWN_CARPET, ORANGE_CARPET, YELLOW_CARPET, WHITE_CARPET, LIME_CARPET, GREEN_CARPET, BLACK_CARPET, BLUE_CARPET, LIGHT_BLUE_CARPET, PURPLE_CARPET, MAGENTA_CARPET]
cheight = 10

def on_on_chat():
    startpos = player.position()
    blocks.place(SLIME_BLOCK, positions.add(startpos, pos(0, -1, 0)))
    player.execute("effect @s jump_boost 9999 90 true")
    counter = 0
    while startpos.get_value(Axis.Y) < 320 - cheight:
        for i in range(cheight):
            for j in range(4):
                player.execute("setblock " + positions.add(startpos, pos(x[j], 0, z[j])) + " barrier")
                blocks.place(carpets[counter%carpets.length], positions.add(startpos, pos(x[j], 0, z[j])))
            startpos = positions.add(startpos, pos(0, 2, 0))
        counter += 1
player.on_chat("run", on_on_chat)
