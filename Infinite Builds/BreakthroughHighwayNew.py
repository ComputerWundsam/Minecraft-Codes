streetblock = BLACK_CONCRETE
borderblock = STONE_BRICKS
stripeblock = WHITE_CONCRETE
width = 100


bridgearray = [60, 60, 15, 11, 9, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 9, 11, 15, 60, 60]
stripearray = [1, width/2-1, width/2+1, width-1]

def on_on_chat():
    startpos = player.position().to_world()
    counter = 0
    while True:
        blocks.fill(AIR, startpos, positions.add(startpos, pos(0, 10, width)))
        blocks.fill(streetblock, startpos, positions.add(startpos, pos(0, 0, width)))
        blocks.fill(borderblock, positions.add(startpos, pos(0, -1, 0)), positions.add(startpos, pos(0, -bridgearray[counter%bridgearray.length], width)))
        for i in range(stripearray.length):
            blocks.place(stripeblock, positions.add(startpos, pos(0, 0, stripearray[i])))
        for i in range(3):
            blocks.place(borderblock, positions.add(startpos, pos(0, 1, (width/2)*i)))
        if(counter % 20 == 19):
            for i in range(7):
                blocks.fill(stripeblock, positions.add(startpos, pos(0, 0, 7+6*i)), positions.add(startpos, pos(-9, 0, 7+6*i)))
                blocks.fill(stripeblock, positions.add(startpos, pos(0, 0, width/2+7+6*i)), positions.add(startpos, pos(-9, 0, width/2+7+6*i)))
        if(counter % 16 == 0):
            for i in range(3):
                blocks.fill(BLACKSTONE_WALL, positions.add(startpos, pos(0, 2, (width/2)*i)), positions.add(startpos, pos(0, 6, (width/2)*i)))
                blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, pos(0, 7, (width/2)*i)))
        counter += 1
        startpos = positions.add(startpos, pos(1, 0, 0))

player.on_chat("run", on_on_chat)
