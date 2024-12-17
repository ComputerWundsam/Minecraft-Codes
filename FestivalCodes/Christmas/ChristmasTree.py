ornaments = ORANGE_CONCRETE, MAGENTA_CONCRETE, LIGHT_BLUE_CONCRETE, YELLOW_CONCRETE, LIME_CONCRETE, PINK_CONCRETE, CYAN_CONCRETE, PURPLE_CONCRETE, BLUE_CONCRETE, RED_CONCRETE, SHROOMLIGHT, OCHRE_FROGLIGHT, VERDANT_FROGLIGHT, PEARLESCENT_FROGLIGHT, GLOWSTONE, SEA_LANTERN
oradius = 32
layers = 8
pi = 3.14159265359

def on_on_chat():
    startpos = player.position()
    for i in range(2*pi):
        blocks.fill(LOG_SPRUCE, positions.add(startpos, pos(-Math.sin(i/2)*2, 0, Math.cos(i/2)*2)), positions.add(startpos, pos(Math.sin(i/2)*2, layers*6, Math.cos(i/2)*2)), FillOperation.REPLACE)
        blocks.replace(LEAVES_SPRUCE, AIR, positions.add(startpos, pos(-Math.sin(i/2)*2-1, -1, Math.cos(i/2)*2-1)), positions.add(startpos, pos(Math.sin(i/2)*2+1, layers*6+1, Math.cos(i/2)*2+1)))
    for i in range(2*pi):
        blocks.fill(RED_CONCRETE, positions.add(startpos, pos((-2*pi+i)/2, layers*6+2+i, (-2*pi+i)/2)), positions.add(startpos, pos((2*pi-i)/2, layers*6+2+i, (2*pi-i)/2)), FillOperation.REPLACE)
    for k in range(layers):
        radius = oradius - 2*k
        c = randint(radius/3, radius/2)    
        for i in range(c):
            for j in range(radius +1):
                diff = Math.cos(j/(2*radius))
                value = (2*pi*i)/(c)
                blocks.place(LOG_SPRUCE, positions.add(startpos, pos(Math.sin(value)*j * diff, (k+1)*6, Math.cos(value)*j  * diff)))
                blocks.replace(LEAVES_SPRUCE, AIR, positions.add(startpos, pos(Math.sin(value)*j * diff-1, (k+1)*6-1, Math.cos(value)*j  * diff-1)), positions.add(startpos, pos(Math.sin(value)*j * diff+1, (k+1)*6+1, Math.cos(value)*j  * diff+1)))
            blocks.fill(ornaments[randint(0, ornaments.length-1)], positions.add(startpos, pos(Math.sin(value)*j * diff-1, (k+1)*6-2, Math.cos(value)*j  * diff-1)), positions.add(startpos, pos(Math.sin(value)*j * diff+1, (k+1)*6-3, Math.cos(value)*j  * diff+1)))
player.on_chat("run", on_on_chat)
