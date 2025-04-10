bridgearray = [50, 50, 15, 11, 9, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2]
width = 28
stripearray = [1, width/2-1, width/2+1, width-1]

#First execute "setup" command, and then "run" command

def prepare():
    startpos = player.position()
    blocks.fill(STONE_BRICKS, positions.add(startpos, pos(0, 0, 0)), positions.add(startpos, pos(1, 50, width)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(0, 50, 1)), positions.add(startpos, pos(1, 50, width-1)), FillOperation.REPLACE)
    blocks.fill(OBSIDIAN, positions.add(startpos, pos(0, 49, 1)), positions.add(startpos, pos(1, 49, width-1)), FillOperation.REPLACE)
    blocks.fill(STONE_BRICKS, positions.add(startpos, pos(0, 50, width/2)), positions.add(startpos, pos(1, 50, width/2)), FillOperation.REPLACE)
    blocks.place(WHITE_CONCRETE, positions.add(startpos, pos(1, 49, (width/4))))
    blocks.place(WHITE_CONCRETE, positions.add(startpos, pos(1, 49, 3*(width/4))))
    for i in range(stripearray.length):
        blocks.fill(WHITE_CONCRETE, positions.add(startpos, pos(0, 49, stripearray[i])), positions.add(startpos, pos(1, 49, stripearray[i])), FillOperation.REPLACE)
    for i in range(bridgearray.length):
        blocks.save_structure("first" + bridgearray[i], positions.add(startpos, pos(0, 50-bridgearray[i], 0)), positions.add(startpos, pos(0, 60, width)))
        blocks.save_structure("second" + bridgearray[bridgearray.length-i-1], positions.add(startpos, pos(1, 50-bridgearray[bridgearray.length-i-1], 0)), positions.add(startpos, pos(1, 60, width)))
player.on_chat("setup", prepare)


def highway():
    startpos = pos(0, -50, 0).to_world()
    while True:
        for i in range(bridgearray.length):
            blocks.load_structure("first" + bridgearray[i], positions.add(startpos, pos(i, 50-bridgearray[i], 0)))
        startpos = positions.add(startpos, pos(bridgearray.length, 0, 0))
        for i in range(bridgearray.length):
                blocks.load_structure("second" + bridgearray[bridgearray.length-i-1], positions.add(startpos, pos(i, 50-bridgearray[bridgearray.length-i-1], 0)))
        startpos = positions.add(startpos, pos(bridgearray.length, 0, 0))
player.on_chat("run", highway)
