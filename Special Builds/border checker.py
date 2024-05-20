directions = [pos(1, 0, 0),  pos(0, 0, 1), pos(-1, 0, 0), pos(0, 0, -1)]
wallsize = 15

def on_on_chat():
    directionint = 0 
    counter = 0
    startpos = positions.add(player.position().to_world(), pos(0, -1,0))
    loops.pause(5000)
    endpos = positions.add(startpos, pos(0, 0, 1))
    blocks.fill(COBBLESTONE, positions.add(startpos, pos(0, 1, 0)), positions.add(startpos, pos(0, wallsize, 0)))
    while(not positions.equals(startpos, endpos)):
        blocks.fill(COBBLESTONE, positions.add(endpos, pos(0, 1, 0)), positions.add(endpos, pos(0, wallsize, 0)))
        if(counter%4 == 2):
            blocks.fill(AIR, positions.add(endpos, pos(0, wallsize*3/5, 0)), positions.add(endpos, pos(0, wallsize*4/5, 0)))
        if(counter%2 == 0):
            blocks.place(COBBLESTONE, positions.add(endpos, pos(0, wallsize+1, 0)))
            if(counter%50 == 48):
                blocks.fill(OAK_FENCE, positions.add(endpos, pos(0, wallsize+2, 0)), positions.add(endpos, pos(0, wallsize+5, 0)))
                blocks.fill(BLUE_WOOL, positions.add(endpos, pos(1, wallsize+3, 0)), positions.add(endpos, pos(4, wallsize+5, 0)))
        for i in range(4):
            if(not blocks.test_for_block(AIR, positions.add(endpos, directions[abs((directionint+i-1)%4)]))): 
                endpos = positions.add(endpos, directions[abs((directionint+i-1)%4)])
                directionint += i-1
                break
        counter += 1
player.on_chat("run", on_on_chat)

def on_travelled_walk():
    blocks.replace(AIR, COBBLESTONE, pos(-20, 0, -20), pos(20, 15, 20))
    blocks.replace(AIR, OAK_FENCE, pos(-20, 0, -20), pos(20, 15, 20))
    blocks.replace(AIR, BLUE_WOOL, pos(-20, 0, -20), pos(20, 15, 20))

#player.on_travelled(FLY, on_travelled_walk)
