layers = 4
height = 8
distance = 10
size = 14

def on_on_chat():
    startpos = player.position()
    for i in range(layers):
        blocks.fill(REDSTONE_LAMP , positions.add(startpos, pos(distance, i*height, distance)), positions.add(startpos, pos(distance+size, height+i*height, distance+size)), FillOperation.REPLACE)
        player.execute("fill " + positions.add(startpos, pos(distance+1, 0+i*height, distance+1)) + " " + positions.add(startpos, pos(distance+size-1, height+i*height-1, distance+size-1)) + " sculk_sensor")
        blocks.fill(IRON_TRAPDOOR , positions.add(startpos, pos(distance+2, i*height+height/2, distance+2)), positions.add(startpos, pos(distance+size-2, i*height+height/2, distance+size-2)), FillOperation.REPLACE)
        blocks.fill(AIR , positions.add(startpos, pos(distance+3, i*height, distance+3)), positions.add(startpos, pos(distance+size-3, height+i*height-2, distance+size-3)), FillOperation.REPLACE)
player.on_chat("run", on_on_chat)
