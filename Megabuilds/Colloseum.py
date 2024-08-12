pi = 3.14159265359
doorcount = 48
h = 10
bows = [0, 7, 7, 8, 7, 7, 0]
stairarray = [[5, 4], [6, 7], [4, 5], [7, 6], [5, 4]]
startpos = pos(0, 0, 0)
radius = bows.length*doorcount/(2*pi)

def on_on_chat():
    global startpos
    startpos = player.position()
    flatten()
    createground()
    createwalls()

def flatten():
    for i in range(70):
        blocks.fill(AIR, positions.add(startpos, pos(-radius, 70-i, -radius)), positions.add(startpos,  pos(radius, 70-i, radius)), FillOperation.REPLACE)

def createground():
    for i in range(2*radius*pi):
        blocks.fill(RED_SANDSTONE, startpos, positions.add(startpos, pos(Math.sin(i/radius)*radius, -5, Math.cos(i/radius)*radius)))
    iradius = radius - 2*h-2
    for j in range(2*iradius*pi):
        blocks.fill(AIR, startpos, positions.add(startpos,pos(Math.sin(j/(iradius-1))*(iradius-1), -4, Math.cos(j/(iradius-1))*(iradius-1))))
    createarena(iradius)

def createarena(iradius):
    for k in range(2*h+1):
        for j in range(2*(iradius+k)*pi):
            blocks.fill(SANDSTONE, positions.add(startpos,pos(Math.sin(j/(iradius+k))*(iradius+k)-1, k, Math.cos(j/(iradius+k))*(iradius+k)-1)), positions.add(startpos,pos(Math.sin(j/(iradius+k))*(iradius+k)+1, k, Math.cos(j/(iradius+k))*(iradius+k)+1)))


def createwalls():
    for j in range(3):
        eighth = radius*pi/4
        ecount = 0
        for i in range (2*radius*pi):
            blocks.fill(SANDSTONE, positions.add(startpos, pos(Math.sin(i/radius)*radius, bows[i%bows.length]+h*j, Math.cos(i/radius)*radius)), positions.add(startpos, pos(Math.sin(i/radius)*radius, h-1+h*j, Math.cos(i/radius)*radius)), FillOperation.REPLACE)
            blocks.fill(SANDSTONE, positions.add(startpos, pos(Math.sin(i/radius)*radius-1, h+h*j, Math.cos(i/radius)*radius -1)), positions.add(startpos, pos(Math.sin(i/radius)*radius +1, h+h*j, Math.cos(i/radius)*radius+1)), FillOperation.REPLACE)
            if i > eighth:
                eighth += radius*pi/2    
                ecount += 1
            if(i%bows.length == 1):
                blocks.place(blocks.block_with_data(SANDSTONE_STAIRS, stairarray[ecount][0]), positions.add(startpos, pos(Math.sin(i/radius)*radius, bows[i%bows.length]+h*j-1, Math.cos(i/radius)*radius)))
            elif(i%bows.length == bows.length//2):
                blocks.place(blocks.block_with_data(SANDSTONE_SLAB, 8), positions.add(startpos, pos(Math.sin(i/radius)*radius, bows[i%bows.length]+h*j-1, Math.cos(i/radius)*radius)))
            elif (i%bows.length == bows.length-2):
                blocks.place(blocks.block_with_data(SANDSTONE_STAIRS, stairarray[ecount][1]), positions.add(startpos, pos(Math.sin(i/radius)*radius, bows[i%bows.length]+h*j-1, Math.cos(i/radius)*radius)))
    for i in range(2*radius*pi):
        blocks.fill(SANDSTONE, positions.add(startpos, pos(Math.sin(i/radius)*radius, h*j, Math.cos(i/radius)*radius)), positions.add(startpos, pos(Math.sin(i/radius)*radius, h+h*j, Math.cos(i/radius)*radius)), FillOperation.REPLACE)
        blocks.fill(SANDSTONE, positions.add(startpos, pos(Math.sin(i/radius)*radius-1, h+h*j, Math.cos(i/radius)*radius -1)), positions.add(startpos, pos(Math.sin(i/radius)*radius +1, h+h*j, Math.cos(i/radius)*radius+1)), FillOperation.REPLACE)
        if(i%bows.length == bows.length//2):
            blocks.place(AIR, positions.add(startpos, pos(Math.sin(i/radius)*radius, h*j+h/2, Math.cos(i/radius)*radius)))



player.on_chat("run", on_on_chat)
