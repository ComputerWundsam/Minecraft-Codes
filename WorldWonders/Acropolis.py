startpos = player.position()
roofsegments = 6
segmentwidth = 7
adepth = 140
pillarheight = 30

def on_on_chat():
    global startpos
    startpos = player.position()
    loops.pause(5000)
    flatten()
    createground()
    for i in range(roofsegments):
        createpillar(positions.add(startpos, pos(segmentwidth * i, 0, 3)))
        createpillar(positions.add(startpos, pos(segmentwidth * i, 0, adepth - 3)))
        createpillar(positions.add(startpos, pos(-segmentwidth * i, 0, 3)))
        createpillar(positions.add(startpos, pos(-segmentwidth * i, 0, adepth - 3)))
    for i in range(adepth/segmentwidth - 2):
        createpillar(positions.add(startpos, pos(roofsegments*(segmentwidth-1)-1, 0, 3 + segmentwidth + segmentwidth*i)))
        createpillar(positions.add(startpos, pos(-roofsegments*(segmentwidth-1)+1, 0, 3 + segmentwidth + segmentwidth*i)))
    createroof(positions.add(startpos, pos(0, pillarheight+1, 0)))
player.on_chat("run", on_on_chat)

def flatten():
    for i in range(pillarheight+5):
        blocks.fill(AIR, positions.add(startpos, pos(-roofsegments*segmentwidth-10, pillarheight-i-1, -10)), positions.add(startpos, pos(roofsegments*segmentwidth+10, pillarheight-i-1, adepth+10)), FillOperation.REPLACE)

def createground():
    blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(-segmentwidth * roofsegments, -1, 0)), positions.add(startpos, pos(segmentwidth * roofsegments, -1, adepth)), FillOperation.REPLACE)
    for i in range(5):
            blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 0), positions.add(startpos, pos(-segmentwidth * roofsegments-1-i, -1-i, -1-i)),
                                                                        positions.add(startpos, pos(-segmentwidth * roofsegments - i - 1, -1-i, adepth+1+i)), FillOperation.REPLACE)
            blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 1), positions.add(startpos, pos(segmentwidth * roofsegments+1+i, -1-i, -1-i)),
                                                                        positions.add(startpos, pos(segmentwidth * roofsegments + i + 1, -1-i, adepth+1+i)), FillOperation.REPLACE)
            blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 2), positions.add(startpos, pos(-segmentwidth * roofsegments-1-i, -1-i, -1-i)), 
                                                                        positions.add(startpos, pos(segmentwidth * roofsegments + i + 1, -1-i, -1-i)), FillOperation.REPLACE)
            blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 3), positions.add(startpos, pos(-segmentwidth * roofsegments-1-i, -1-i, adepth+1+i)), 
                                                                        positions.add(startpos, pos(segmentwidth * roofsegments + i + 1, -1-i, adepth+1+i)), FillOperation.REPLACE)


def createroof(setpos: any):
    global segmentwidth
    for j in range(roofsegments):
        blocks.fill(BLOCK_OF_QUARTZ,
            positions.add(setpos,
                pos(-segmentwidth * j - (segmentwidth - 1),
                    1 + roofsegments - j,
                    0)),
            positions.add(setpos, pos(-segmentwidth * j, 0, adepth)),
            FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_QUARTZ,
            positions.add(setpos,
                pos(segmentwidth * j + (segmentwidth - 1),
                    1 + roofsegments - j,
                    0)),
            positions.add(setpos, pos(segmentwidth * j, 0, adepth)),
            FillOperation.REPLACE)
def createpillar(setpos2: any):
    blocks.fill(PILLAR_QUARTZ_BLOCK,
        positions.add(setpos2, pos(-1, 0, -1)),
        positions.add(setpos2, pos(1, pillarheight, 1)),
        FillOperation.REPLACE)
    for k in range(2):
        for l in range(2):
            blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 0 + 4 * k + l),
                positions.add(setpos2, pos(-2 + 4 * l, k * pillarheight, -2)),
                positions.add(setpos2, pos(-2 + 4 * l, k * pillarheight, 2)))
            blocks.fill(blocks.block_with_data(QUARTZ_STAIRS, 2 + 4 * k + l),
                positions.add(setpos2, pos(-2, k * pillarheight, -2 + 4 * l)),
                positions.add(setpos2, pos(2, k * pillarheight, -2 + 4 * l)))
