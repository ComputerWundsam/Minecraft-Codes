
def on_on_chat():
  #counter necessary for changing blocks
    counter = 0
  #startpos makes the position absoulute
    startpos = player.position()
    while True:
        #based on the counter, it changes whether it should be fire or magma blocks
        if(counter % 2 == 0):
            blocks.fill(MAGMA_BLOCK, 
                positions.add(startpos, pos(-3, counter, -3)), 
                positions.add(startpos, pos(3, counter, 3)))
        else:
            blocks.fill(FIRE, 
                positions.add(startpos, pos(-3, counter, -3)), 
                positions.add(startpos, pos(3, counter, 3)))
        #fills inside of tower with air
        blocks.fill(AIR, 
            positions.add(startpos, pos(-2, counter, -2)), 
            positions.add(startpos, pos(2, counter, 2)))
        counter += 1
player.on_chat("run", on_on_chat)
