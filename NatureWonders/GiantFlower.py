pi = 3.14159265359
radius = 8
oradius = 30
c = 12
startpos = pos(0, 0, 0)

def on_on_chat():
    global startpos
    iradius = oradius - radius
    startpos = player.position()
    loops.pause(5000)
    for i in range(iradius*2):
        blocks.fill(DIAMOND_BLOCK, positions.add(startpos, pos(Math.sin(i/iradius)*iradius, Math.cos(i/iradius)*iradius, 0)), 
                                    positions.add(startpos, pos(-Math.sin(i/iradius)*iradius, Math.cos(i/iradius)*iradius, 0)), FillOperation.REPLACE)
        blocks.fill(DIAMOND_BLOCK, positions.add(startpos, pos(Math.sin(i/iradius)*iradius, -Math.cos(i/iradius)*iradius, 0)), 
                                    positions.add(startpos, pos(-Math.sin(i/iradius)*iradius, -Math.cos(i/iradius)*iradius, 0)), FillOperation.REPLACE)
    for i in range(c):
        value = ((i*pi)/(c*radius))*2*radius
        createcircle(positions.add(startpos, pos(Math.sin(value)*oradius, Math.cos(value)*oradius, 0)))
player.on_chat("run", on_on_chat)




def createcircle(setpos):
    for i in range(radius*pi):
        blocks.fill(GOLD_BLOCK, positions.add(setpos, pos(Math.sin(i/radius)*radius-1, Math.cos(i/radius)*radius-1, -1)), 
                                positions.add(setpos, pos(Math.sin(i/radius)*radius+1, Math.cos(i/radius)*radius+1, 1)), FillOperation.REPLACE)
        blocks.fill(GOLD_BLOCK, positions.add(setpos, pos(-Math.sin(i/radius)*radius-1, Math.cos(i/radius)*radius-1, -1)),
                                positions.add(setpos, pos(-Math.sin(i/radius)*radius+1, Math.cos(i/radius)*radius+1, 1)), FillOperation.REPLACE)
