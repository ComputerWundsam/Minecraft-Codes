streetblock = BLACK_CONCRETE
borderblock = STONE_BRICKS
stripeblock = WHITE_CONCRETE

bridgearray = [60, 60, 15, 11, 9, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 9, 11, 15, 60, 60]
stripearray = [1, 11, 13, 23]

def on_on_chat():
    startpos = player.position().to_world()
    counter = 0
    while True:
        blocks.fill(AIR, startpos, positions.add(startpos, pos(0, 10, 24)))
        blocks.fill(streetblock, startpos, positions.add(startpos, pos(0, 0, 24)))
        blocks.fill(borderblock, positions.add(startpos, pos(0, -1, 0)), positions.add(startpos, pos(0, -bridgearray[counter%bridgearray.length], 24)))
        for i in range(stripearray.length):
            blocks.place(stripeblock, positions.add(startpos, pos(0, 0, stripearray[i])))
        for i in range(3):
            blocks.place(borderblock, positions.add(startpos, pos(0, 1, 12*i)))
        if(counter % 20 >= 10):
            blocks.place(stripeblock, positions.add(startpos, pos(0, 0, 6)))
            blocks.place(stripeblock, positions.add(startpos, pos(0, 0, 18)))
        if(counter % 8 == 0):
            for i in range(3): 
                blocks.fill(BLACKSTONE_WALL, positions.add(startpos, pos(0, 2, 12*i)), positions.add(startpos, pos(0, 6, 12*i)))
                blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, pos(0, 7, 12*i)))
        counter += 1
        startpos = positions.add(startpos, pos(1, 0, 0))

player.on_chat("run", on_on_chat)
