spiralsize = 2
pi = 3.14159265359
blockset = [RED_CONCRETE, ORANGE_CONCRETE, YELLOW_CONCRETE, LIME_CONCRETE, LIGHT_BLUE_CONCRETE, MAGENTA_CONCRETE]
startpos = player.position()

def on_on_chat():
    radius = spiralsize * blockset.length/pi
    global startpos
    blockoffset = [0]
    blockoffset.pop()
    startpos = player.position()
    for i in range(blockset.length):
        blockoffset.append((2*pi*radius)*(i/blockset.length))
    player.say(blockoffset[blockoffset.length-1])
    j = 0
    while True:
        for i in range(2*radius*pi):
            blocks.place(blockset[(i+j)%blockset.length], positions.add(startpos, pos(Math.sin(i/radius)*radius, j, Math.cos(i/radius)*radius)))
        j += 1


player.on_chat("run", on_on_chat)
