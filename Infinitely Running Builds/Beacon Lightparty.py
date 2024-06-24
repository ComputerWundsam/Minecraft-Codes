colorarray = [RED_STAINED_GLASS, ORANGE_STAINED_GLASS, YELLOW_STAINED_GLASS, LIME_STAINED_GLASS, LIGHT_BLUE_STAINED_GLASS, MAGENTA_STAINED_GLASS]
positionsets = [pos(0, 0, 0)]
constantvalue = [0]

def on_on_chat():
    counter = 0
    startpos = player.position()
    positionsets.remove_at(0)
    constantvalue.remove_at(0)
    loops.pause(3000)
    for k in range(5):
        for j in range(5):
            for i in range(2):
                blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(5*j+2-i, i, 5*k+2-i)), positions.add(startpos, pos(5*j+-2+i, i, 5*k+-2+i)))
            blocks.place(BEACON, positions.add(startpos,pos(5*j+0, 2, 5*k+0)))
            positionsets.push(positions.add(startpos,pos(5*j+0, 3, 5*k+0)))
            constantvalue.push(randint(0, colorarray.length))
    while True:
        for i in range(positionsets.length):
            blocks.place(colorarray[(counter+constantvalue[i])%colorarray.length], positionsets[i])
        loops.pause(2500)
        counter += 1
player.on_chat("run", on_on_chat)
