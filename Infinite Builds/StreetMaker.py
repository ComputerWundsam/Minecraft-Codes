xdir = [1, 0, -1, 0]
zdir = [0, -1, 0, 1]
size = 3
radius = 20
pi = 3.14159265359
outsize = 4

startpos = player.position()
def on_on_chat():
    c = 100
    global startpos, outsize
    outsize = size+1    
    startpos = positions.add(player.position(), pos(0, -1, 0))
    for i in range(20000):
        if c <= 4:
            c += 100
        CreateStreet(startpos)
        startpos = positions.add(startpos, pos(xdir[c%xdir.length], 0, zdir[c%zdir.length]))
        dirs = randint(0, 20)
        if(dirs < 5):
            startpos = positions.add(startpos, pos(xdir[(c+1)%xdir.length], 0, zdir[(c+1)%zdir.length]))
            dirs = randint(0, 20)
            if dirs < 1:
                c += 1
                createcurve(positions.add(startpos, pos(xdir[(c)%xdir.length]*radius, 0, zdir[(c)%zdir.length]*radius)), c+2, c+3)
                startpos = positions.add(startpos, pos((xdir[(c+3)%xdir.length] + xdir[(c+4)%xdir.length])*radius, 0, (zdir[(c+3)%zdir.length] + zdir[(c+4)%zdir.length])*radius))
        elif (dirs > 15):
            startpos = positions.add(startpos, pos(xdir[(c-1)%xdir.length], 0, zdir[(c-1)%zdir.length]))
            dirs = randint(0, 20)
            if dirs < 1:
                createcurve(positions.add(startpos, pos(xdir[(c-1)%xdir.length]*radius, 0, zdir[(c-1)%zdir.length]*radius)), c, c+1)
                startpos = positions.add(startpos, pos((xdir[(c+3)%xdir.length] + xdir[(c+4)%xdir.length])*radius, 0, (zdir[(c+3)%zdir.length] + zdir[(c+4)%zdir.length])*radius))
                c -= 1
        if i % 20 == 0:
            createstreetlamps()

def createcurve(setpos, fc, sc):
    global startpos
    setx = xdir[fc%xdir.length]+xdir[sc%xdir.length]
    setz = zdir[fc%zdir.length]+zdir[sc%zdir.length]
    change = (sc%xdir.length)*(pi/2)
    for i in range(radius*pi/2):
        CreateStreet(positions.add(setpos, pos(Math.sin((i+change)/radius)*radius*setx, 0, Math.cos((i+change)/radius)*radius*setz)))

def createstreetlamps():
    for i in range(4):
        createstreetlamp(positions.add(startpos, pos(-outsize + (2*outsize *(i%2)), 0, -outsize + (2*outsize *(i//2)))))


def createstreetlamp(setpos):
    blocks.place(STONE_BRICKS, setpos)
    blocks.fill(NETHER_BRICK_FENCE, positions.add(setpos, pos(0, 1, 0)), positions.add(setpos, pos(0, 5, 0)), FillOperation.REPLACE)
    blocks.place(OCHRE_FROGLIGHT, positions.add(setpos, pos(0, 5, 0)))

def CreateStreet(setpos):
    blocks.fill(STONE_BRICKS, positions.add(setpos, pos(-size, 0, -size)),
            positions.add(setpos, pos(size, 0, size)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(setpos, pos(-size, 1, -size)),
            positions.add(setpos, pos(size, 20, size)), FillOperation.REPLACE)

player.on_chat("run", on_on_chat)
