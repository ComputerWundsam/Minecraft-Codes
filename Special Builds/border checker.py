directions = [pos(1, 0, 0),  pos(0, 0, 1), pos(-1, 0, 0), pos(0, 0, -1)]

wallsize = 1
startpos = pos(0, 0, 0)
endpos = pos(0, 0, 0)

def on_on_chat():
    counter = 0
    global startpos, endpos 
    startpos = positions.add(player.position().to_world(), pos(0, -1,0))
    player.say(startpos)
    endpos = positions.add(startpos, pos(0, 0, 1))
    blocks.fill(STONE_BRICKS, positions.add(startpos, pos(0, 1, 0)), positions.add(startpos, pos(0, wallsize, 0)))
    while(not positions.equals(startpos, endpos)):
        blocks.fill(STONE_BRICKS, positions.add(endpos, pos(0, 1, 0)), positions.add(endpos, pos(0, wallsize, 0)))
        for i in range(4):
            if(not blocks.test_for_block(AIR, positions.add(endpos, directions[abs((counter+i-1)%4)]))): 
                endpos = positions.add(endpos, directions[abs((counter+i-1)%4)])
                player.say(endpos)
                counter += i-1
                break
        if(startpos == endpos):
            player.say("hi")

player.on_chat("run", on_on_chat)
