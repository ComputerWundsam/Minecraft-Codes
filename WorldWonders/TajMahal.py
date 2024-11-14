startpos = pos(0, 0, 0)
segmentcount = 24
centralcircleradius = 20
pi = 3.14159265359
towersegmentheight = 24
centerheight = 40

def on_on_chat():
    global startpos
    startpos = player.position()
    createfundament()
    for i in range(4):
        createsidetower(positions.add(startpos, pos(4+(5*segmentcount-8)*(i%2), 0,4+(5*segmentcount-4)*(i//2))))
    createcentralcastle(positions.add(startpos, pos(segmentcount*5/2, 8, segmentcount*5/2)))
player.on_chat("run", on_on_chat)






def createfundament():
    for i in range(segmentcount):
        createwalldoorboweast(positions.add(startpos, pos(5*i+1, 0, 0)), 0)
        createwalldoorboweast(positions.add(startpos, pos(5*i+1, 0, 5*segmentcount)), 1)
        createwalldoorbownorth(positions.add(startpos, pos(0, 0, 5*i+1)), 0)
        createwalldoorbownorth(positions.add(startpos, pos(5*segmentcount, 0, 5*i+1)), 1)
    for i in range(4):
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos((5*segmentcount+1)*(i%2), 8,(5*segmentcount+1)*(i//2))), positions.add(startpos, pos((5*segmentcount+1)*(i%2), 0, (5*segmentcount+1)*(i//2))), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(1, 8, 1)), positions.add(startpos, pos(5*segmentcount, 8, 5*segmentcount)), FillOperation.REPLACE)    


def createwalldoorboweast(setpos, south):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(4, 8, 1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(1, 7, south)), positions.add(setpos, pos(3, 7, south)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(1, 0, south)), positions.add(setpos, pos(3, 4, south)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 5), positions.add(setpos, pos(1, 4, south)))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 4), positions.add(setpos, pos(3, 4, south)))

def createwalldoorbownorth(setpos, west):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(1, 8, 4)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(west, 7, 1)), positions.add(setpos, pos(west, 7, 3)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(west, 0, 1)), positions.add(setpos, pos(west, 4, 3)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 7), positions.add(setpos, pos(west, 4, 1)))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 6), positions.add(setpos, pos(west, 4, 3)))

def createsidetower(setpos):
    for i in range(4):
        blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(8-i, 0, 4+i)), positions.add(setpos, pos(-8+i, 8, -4-i)), FillOperation.REPLACE)
    for i in range(3):
        towerradius = 6-i
        for j in range(towerradius * pi):
            blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(Math.sin(j/towerradius)*towerradius, 8 + towersegmentheight  + towersegmentheight*i, Math.cos(j/towerradius)*towerradius)), positions.add(setpos, pos(-Math.sin(j/towerradius)*towerradius, 8 + towersegmentheight*i, Math.cos(j/towerradius)*towerradius)), FillOperation.REPLACE)
        towerradius = towerradius + 2
        for j in range(towerradius * pi):
            blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(Math.sin(j/towerradius)*towerradius, 8 + towersegmentheight + towersegmentheight*i, Math.cos(j/towerradius)*towerradius)), positions.add(setpos, pos(-Math.sin(j/towerradius)*towerradius, 8 + towersegmentheight + towersegmentheight*i, Math.cos(j/towerradius)*towerradius)), FillOperation.REPLACE)
    createsmallpavillon(positions.add(setpos, pos(0, 8 + 3*towersegmentheight, 0)), 6)



