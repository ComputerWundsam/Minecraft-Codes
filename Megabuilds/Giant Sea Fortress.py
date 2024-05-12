
bowblock = IRON_BLOCK
baseblock = GOLD_BLOCK
roofblock = DIAMOND_BLOCK
centerblock = WHITE_CONCRETE
buildingblock = LIGHT_GRAY_CONCRETE
windowblock = WHITE_STAINED_GLASS
startpos = pos(0, 0, 0)
levelheight = 4

def on_on_chat():
    global startpos
    startpos = player.position().to_world()
    createtowerparts(8)
player.on_chat("test", on_on_chat)

def createtowerparts(levels):
    global startpos
    for k in range(levels):
        width = (levels-k+1)*2
        hwidth = width / 2
        for i in range(levels-k):
            blocks.fill(buildingblock,
                positions.add(startpos, pos(-hwidth, i * levelheight, -hwidth)),
                positions.add(startpos, pos(hwidth, i * levelheight, hwidth)),
                FillOperation.REPLACE)
            for j in range(width):
                if j == 0:
                    setblock = roofblock
                elif j % 2 == 0:
                    setblock = buildingblock
                else:
                    setblock = windowblock
                blocks.fill(setblock,
                    positions.add(startpos, pos(-hwidth + j, i * levelheight + 1, -hwidth)),
                    positions.add(startpos,
                        pos(-hwidth + j, i * levelheight + levelheight - 1, -hwidth)),
                    FillOperation.REPLACE)
                blocks.fill(setblock,
                    positions.add(startpos, pos(hwidth, i * levelheight + 1, -hwidth + j)),
                    positions.add(startpos,
                        pos(hwidth, i * levelheight + levelheight - 1, -hwidth + j)),
                    FillOperation.REPLACE)
                blocks.fill(setblock,
                    positions.add(startpos, pos(hwidth - j, i * levelheight + 1, hwidth)),
                    positions.add(startpos, pos(hwidth - j, i * levelheight + levelheight - 1, hwidth)),
                    FillOperation.REPLACE)
                blocks.fill(setblock,
                    positions.add(startpos, pos(-hwidth, i * levelheight + 1, hwidth - j)),
                    positions.add(startpos,
                        pos(-hwidth, i * levelheight + levelheight - 1, hwidth - j)),
                    FillOperation.REPLACE)
        blocks.fill(roofblock,
            positions.add(startpos, pos(-hwidth, ((levels-k) * levelheight), -hwidth)),
            positions.add(startpos, pos(hwidth, ((levels-k) * levelheight) , hwidth)),
            FillOperation.REPLACE)
        startpos = positions.add(startpos, pos(0, ((levels-k) * levelheight), 0))
    blocks.fill(baseblock, startpos, positions.add(startpos, pos(0, 20, 0)))

def createbase():
    global startpos
    blocks.fill(baseblock,
        positions.add(startpos, pos(34, 0, -3)),
        positions.add(startpos, pos(28, -50, 3)),
        FillOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(-34, 0, -3)),
        positions.add(startpos, pos(-28, -50, 3)),
        FillOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(-3, 0, -34)),
        positions.add(startpos, pos(3, -50, -28)),
        FillOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(-3, 0, 34)),
        positions.add(startpos, pos(3, -50, 28)),
        FillOperation.REPLACE)
    for i in range(10):
        shapes.circle(centerblock, startpos, 30-i, Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(AIR, startpos, 28-i, Axis.Y, ShapeOperation.REPLACE)
        startpos = positions.add(startpos, pos(0, -1, 0))
    shapes.circle(centerblock, startpos, 20, Axis.Y, ShapeOperation.REPLACE)
    


def createbow():
    global startpos
    shapes.circle(bowblock, startpos, 50, Axis.X, ShapeOperation.REPLACE)
    shapes.circle(bowblock, startpos, 50, Axis.Z, ShapeOperation.REPLACE)
    shapes.circle(bowblock, startpos, 50, Axis.Y, ShapeOperation.REPLACE)
    shapes.circle(AIR, startpos, 46, Axis.X, ShapeOperation.REPLACE)
    shapes.circle(AIR, startpos, 46, Axis.Z, ShapeOperation.REPLACE)
    shapes.circle(AIR, startpos, 46, Axis.Y, ShapeOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(52, 0, -3)),
        positions.add(startpos, pos(46, -50, 3)),
        FillOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(-3, 0, 52)),
        positions.add(startpos, pos(3, -50, 46)),
        FillOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(-52, 0, -3)),
        positions.add(startpos, pos(-46, -50, 3)),
        FillOperation.REPLACE)
    blocks.fill(baseblock,
        positions.add(startpos, pos(-3, 0, -52)),
        positions.add(startpos, pos(3, -50, -46)),
        FillOperation.REPLACE)

def seaskyscraper():
    global startpos
    startpos = player.position().to_world()
    loops.pause(10000)
    createbow()
    createbase()
    createtowerparts(7)
    
player.on_chat("run", seaskyscraper)
