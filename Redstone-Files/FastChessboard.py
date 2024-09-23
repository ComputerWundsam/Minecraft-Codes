checkeredplates = [WHITE_CONCRETE, BLACK_CONCRETE]

boardsize = 500

def on_chat():
    startpos = positions.add(player.position(), pos(0, -1, 0))
    createflooring(startpos, positions.add(startpos, pos(11, 0, boardsize)))
player.on_chat("run", on_chat)


def createflooring(beginpos: Position  ,endpos: Position):
    player.say(beginpos)
    setx = endpos.get_value(Axis.X) - beginpos.get_value(Axis.X)
    setz = endpos.get_value(Axis.Z) - beginpos.get_value(Axis.Z)
    blocks.fill(AIR, endpos, positions.add(endpos, pos(1, 0, -setz)), FillOperation.REPLACE)
    for i in range(setx+1):
        blocks.fill(checkeredplates[i%checkeredplates.length], positions.add(beginpos, pos(i, 0, 0)), positions.add(beginpos, pos(i, 0, setz)), FillOperation.REPLACE)
    for i in range(setz/2):
        blocks.place(blocks.block_with_data(PISTON, 4), positions.add(beginpos,pos(-1, 0, 2*i+1)))
        blocks.place(REDSTONE_BLOCK, positions.add(beginpos,pos(-2, 0, 2*i+1)))
    loops.pause(boardsize)
    blocks.fill(AIR, positions.add(beginpos,pos(-2, 0, setz)), beginpos, FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(endpos, pos(1, 0, 0)), positions.add(endpos, pos(1, 0, -setz)), FillOperation.REPLACE)