def createcentralcastle(setpos):
    for i in range(2):
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-segmentcount*1, 0, -segmentcount*-(1.5-3*i))), positions.add(setpos, pos(segmentcount*1, centerheight, -segmentcount*-(1.5-(3*i)))), FillOperation.REPLACE)
        createbigwindoweast(positions.add(setpos, pos(0, 0, -(segmentcount+3)*(-1.5+3*i))), -1+2*i)
        createbigwindownorth(positions.add(setpos, pos(-(segmentcount+3)*(-1.5+3*i), 0, 0)), -1+2*i)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-segmentcount*-(1.5-3*i), 0, -segmentcount*1)), positions.add(setpos, pos(-segmentcount*-(1.5-(3*i)), centerheight,  segmentcount*1,)), FillOperation.REPLACE)
        for j in range(4):
            createinnerwindowseast(positions.add(setpos, pos((-segmentcount*0.75) * (1 - (2* (j%2))), 5 + 20*(j//2), -segmentcount*-(1.5-3*i))), 10, -1 + (2*i))
            createinnerwindowsnorth(positions.add(setpos, pos(-segmentcount*-(1.5-3*i), 5 + 20*(j//2), (-segmentcount*0.75) * (1 - (2* (j%2))))), 10, -1 + (2*i))    
    for i in range(segmentcount/2 + 1):
        smalltower = 0
        if (i == 0 or i == segmentcount/2):
            smalltower = 8
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-segmentcount*1.5+i, centerheight, -segmentcount*1-i)), positions.add(setpos, pos(segmentcount*1.5-i, centerheight, segmentcount*1+i)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-segmentcount*1.5+i, 0, -segmentcount*1-i)), positions.add(setpos, pos(-segmentcount*1.5+i, centerheight + smalltower, -segmentcount*1-i)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(segmentcount*1.5-i, 0, -segmentcount*1-i)), positions.add(setpos, pos(segmentcount*1.5-i, centerheight + smalltower, -segmentcount*1-i)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(segmentcount*1.5-i, 0, segmentcount*1+i)), positions.add(setpos, pos(segmentcount*1.5-i, centerheight + smalltower, segmentcount*1+i)), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-segmentcount*1.5+i, 0, segmentcount*1+i)), positions.add(setpos, pos(-segmentcount*1.5+i, centerheight + smalltower, segmentcount*1+i)), FillOperation.REPLACE)

    createcentralcircletower(positions.add(setpos, pos(0, centerheight, 0)))


def createcentralcircletower(setpos):
    for i in range(centralcircleradius*pi):
        blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(-Math.sin(i/centralcircleradius)*centralcircleradius, 0, Math.cos(i/centralcircleradius)*centralcircleradius)),
            positions.add(setpos, pos(Math.sin(i/centralcircleradius)*centralcircleradius, 25, Math.cos(i/centralcircleradius)*centralcircleradius)), FillOperation.REPLACE)
    j = 0
    orbsize = 1
    while (orbsize > 0):
        orbsize = Math.sin((centralcircleradius+j)/(centralcircleradius+2))*(centralcircleradius+2)
        if(blocks.test_for_block(AIR, positions.add(setpos, pos(0, 21+(j/2), 0)))):
            for i in range(orbsize*pi):
                blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(-Math.sin(i/orbsize)*orbsize, 21+(j/2), Math.cos(i/orbsize)*orbsize)),
                    positions.add(setpos, pos(Math.sin(i/orbsize)*orbsize, 21+(j/2), Math.cos(i/orbsize)*orbsize)), FillOperation.REPLACE)
        j += 2
    blocks.fill(GOLD_BLOCK, positions.add(setpos, pos(0, 21, 0)), positions.add(setpos, pos(0, 21+j, 0)), FillOperation.REPLACE)
    for i in range(4):
        createsmallpavillon(positions.add(setpos, pos(-(centralcircleradius+2)+ 2*(centralcircleradius+2)*(i%2), 0 , -(centralcircleradius+2)+ 2*(centralcircleradius+2)*(i//2))), 8)


def createsmallpavillon(setpos, towerradius):
    pillarradius = towerradius - 2
    for i in range(8):
        val = 2*pi*i/8
        blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(Math.sin(val)*pillarradius, 0, Math.cos(val)*pillarradius)), positions.add(setpos, pos(Math.sin(val)*pillarradius, 8, Math.cos(val)*pillarradius)))
    for i in range(towerradius*pi):
        blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(Math.sin(i/towerradius)*towerradius, 8, Math.cos(i/towerradius)*towerradius)), positions.add(setpos, pos(-Math.sin(i/towerradius)*towerradius,  8, Math.cos(i/towerradius)*towerradius)), FillOperation.REPLACE)
    for i in range(pillarradius*pi/2):
        if(blocks.test_for_block(AIR, positions.add(setpos, pos(0, 9 + Math.sin(i/pillarradius)*pillarradius, 0)))):
            tvalue = Math.cos(i/pillarradius)*pillarradius
            for j in range((Math.cos(i/pillarradius)*pillarradius)*pi):
                blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(Math.sin(j/tvalue)*tvalue, 9 + Math.sin(i/pillarradius)*pillarradius, Math.cos(j/tvalue)*tvalue)), 
                        positions.add(setpos, pos(-Math.sin(j/tvalue)*tvalue, 9 + Math.sin(i/pillarradius)*pillarradius, Math.cos(j/tvalue)*tvalue)), FillOperation.REPLACE)
    blocks.fill(GOLD_BLOCK, positions.add(setpos, pos(0, 9 + pillarradius, 0)), positions.add(setpos, pos(0, 9 + pillarradius*2, 0)), FillOperation.REPLACE)

