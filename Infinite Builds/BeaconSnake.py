radius = 30
pi = 3.14159265359
mod = 1
size = 1
randomglass = [BLACK_STAINED_GLASS, BLUE_STAINED_GLASS, BROWN_STAINED_GLASS, CYAN_STAINED_GLASS, GRAY_STAINED_GLASS, GREEN_STAINED_GLASS, LIGHT_BLUE_STAINED_GLASS, LIGHT_GRAY_STAINED_GLASS, LIME_STAINED_GLASS, 
MAGENTA_STAINED_GLASS, ORANGE_STAINED_GLASS, PINK_STAINED_GLASS, PURPLE_STAINED_GLASS, RED_STAINED_GLASS, WHITE_STAINED_GLASS, YELLOW_STAINED_GLASS]


def on_on_chat():
    global mod
    startpos = player.position()
    while True:
        for i in range(radius*pi):
            xvalue = Math.sin(i/radius)*radius*mod
            zvalue = Math.cos(i/radius)*radius
            blocks.fill(IRON_BLOCK, positions.add(startpos, pos(xvalue-size, -1, zvalue-size)), positions.add(startpos, pos(xvalue+size, 0, zvalue+size)))
            blocks.place(BEACON, positions.add(startpos, pos(xvalue, 1, zvalue)))
            blocks.place(randomglass[randint(0, randomglass.length-1)], positions.add(startpos, pos(xvalue, 2, zvalue)))
        startpos = positions.add(startpos, pos(0, 0, -2*radius))
        mod = mod * -1
        
player.on_chat("run", on_on_chat)
