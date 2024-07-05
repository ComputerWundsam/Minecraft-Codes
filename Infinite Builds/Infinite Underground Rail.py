def trainrun():
    startpos = player.position().to_world()
    counter = 0
    while True:
        player.execute("fill " + positions.add(startpos, pos(1, 0, -3)) + " " + positions.add(startpos, pos(0, 5, 3)) + " barrier")        
        blocks.fill(AIR, positions.add(startpos, pos(0, 0, -2)), positions.add(startpos, pos(0, 4, 2)), FillOperation.REPLACE)
        if(counter % 75 == 0):
            blocks.place(REDSTONE_BLOCK, positions.add(startpos, pos(0, 0, 0)))
            blocks.place(POWERED_RAIL, positions.add(startpos, pos(0, 1, 0)))
        else:
            blocks.place(OCHRE_FROGLIGHT, positions.add(startpos, pos(0, 0, 0)))
            blocks.place(RAIL, positions.add(startpos, pos(0, 1, 0)))
        startpos = positions.add(startpos, pos(1, 0, 0))
        counter += 1
player.on_chat("run", trainrun)