def createbigwindownorth(setpos, north):
    size = 20
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(0, size, -size/2-1)), positions.add(setpos, pos(4 * north, 0, size/2+1)), FillOperation.REPLACE)
    createinnerwindowsnorth(positions.add(setpos, pos(0, size, 0)), size, north)
    blocks.fill(AIR, positions.add(setpos, pos(0, size, -size/2)), positions.add(setpos, pos(3 * north, 1, size/2)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(0, centerheight, (-size/2-1)*(-1+2*i))), positions.add(setpos, pos(0, centerheight+8, (-size/2-1)*(-1+2*i))), FillOperation.REPLACE)

def createinnerwindowsnorth(setpos, size, north):
    halfsize = size/2
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(0, size, -halfsize-1)), positions.add(setpos, pos(4 * north, -1, halfsize+1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(0, size/2, -halfsize)), positions.add(setpos, pos(3 * north , 0, halfsize)), FillOperation.REPLACE)
    for i in range(halfsize*pi/2 +1):
        blocks.fill(AIR, positions.add(setpos, pos(0, i/2+halfsize, Math.cos(i/halfsize)*halfsize)), positions.add(setpos, pos(3 * north, i/2+halfsize, -Math.cos(i/halfsize)*halfsize)), FillOperation.REPLACE)
    

def createbigwindoweast(setpos, east):
    size = 20
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-size/2-1, size, 0)), positions.add(setpos, pos(size/2+1, 0, 4 * east)), FillOperation.REPLACE)
    createinnerwindowseast(positions.add(setpos, pos(0, size, 0)), size, east)
    blocks.fill(AIR, positions.add(setpos, pos(-size/2, size, 0)), positions.add(setpos, pos(size/2, 1, 3 * east)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos((-size/2-1)*(-1+2*i), centerheight, 0)), positions.add(setpos, pos((-size/2-1)*(-1+2*i), centerheight+8, 0)), FillOperation.REPLACE)

def createinnerwindowseast(setpos, size, east):
    halfsize = size/2
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(setpos, pos(-halfsize-1, size, 0)), positions.add(setpos, pos(halfsize+1, -1, 4 * east)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(-halfsize, size/2, 0)), positions.add(setpos, pos(halfsize, 0, 3 * east)), FillOperation.REPLACE)
    for i in range(halfsize*pi/2 +1):
        blocks.fill(AIR, positions.add(setpos, pos(Math.cos(i/halfsize)*halfsize, i/2+halfsize, 0)), positions.add(setpos, pos(-Math.cos(i/halfsize)*halfsize, i/2+halfsize, 3 * east)), FillOperation.REPLACE)
    

def on_chat():
    createcentralcastle(player.position())
player.on_chat("jump", on_chat)
