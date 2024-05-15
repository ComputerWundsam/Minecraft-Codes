fibo = [3, 5, 8, 13]
buildingblock = IRON_BLOCK
counter = 0

def on_on_chat():
    startpos = player.position()
    loops.pause(1000)
    global counter
    radius = 4
    for i in range(4):
        shapes.circle(buildingblock, startpos, radius, Axis.X, ShapeOperation.REPLACE)
        startpos = positions.add(startpos, pos(1, 0, 0))
        setbuildingblock()
        radius += 1
    for f in range(fibo.length):
        for i in range(fibo[fibo.length-f]):
            shapes.circle(buildingblock, startpos, radius, Axis.X, ShapeOperation.REPLACE)
            startpos = positions.add(startpos, pos(1, 0, 0))
            setbuildingblock()
        radius -= 1
    for i in range(8):
        blocks.fill(buildingblock, positions.add(startpos, pos(0, -8-radius+i, 0)), positions.add(startpos, pos(0, 8+radius-i, 0)))
        blocks.fill(buildingblock, positions.add(startpos, pos(0, 0, -8-radius+i)), positions.add(startpos, pos(0, 0, 8+radius-i)))
        startpos = positions.add(startpos, pos(-1, 0, 0))
        setbuildingblock()

player.on_chat("run", on_on_chat)


def setbuildingblock():
    global counter
    global buildingblock
    counter += 1
    player.say(counter)
    if(counter%2 == 0):
        buildingblock = IRON_BLOCK
    else:
        buildingblock = REDSTONE_BLOCK


