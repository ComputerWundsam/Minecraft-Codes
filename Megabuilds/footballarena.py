pi = 3.14159265359
rowsize = 14
arenawidth = 140
lengthmod = 60
circleradius = 12
outersquare = 16
innersquare = 8
arenaoffset = 8
goalsize = 4

karray = [[0, -1, 0, 1], [1, 0, -1, 0]]

def on_on_chat():
    startpos = player.position()
    for i in range(rowsize):
        blocks.place(LIGHT_BLUE_CONCRETE, positions.add(startpos, pos(i, i, 0)))
        blocks.place(WHITE_CONCRETE, positions.add(startpos,pos(rowsize-i, 17+i//4, 0)))
    blocks.fill(IRON_BLOCK, positions.add(startpos,pos(rowsize, rowsize, 0)), positions.add(startpos,pos(rowsize, 16, 0)), FillOperation.REPLACE)
    blocks.save_structure("row0", positions.add(startpos,pos(0, 0, 0)), positions.add(startpos,pos(rowsize, 20, 0)))
    blocks.load_structure("row0", positions.add(startpos, pos(0, 0, 4)))
    blocks.replace(LIGHT_BLUE_CONCRETE, WHITE_CONCRETE, positions.add(startpos, pos(0, rowsize, 4)), positions.add(startpos, pos(rowsize, 20, 4)))
    blocks.replace(BLUE_CONCRETE, LIGHT_BLUE_CONCRETE, positions.add(startpos, pos(0, 0, 4)), positions.add(startpos, pos(rowsize, rowsize, 4)))
    blocks.save_structure("row1", positions.add(startpos,pos(0, 0, 4)), positions.add(startpos,pos(rowsize, 20, 4)))
player.on_chat("run", on_on_chat)

def createcorner():
    
    startpos = player.position()
    for j in range(rowsize*pi/2+1):
        for i in range(rowsize):
            blocks.fill(LIGHT_BLUE_CONCRETE, positions.add(startpos, pos(Math.sin(j/rowsize)*i-1, i, Math.cos(j/rowsize)*i-1)), positions.add(startpos, pos(Math.sin(j/rowsize)*i+1, i, Math.cos(j/rowsize)*i+1)))
            blocks.fill(WHITE_CONCRETE, positions.add(startpos,pos(Math.sin(j/rowsize)*i-1, 19-i//4, Math.cos(j/rowsize)*i-1)), positions.add(startpos,pos(Math.sin(j/rowsize)*i+1, 19-i//4, Math.cos(j/rowsize)*i+1)))
        blocks.fill(IRON_BLOCK, positions.add(startpos,pos(Math.sin(j/rowsize)*rowsize, rowsize, Math.cos(j/rowsize)*rowsize)), positions.add(startpos,pos(Math.sin(j/rowsize)*rowsize, 16, Math.cos(j/rowsize)*rowsize)), FillOperation.REPLACE)
    blocks.save_structure("corner", startpos, positions.add(startpos, pos(rowsize, 20, rowsize)))
player.on_chat("corner", createcorner)


def createstadium():
    startpos = player.position()
    loops.pause(3000)
    createfootballfield(positions.add(startpos, pos(-arenawidth-lengthmod, -1, 0)))
    for k in range(4):
        for i in range(arenawidth + (lengthmod*((k)%2))):
            blocks.load_structure("row" + i%2, startpos, k)
            startpos = positions.add(startpos, pos(karray[0][k]*1, 0, karray[1][k]*1))
        if k == 1:
            startpos = positions.add(startpos, pos(rowsize*karray[0][k], 0, 0))
        if k == 2:
            startpos = positions.add(startpos, pos(0, 0, rowsize*karray[1][k]))
        blocks.load_structure("corner", startpos, k)
        if k == 2:
                startpos = positions.add(startpos, pos(rowsize, 0, 0))

def createfootballfield(setpos):
    blocks.fill(GRASS, positions.add(setpos, pos(0, 0, 0)), positions.add(setpos, pos(arenawidth+lengthmod, 0, arenawidth)), FillOperation.REPLACE)
    setwhitesquare(positions.add(setpos, pos(arenaoffset, 0, arenaoffset)), positions.add(setpos, pos(arenawidth+lengthmod-arenaoffset, 0, arenawidth-arenaoffset)))
    blocks.fill(WHITE_CONCRETE, positions.add(setpos, pos((arenawidth+lengthmod)/2, 0, arenaoffset)), positions.add(setpos, pos((arenawidth+lengthmod)/2, 0, arenawidth-arenaoffset)), FillOperation.REPLACE)
    setwhitesquare(positions.add(setpos, pos(arenaoffset, 0, arenawidth/2-outersquare)), positions.add(setpos, pos(arenaoffset+outersquare, 0, arenawidth/2+outersquare)))
    setwhitesquare(positions.add(setpos, pos(arenawidth+lengthmod-arenaoffset-outersquare, 0, arenawidth/2-outersquare)), positions.add(setpos, pos(arenawidth+lengthmod-arenaoffset, 0, arenawidth/2+outersquare)))
    setwhitesquare(positions.add(setpos, pos(arenaoffset, 0, arenawidth/2-innersquare)), positions.add(setpos, pos(arenaoffset+innersquare, 0, arenawidth/2+innersquare)))
    setwhitesquare(positions.add(setpos, pos(arenawidth+lengthmod-arenaoffset-innersquare, 0, arenawidth/2-innersquare)), positions.add(setpos, pos(arenawidth+lengthmod-arenaoffset, 0, arenawidth/2+innersquare)))
    creategoal(positions.add(setpos, pos(arenaoffset, 0, arenawidth/2)), -1)
    creategoal(positions.add(setpos, pos(arenawidth + lengthmod - arenaoffset, 0, arenawidth/2)), 1)
    setcentercircle(positions.add(setpos, pos((arenawidth+lengthmod)/2, 0, arenawidth/2)))



def creategoal(setpos, front):
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, 0, goalsize)), positions.add(setpos, pos(goalsize * front, goalsize, -goalsize)), FillOperation.HOLLOW)
    blocks.fill(AIR, positions.add(setpos, pos(0, 1, goalsize-1)), positions.add(setpos, pos(0, goalsize-1, -goalsize+1)), FillOperation.REPLACE)
    blocks.replace(COBWEB, IRON_BLOCK, positions.add(setpos, pos(0, 1, goalsize-1)), positions.add(setpos, pos(goalsize * front, goalsize-1, -goalsize+1)))
    blocks.replace(COBWEB, IRON_BLOCK, positions.add(setpos, pos(1, 1, goalsize-1)), positions.add(setpos, pos((goalsize-1) * front, goalsize, -goalsize+1)))
    blocks.replace(COBWEB, IRON_BLOCK, positions.add(setpos, pos(1, 1, goalsize)), positions.add(setpos, pos((goalsize-1) * front, goalsize-1, -goalsize)))



def setwhitesquare(firstpos, secondpos):
    blocks.fill(WHITE_CONCRETE, firstpos, secondpos, FillOperation.REPLACE)
    blocks.fill(GRASS, positions.add(firstpos, pos(1, 0, 1)), positions.add(secondpos, pos(-1, 0, -1)), FillOperation.REPLACE)

def setcentercircle(setpos):
    for i in range(circleradius*pi):
        blocks.place(WHITE_CONCRETE, positions.add(setpos, pos(Math.sin(i/circleradius)*circleradius, 0, Math.cos(i/circleradius)*circleradius)))
        blocks.place(WHITE_CONCRETE, positions.add(setpos, pos(-Math.sin(i/circleradius)*circleradius, 0, Math.cos(i/circleradius)*circleradius)))
player.on_chat("stadium", createstadium)
