streetblock = STONE_BRICKS
borderblock = STONE_BRICKS
stripeblock = WHITE_CONCRETE
size = 10


bridgearray = [60, 30, 15, 11, 9, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 9, 11, 15, 60, 60]

def on_on_chat():
    startpos = player.position().to_world()
    counter = 0
    while blocks.test_for_block(AIR, startpos):
        blocks.fill(AIR, startpos, positions.add(startpos, pos(0, 10, size)))
        blocks.fill(streetblock, startpos, positions.add(startpos, pos(0, 0, size)))
        blocks.fill(borderblock, positions.add(startpos, pos(0, -1, 0)), positions.add(startpos, pos(0, -bridgearray[counter%bridgearray.length], size)))
        for i in range(2):
            if (counter%2 == 0):
                blocks.fill(streetblock, positions.add(startpos, pos(0, 1, size*i)), positions.add(startpos, pos(0, 2, size*i)))
                if(counter % 16 == 0):
                    blocks.fill(BLACKSTONE_WALL, positions.add(startpos, pos(0, 3, size*i)), positions.add(startpos, pos(0, 7, size*i)))
                    blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, pos(0, 8, size*i)))
            else:
                blocks.place(streetblock, positions.add(startpos, pos(0, 1, size*i)))
        counter += 1
        startpos = positions.add(startpos, pos(1, 0, 0))
player.on_chat("run", on_on_chat)
