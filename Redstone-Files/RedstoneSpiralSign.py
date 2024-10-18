size = 8
switchsize = 4

def on_on_chat():
    startpos = player.position()
    blocks.fill(REDSTONE_LAMP, positions.add(startpos, pos(-size, -size, 0)), positions.add(startpos, pos(size, size, 0)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 2), positions.add(startpos, pos(-size, -size, -1)), positions.add(startpos, pos(size, size, -1)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 0), positions.add(startpos, pos(0, 1, -2)), positions.add(startpos, pos(0, size, -2)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 1), positions.add(startpos, pos(0, -size, -2)), positions.add(startpos, pos(0, -1, -2)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 5), positions.add(startpos, pos(-size, 0, -2)), positions.add(startpos, pos(-1, 0, -2)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(OBSERVER, 4), positions.add(startpos, pos(size, 0, -2)), positions.add(startpos, pos(1, 0, -2)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(OBSERVER, 2), positions.add(startpos, pos(0, 0, -2)))
    createspiral(positions.add(startpos, pos(1, 1, -2)), 1, 1)
    createspiral(positions.add(startpos, pos(-1, 1, -2)), -1, 1)
    createspiral(positions.add(startpos, pos(-1, -1, -2)), -1, -1)
    createspiral(positions.add(startpos, pos(1, -1, -2)), 1, -1)
    createswitch(positions.add(startpos, pos(0, 0, -3)))

player.on_chat("run", on_on_chat)


def createspiral(setpos, dx, dy):
    psize = size -1
    for i in range(psize/2):
        blocks.replace(blocks.block_with_data(OBSERVER, 4.5 - dx*0.5), AIR, positions.add(setpos, pos(dx*i, dy*i, 0)), positions.add(setpos, pos((psize-(2*i))*dx+dx*i, dy*i, 0)))
        blocks.replace(blocks.block_with_data(OBSERVER, 0.5 - dy*0.5), AIR, positions.add(setpos, pos((psize-(2*i))*dx+i*dx, (psize-(2*i))*dy+i*dy, 0)), positions.add(setpos, pos((psize-(2*i))*dx+i*dx, dy*i, 0)))
        blocks.replace(blocks.block_with_data(OBSERVER, 4.5 +  dx*0.5), AIR, positions.add(setpos, pos(psize*dx-i*dx, dy*psize-i*dy, 0)), positions.add(setpos, pos(i*dx, dy*psize-i*dy, 0)))
        blocks.replace(blocks.block_with_data(OBSERVER, 0.5 + dy*0.5), AIR, positions.add(setpos, pos(i*dx, psize*dy-i*dy, 0)), positions.add(setpos, pos(i*dx, i*dy, 0)))

def createswitch(setpos):
    blocks.fill(GRASS, positions.add(setpos, pos(0, -1, 0)), positions.add(setpos, pos(-1, -1, -switchsize-2)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(REPEATER, 14), positions.add(setpos, pos(0, 0, -1)), positions.add(setpos, pos(0, 0, -switchsize-1)), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(REPEATER, 12), positions.add(setpos, pos(-1, 0, -1)), positions.add(setpos, pos(-1, 0, -switchsize-1)), FillOperation.REPLACE)
    blocks.place(REDSTONE, positions.add(setpos, pos(0, 0, 0)))
    blocks.place(REDSTONE, positions.add(setpos, pos(-1, 0, 0)))
    blocks.place(REDSTONE, positions.add(setpos, pos(0, 0, -switchsize-2)))
    blocks.place(REDSTONE, positions.add(setpos, pos(-1, 0, -switchsize-2)))
    blocks.place(REDSTONE_BLOCK, positions.add(setpos, pos(-2, 0, -switchsize-2)))
    loops.pause(100*switchsize)
    blocks.place(AIR, positions.add(setpos, pos(-2, 0, -switchsize-2)))

#4 = links
#5 = rechts
#0
#1
