
towersize = 6
castlesize = 50
height = 10
iceblock = BLUE_ICE
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    startpos = player.position()
    createwalls()
    creategate()
    for i in range(4):
        createicetower(positions.add(startpos, pos(-(castlesize-1) + (2*(castlesize-1)*(i%2)), 0, -(castlesize-1) + (2*(castlesize-1)*(i//2)))))
    createicetowerdoors()

player.on_chat("run", on_on_chat)

def createwalls():
    blocks.fill(iceblock, positions.add(startpos, pos(-castlesize, 0, -castlesize+3)), positions.add(startpos, pos(castlesize, height, -castlesize)), FillOperation.REPLACE)
    blocks.fill(iceblock, positions.add(startpos, pos(castlesize-3, 0, -castlesize)), positions.add(startpos, pos(castlesize, height, castlesize)), FillOperation.REPLACE)
    blocks.fill(iceblock, positions.add(startpos, pos(-castlesize, 0, castlesize-3)), positions.add(startpos, pos(castlesize, height, castlesize)), FillOperation.REPLACE)
    blocks.fill(iceblock, positions.add(startpos, pos(-castlesize+3, 0, -castlesize)), positions.add(startpos, pos(-castlesize, height, castlesize)), FillOperation.REPLACE)
    for i in range(castlesize*2):
        blocks.fill(iceblock, positions.add(startpos, pos(-castlesize+i, 0, -castlesize)), positions.add(startpos, pos(-castlesize+i, height+1+(i%2), -castlesize)), FillOperation.REPLACE)
        blocks.fill(iceblock, positions.add(startpos, pos(castlesize-i, 0, castlesize)), positions.add(startpos, pos(castlesize-i, height+1+(i%2), castlesize)), FillOperation.REPLACE)
        blocks.fill(iceblock, positions.add(startpos, pos(-castlesize, 0, -castlesize+i)), positions.add(startpos, pos(-castlesize, height+1+(i%2), -castlesize+i)), FillOperation.REPLACE)
        blocks.fill(iceblock, positions.add(startpos, pos(castlesize, 0, castlesize-i)), positions.add(startpos, pos(castlesize, height+1+(i%2), castlesize-i)), FillOperation.REPLACE)

def createicetower(setpos):
    blocks.fill(iceblock, positions.add(setpos, pos(-towersize, 0, -towersize)), positions.add(setpos, pos(towersize, 2*height, towersize)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(-towersize+1, height+1, -towersize+1)), positions.add(setpos, pos(towersize-1, 2*height-1, towersize-1)), FillOperation.REPLACE)
    for i in range(towersize*2+1):
        blocks.fill(iceblock, positions.add(setpos, pos(-towersize+i, 2*height, -towersize)), positions.add(setpos, pos(-towersize+i, 2*height+2-(i%2), -towersize)), FillOperation.REPLACE)
        blocks.fill(iceblock, positions.add(setpos, pos(towersize-i, 2*height, towersize)), positions.add(setpos, pos(towersize-i, 2*height+2-(i%2), towersize)), FillOperation.REPLACE)
        blocks.fill(iceblock, positions.add(setpos, pos(-towersize, 2*height, -towersize+i)), positions.add(setpos, pos(-towersize, 2*height+2-(i%2), -towersize+i)), FillOperation.REPLACE)
        blocks.fill(iceblock, positions.add(setpos, pos(towersize, 2*height, towersize-i)), positions.add(setpos, pos(towersize, 2*height+2-(i%2), towersize-i)), FillOperation.REPLACE)
    
def createicetowerdoors():
    blocks.fill(AIR, positions.add(startpos, pos(-castlesize+1, height+1, -castlesize+1)), positions.add(startpos, pos(castlesize-1, height+2, -castlesize+1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(castlesize-1, height+1, -castlesize+1)), positions.add(startpos, pos(castlesize-1, height+2, castlesize-1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-castlesize+1, height+1, castlesize-1)), positions.add(startpos, pos(castlesize-1, height+2, castlesize-1)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(-castlesize+1, height+1, -castlesize+1)), positions.add(startpos, pos(-castlesize+1, height+2, castlesize-1)), FillOperation.REPLACE)

    
def creategate():
    blocks.fill(AIR, positions.add(startpos, pos(castlesize-3, 0, -2)), positions.add(startpos, pos(castlesize+1, height/2, 2)), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(castlesize, 0, -3)), positions.add(startpos, pos(castlesize, height/2+1, 3)), FillOperation.REPLACE)
    blocks.fill(NETHER_BRICK_FENCE, positions.add(startpos, pos(castlesize, 0, -2)), positions.add(startpos, pos(castlesize, height/2, 2)), FillOperation.REPLACE)
    createicetower(positions.add(startpos, pos(castlesize-2, 0, -4-2*towersize)))
    createicetower(positions.add(startpos, pos(castlesize-2, 0, 4+2*towersize)))


def on_chat():
    createicetower(player.position())
player.on_chat("jump", on_chat)
