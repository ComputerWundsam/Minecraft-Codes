bsets = [POLISHED_ANDESITE, CLAY, LIGHT_GRAY_GLAZED_TERRACOTTA,LIGHT_GRAY_GLAZED_TERRACOTTA,BLUE_ICE,LIGHT_BLUE_WOOL]

def on_on_chat():
    startpos = player.position()
    loops.pause(5000)
    for i in range(100):
        for j in range(4):
            blocks.fill(AIR, positions.add(startpos, pos(0, -i,0)), positions.add(startpos, pos(-160+((2*160)*(j//2)), -i, -160+((2*160)*(j%2)))))
    for j in range(4):
            blocks.fill(GRASS, positions.add(startpos, pos(0, -100,0)), positions.add(startpos, pos(-160+((2*160)*(j//2)), -100, -160+((2*160)*(j%2)))))
    for i in range (xyzi.length):
        blocks.place(bsets[xyzi[i][3]], positions.add(startpos, pos(xyzi[i][0], xyzi[i][1], xyzi[i][2])))
player.on_chat("run", on_on_chat)
