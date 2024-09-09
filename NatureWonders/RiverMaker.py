xdir = [1, 0, -1, 0]
zdir = [0, -1, 0, 1]
size = 3
radius = 8
pi = 3.14159265359

startpos = player.position()
def on_on_chat():
    c = 100
    global startpos
    startpos = positions.add(player.position(), pos(0, -1, 0))

    for i in range(200):
        if c <= 4:
            c += 100
        blocks.fill(WATER, positions.add(startpos, pos(-size, 0, -size)), positions.add(startpos, pos(size, -2, size)), FillOperation.REPLACE)
        startpos = positions.add(startpos, pos(xdir[c%xdir.length], 0, zdir[c%zdir.length]))
        dirs = randint(0, 20)
        if(dirs < 2):
            startpos = positions.add(startpos, pos(xdir[(c+1)%xdir.length], 0, zdir[(c+1)%zdir.length]))
            dirs = randint(0, 20)
            if dirs < 5:
                c += 1
                #createcurve(positions.add(startpos, pos(xdir[(c)%xdir.length]*radius, 0, zdir[(c)%zdir.length]*radius)), c-1, c)

        elif (dirs > 18):
            startpos = positions.add(startpos, pos(xdir[(c-1)%xdir.length], 0, zdir[(c-1)%zdir.length]))
            dirs = randint(0, 20)
            if dirs < 5:
                #createcurve(positions.add(startpos, pos(xdir[(c-1)%xdir.length]*radius, 0, zdir[(c-1)%zdir.length]*radius)), c-1, c)
                c -= 1

def createcurve(setpos, fc, sc, c):
    setx = xdir[fc%xdir.length]+xdir[sc%xdir.length]
    setz = zdir[fc%zdir.length]+zdir[sc%zdir.length]
    change = c%xdir.length*(pi/2)

    for i in range(radius*pi/2):
        blocks.fill(WATER, positions.add(setpos, pos(Math.sin((i+change)/radius*setx)*radius-size, 0, Math.cos((i+change)/radius*setx)*radius-size)), 
                            positions.add(setpos, pos(Math.sin((i+change)/radius*setz)*radius+size, -2, Math.cos((i+change)/radius*setz)*radius+size)), FillOperation.REPLACE)

player.on_chat("run", on_on_chat)

testpos = pos(0, -1, 0).to_world()
for i in range(4):
    createcurve(testpos, i, i+1, 12+i)
