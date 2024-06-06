wallbrick = BLOCK_OF_QUARTZ
glassblock = GLASS
groundbrick = LIGHT_BLUE_CONCRETE
roofblock = GOLD_BLOCK


bigonion = [10, 7, 4, 5, 7, 8, 8, 8, 7, 7, 6, 6, 5, 4, 3, 1]
doorbow = [0, 3, 5, 6, 7, 8, 9]

uwidth = 20
height = 15

startpos = player.position()

def createwalls():
    for j in range(2):
        for i in range(uwidth):
            #x walls
            blocks.fill(wallbrick, positions.add(startpos, pos(-uwidth-4+i, 0, 2*j*(uwidth+8))), positions.add(startpos, pos(-uwidth-4+i, height, 2*j*(uwidth+8))))
            blocks.fill(wallbrick, positions.add(startpos, pos(uwidth+4-i, 0, 2*j*(uwidth+8))), positions.add(startpos, pos(uwidth+4-i, height, 2*j*(uwidth+8))))
            blocks.fill(groundbrick, positions.add(startpos, pos(-uwidth-4+i, 0, 2*j*(uwidth+8)-1)), positions.add(startpos, pos(-uwidth-4+i, 3, 2*j*(uwidth+8)+1)))
            blocks.fill(groundbrick, positions.add(startpos, pos(uwidth+4-i, 0, 2*j*(uwidth+8)-1)), positions.add(startpos, pos(uwidth+4-i, 3, 2*j*(uwidth+8)+1)))
            #z walls
            blocks.fill(wallbrick, positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), 0, i+8)), positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), height, i+8)))
            blocks.fill(wallbrick, positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), 0, 2*uwidth+6-i)), positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), height, 2*uwidth+6-i)))
            blocks.fill(groundbrick, positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12)-1, 0, i+8)), positions.add(startpos, pos(2*j*(uwidth+12)+1 - (uwidth+12), 3, i+8)))
            blocks.fill(groundbrick, positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12)-1, 0, 2*uwidth+6-i)), positions.add(startpos, pos(2*j*(uwidth+12)+1 - (uwidth+12), 3, 2*uwidth+6-i)))
            if (i % 2 == 1):
                #x windows
                blocks.fill(glassblock, positions.add(startpos, pos(-uwidth-4+i, height/5, 2*j*(uwidth+8))), positions.add(startpos, pos(-uwidth-4+i, (height*3)/4, 2*j*(uwidth+8))))
                blocks.fill(glassblock, positions.add(startpos, pos(uwidth+4-i, height/5, 2*j*(uwidth+8))), positions.add(startpos, pos(uwidth+4-i, (height*3)/4, 2*j*(uwidth+8))))
                #z windows
                blocks.fill(glassblock, positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), height/5, i+8)), positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), (height*3)/4, i+8)))
                blocks.fill(glassblock, positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), height/5, 2*uwidth-i+6)), positions.add(startpos, pos(2*j*(uwidth+12) - (uwidth+12), (height*3)/4, 2*uwidth-i+6)))


def createtowers():
    global startpos
    for i in range(height+1):
        if i < 3:
            setbrick = groundbrick
        else:
            setbrick = wallbrick
        shapes.circle(setbrick, positions.add(startpos, pos(0, i, 0)), 5, Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(setbrick, positions.add(startpos, pos(0, i, 2*uwidth+16)), 5, Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(setbrick, positions.add(startpos, pos(-uwidth-12, i, 0)), 9, Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(setbrick, positions.add(startpos, pos(uwidth+12, i, 0)), 9, Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(setbrick, positions.add(startpos, pos(uwidth+12, i, 2*uwidth+16)), 9, Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(setbrick, positions.add(startpos, pos(-uwidth-12, i, 2*uwidth+16)), 9, Axis.Y, ShapeOperation.REPLACE)
    for i in range(bigonion.length):
        shapes.circle(roofblock, positions.add(startpos, pos(-uwidth-12, i+height+1, 0)), bigonion[i], Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(roofblock, positions.add(startpos, pos(uwidth+12, i+height+1, 0)), bigonion[i], Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(roofblock, positions.add(startpos, pos(uwidth+12, i+height+1, 2*uwidth+16)), bigonion[i], Axis.Y, ShapeOperation.REPLACE)
        shapes.circle(roofblock, positions.add(startpos, pos(-uwidth-12, i+height+1, 2*uwidth+16)), bigonion[i], Axis.Y, ShapeOperation.REPLACE)
    

def createroof():
    global startpos
    for i in range(uwidth+13):
        if(i%2 == 0):
            setbrick = wallbrick
        else:
            setbrick = EMERALD_BLOCK
        blocks.fill(setbrick, positions.add(startpos, pos(uwidth-i+12, height-1, 0)), positions.add(startpos, pos(uwidth+12-i, height-1, 2*uwidth+16)))
        blocks.fill(setbrick, positions.add(startpos, pos(-uwidth-12+i, height-1, 0)), positions.add(startpos, pos(-uwidth-12+i, height-1, 2*uwidth+16)))

def createdoor():
    global startpos
    for i in range(doorbow.length-2):
        blocks.fill(AIR, positions.add(startpos, pos(doorbow.length-3-i, 0, -6)), positions.add(startpos, pos(doorbow.length-3-i, doorbow[i+1], 6)))
        blocks.fill(AIR, positions.add(startpos, pos(-doorbow.length+3+i, 0, -6)), positions.add(startpos, pos(-doorbow.length+3+i, doorbow[i+1], 6)))
        blocks.fill(groundbrick, positions.add(startpos, pos(doorbow.length-3-i, doorbow[i], -6)), positions.add(startpos, pos(doorbow.length-3-i, doorbow[i+1], 6)))
        blocks.fill(groundbrick, positions.add(startpos, pos(-doorbow.length+3+i, doorbow[i], -6)), positions.add(startpos, pos(-doorbow.length+3+i, doorbow[i+1], 6)))


def createtemple():
    global startpos
    startpos = player.position()
    loops.pause(5000)
    createwalls()
    createtowers()
    createdoor()
    createroof()

player.on_chat("run", createtemple)
