glasses = [RED_STAINED_GLASS, ORANGE_STAINED_GLASS, PINK_STAINED_GLASS, YELLOW_STAINED_GLASS, LIME_STAINED_GLASS, GREEN_STAINED_GLASS, LIGHT_BLUE_STAINED_GLASS, CYAN_STAINED_GLASS, BLUE_STAINED_GLASS, MAGENTA_STAINED_GLASS, PURPLE_STAINED_GLASS, BROWN_STAINED_GLASS, GRAY_STAINED_GLASS, LIGHT_GRAY_STAINED_GLASS, BLACK_STAINED_GLASS]
pi = 3.14159265359

radius = 1
firstno = 1
secondno = 1
size = 1

c = 1
inv = 1

def on_on_chat():
    global radius, firstno, secondno, inv

    startpos = player.position()
    r = randint(0, glasses.length)
    
    for i in range(8):
        radius = firstno + secondno
        secondno = firstno
        firstno = radius
        cradius = radius*c
        for j in range(cradius*pi/2):
            blocks.fill(BLOCK_OF_NETHERITE, 
                positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius * inv -size, 0, Math.cos((i*pi/2)+j/cradius)*cradius -size)), 
                positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius * inv +size, 10-i, Math.cos((i*pi/2)+j/cradius)*cradius + size)), FillOperation.REPLACE)
            blocks.place(BEACON, positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius * inv, 10-i+1, Math.cos((i*pi/2)+j/cradius)*cradius)))
            blocks.place(glasses[r%glasses.length], positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius * inv, 10-i+2, Math.cos((i*pi/2)+j/cradius)*cradius)))
            r += 1
        if i  % 2 == 0:
            if i  % 4 == 0:
                startpos = positions.add(startpos, pos(-secondno*c* inv, 0, 0))
            else:
                startpos = positions.add(startpos, pos(secondno*c* inv, 0, 0))
        else:
            if i % 4 == 1:
                startpos = positions.add(startpos, pos(0, 0, secondno*c ))
            else:
                startpos = positions.add(startpos, pos(0, 0, -secondno*c))
player.on_chat("run", on_on_chat)
