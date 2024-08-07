pi = 3.14159265359
outrad = 30  
inrad = 5
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createvolcano()
    fillwithlava()
player.on_chat("run", on_on_chat)

def createvolcano():
    for j in range(outrad):
        setrad = (1-Math.sin(pi*j/(2*outrad)))*(outrad)+inrad+2
        for i in range(2*setrad*pi):
            if (randint(0, outrad*outrad*inrad)-j*j) < 2:
                setblock = MAGMA_BLOCK
            else:
                setblock = OBSIDIAN
            blocks.fill(setblock, positions.add(startpos, pos(Math.sin(i/setrad)*inrad, j, Math.cos(i/setrad)*inrad)),
                    positions.add(startpos, pos(Math.sin(i/setrad)*setrad, j, Math.cos(i/setrad)*setrad)), FillOperation.REPLACE)

def fillwithlava():
    for i in range(2*(inrad+1)*pi):
        blocks.fill(LAVA, positions.add(startpos, pos(Math.sin(i/inrad)*inrad, outrad-3, Math.cos(i/inrad)*inrad)), startpos, FillOperation.REPLACE)
        blocks.place(CAMPFIRE, positions.add(startpos, pos(Math.sin(i/(inrad+1))*(inrad+1), outrad-2, Math.cos(i/(inrad+1))*(inrad+1))))


