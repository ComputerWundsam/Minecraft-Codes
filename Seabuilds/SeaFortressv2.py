radius = 50
pi = 3.14159265359
ringsize = 2
height = 20
tcount = 12
towersize = 6

def on_on_chat():
    global towersize 
    towersize = 3*ringsize
    startpos = player.position()
    loops.pause(5000)
    for i in range(2*radius*pi):
        blocks.fill(IRON_BLOCK, positions.add(startpos, pos(Math.sin(i/radius)*radius-ringsize, height, Math.cos(i/radius)*radius-ringsize)), 
                                positions.add(startpos, pos(Math.sin(i/radius)*radius+ringsize, 0, Math.cos(i/radius)*radius+ringsize)), FillOperation.REPLACE)
        blocks.fill(IRON_BLOCK, positions.add(startpos, pos(0, height, 0)),
                                positions.add(startpos, pos(Math.sin(i/radius)*radius+ringsize, height, Math.cos(i/radius)*radius+ringsize)), FillOperation.REPLACE)
    tpos = 2*radius*pi/tcount
    for i in range(tcount):
        createtower(positions.add(startpos, pos(Math.sin((i*tpos)/radius)*radius, 0, Math.cos((i*tpos)/radius)*radius)), towersize)
    createtower(startpos, towersize+3)

    


def createtower(setpos, setsize):
    for i in range(setsize+1):
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(setpos, pos(-setsize+i, height*i, -setsize+i)),
            positions.add(setpos, pos(setsize-i, height*i+height, setsize-i)), FillOperation.REPLACE)
        for j in range(setsize):
            blocks.replace(GLASS, BLOCK_OF_NETHERITE, positions.add(setpos, pos(-setsize+1+i+(2*j), height*i+1, -setsize)),
                            positions.add(setpos, pos(-setsize+1+i+(2*j), height*i+height-2, setsize)))
            blocks.replace(GLASS, BLOCK_OF_NETHERITE, positions.add(setpos, pos(-setsize, height*i+1, -setsize+1+i+(2*j))),
                            positions.add(setpos, pos(setsize, height*i+height-2, -setsize+1+i+(2*j))))

player.on_chat("run", on_on_chat)


def on_chat():
    createtower(player.position(), towersize)
player.on_chat("jump", on_chat)
